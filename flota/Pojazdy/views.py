from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from Pojazdy.forms import AddVehicleForm, BT_Form, TACHO_Form, ADR_Form, EURO_Form, FRC_Form, UDT_Form, TDT_Form, SearchForm
from Pojazdy.forms import BridgeForm, UK_Form, BridgeDateForm
from .models import PojazdyModel, BT, tacho, ADR, NormaCzystosciSpalin, FRC, UDT, TDT, UKO
from django.db.models import Q
from datetime import date, datetime
# Create your views here.


class AddVehicleView(LoginRequiredMixin, View):
    def get(self, request):
        form = AddVehicleForm()
        ctx = {
            'form': form,
                   }
        return render(request, 'add_vehicle.html', ctx)
    def post(self, request):
        form = AddVehicleForm(request.POST)
        if form.is_valid():
            info = 'Dodano pojazd do bazy danych'
            new_vehicle = PojazdyModel.objects.create(**form.cleaned_data)
            return render(request, 'add_vehicle.html', {'form':form, 'info':info})
        else:
            info = 'Niepoprawne dane !'
            return render(request, 'add_vehicle.html', {'form': form, 'info': info})

class ShowVehicleView(LoginRequiredMixin, View):
    def get(self, request, select):
        if select == 0:
            pojazdy = PojazdyModel.objects.all()
            note = f"(wszystkie pojazdy). Pojazdów w bazie {len(pojazdy)}"
            return render(request, 'show_all.html', {'pojazdy': pojazdy, 'note': note})
        elif select == 1:
            pojazdy = PojazdyModel.objects.exclude(rodzaj__icontains="epa")
            note = f"(tylko samochody ciężarowe i ciągniki siodłowe).Pojazdów w bazie {len(pojazdy)}"
            return render(request, 'show_all.html', {'pojazdy': pojazdy, 'note': note})
        elif select == 2:
            pojazdy = PojazdyModel.objects.filter(rodzaj__icontains="epa")
            note = f"(tylko przyczepy i naczepy).Pojazdów w bazie {len(pojazdy)}"
            return render(request, 'show_all.html', {'pojazdy': pojazdy, 'note': note})


class DeleteVehicleView(LoginRequiredMixin, View):
    def get(self, request, id):
        vehicle = PojazdyModel.objects.get(id=id)
        vehicle.delete()
        return redirect('/wykaz_pojazdow/0/')

class SearchVehicleView(LoginRequiredMixin, View):
    def get(self, request):
        form = SearchForm(request.GET)
        form.is_valid()
        text = form.cleaned_data.get('text', '')
        result = PojazdyModel.objects.filter(
            Q(rodzaj__icontains=text)|
            Q(marka__icontains=text)|
            Q(model__icontains=text)|
            Q(VIN__icontains=text)|
            Q(nr_rej__icontains=text)
        )
        note = f"wyszukano {len(result)}"
        ctx ={
            'form': form,
            'pojazdy': result,
             'note': note,
             }
        return render(request, 'show_all.html', ctx)

class EditVehicleView(LoginRequiredMixin, View):
    def get(self, request, nr):
        p = PojazdyModel.objects.get(nr_rej=nr)
        form = AddVehicleForm(instance=p)
        ctx = {'form': form}
        return render(request, 'edit_vehicle.html', ctx)
    def post(self,request, nr):
        p = PojazdyModel.objects.get(nr_rej=nr)
        form = AddVehicleForm(request.POST, instance=p)
        if form.is_valid():
            form.save()
        return redirect("/wykaz_pojazdow/0/")

class BridgeEditView(LoginRequiredMixin, View):
    def get(self, request):
        form = BridgeForm()
        return render(request, 'bridge_edit.html', {'form': form})
    def post(self, request):
        form = BridgeForm(request.POST)
        if form.is_valid():
            object = PojazdyModel.objects.filter(id=form.cleaned_data['nr'])
            if len(object) > 0:
                return redirect(f'/edit/{object[0].nr_rej}')
            else:
                info = 'Brak pojazdu o takim ID'
                return render(request, 'bridge_edit.html', {'form': form, 'info': info})

class BridgeDelView(LoginRequiredMixin, View):
    def get(self, request):
        form = BridgeForm()
        return render(request, 'bridge_del.html', {'form': form})
    def post(self, request):
        form = BridgeForm(request.POST)
        if form.is_valid():
            object = PojazdyModel.objects.filter(id=form.cleaned_data['nr'])
            if object.exists():
                return redirect(f'/delete/{object[0].id}')
            else:
                info = 'Brak pojazdu o takim ID'
                return render(request, 'bridge_del.html', {'form': form, 'info': info})

class VehicleDetailsView(LoginRequiredMixin, View):
    def get(self, request, id):
        unit = PojazdyModel.objects.filter(id=id)
        today = date.today()
        return render(request, 'detail.html', {'unit': unit,'today': today})

class AddBtView(LoginRequiredMixin, View):
    def get(self, request, id):
        unit = PojazdyModel.objects.get(id=id)
        if BT.objects.filter(pojazd=unit).exists():
            bt_unit=BT.objects.get(pojazd=unit)
            form = BT_Form(instance=bt_unit)
        else:
            form = BT_Form()
        ctx = {'unit': unit, 'form': form}
        return render(request, 'add_BT.html', ctx)
    def post(self,request, id):
        unit = PojazdyModel.objects.get(id=id)
        form = BT_Form(request.POST)
        if form.is_valid():
            if BT.objects.filter(pojazd=unit).exists():
                record = BT.objects.update(nazwa="Przegląd techniczy pojazdu",
                                           instytucja=form.cleaned_data['instytucja'],
                                           wymagane=form.cleaned_data['wymagane'],
                                           data_konc=form.cleaned_data['data_konc'],
                                           pojazd=unit)
                return redirect(f'/details/{id}')
            else:
                f = BT(**form.cleaned_data)
                f.nazwa = "Przegląd techniczy pojazdu"
                f.pojazd = unit
                f.save()
                return redirect(f'/details/{id}')
        else:
            return redirect('wrong/')

class AddTachoView(LoginRequiredMixin, View):
    def get(self, request, id):
        unit = PojazdyModel.objects.get(id=id)
        if tacho.objects.filter(pojazd=unit).exists():
            bt_unit = tacho.objects.get(pojazd=unit)
            form = TACHO_Form(instance=bt_unit)
        else:
            form = TACHO_Form()
        ctx = {'unit': unit, 'form': form}
        return render(request, 'add_tacho.html', ctx)
    def post(self,request, id):
        unit = PojazdyModel.objects.get(id=id)
        form = TACHO_Form(request.POST)
        if form.is_valid():
            if tacho.objects.filter(pojazd=unit).exists():
                record = tacho.objects.update(nazwa="Przegląd urządzenia rejestrującego",
                                           instytucja=form.cleaned_data['instytucja'],
                                           wymagane=form.cleaned_data['wymagane'],
                                           data_konc=form.cleaned_data['data_konc'],
                                           pojazd=unit)
                return redirect(f'/details/{id}')
            else:
                f = tacho(**form.cleaned_data)
                f.nazwa = "Przegląd urządzenia rejestrującego",
                f.pojazd = unit
                f.save()
            return redirect(f'/details/{id}')
        else:
            return redirect('wrong/')
class AddAdrVehView(LoginRequiredMixin, View):
    def get(self, request, id):
        unit = PojazdyModel.objects.get(id=id)
        if ADR.objects.filter(pojazd=unit).exists():
            bt_unit = ADR.objects.get(pojazd=unit)
            form = ADR_Form(instance=bt_unit)
        else:
            form = ADR_Form()
        ctx = {'unit': unit, 'form': form}
        return render(request, 'addadr.html', ctx)
    def post(self,request, id):
        unit = PojazdyModel.objects.get(id=id)
        form = ADR_Form(request.POST)
        if form.is_valid():
            if ADR.objects.filter(pojazd=unit).exists():
                record = ADR.objects.update(nazwa="Dopuszczenie do przewodu ADR",
                                           instytucja=form.cleaned_data['instytucja'],
                                           wymagane=form.cleaned_data['wymagane'],
                                           data_konc=form.cleaned_data['data_konc'],
                                           pojazd=unit)
                return redirect(f'/details/{id}')
            else:
                f = ADR(**form.cleaned_data)
                f.nazwa = "Dopuszczenie do przewodu ADR"
                f.pojazd = unit
                f.save()
            return redirect(f'/details/{id}')
        else:
            return redirect('wrong/')
class AddUdtView(LoginRequiredMixin, View):
    def get(self, request, id):
        unit = PojazdyModel.objects.get(id=id)
        if UDT.objects.filter(pojazd=unit).exists():
            bt_unit = UDT.objects.get(pojazd=unit)
            form = UDT_Form(instance=bt_unit)
        else:
            form = UDT_Form()
        ctx = {'unit': unit, 'form': form}
        return render(request, 'addudt.html', ctx)
    def post(self,request, id):
        unit = PojazdyModel.objects.get(id=id)
        form = UDT_Form(request.POST)
        if form.is_valid():
            if UDT.objects.filter(pojazd=unit).exists():
                record = UDT.objects.update(nazwa="Badanie dopuszczenia windy hydraulicznej lub HDS",
                                           instytucja=form.cleaned_data['instytucja'],
                                           wymagane=form.cleaned_data['wymagane'],
                                           data_konc=form.cleaned_data['data_konc'],
                                           pojazd=unit)
                return redirect(f'/details/{id}')
            else:
                f = UDT(**form.cleaned_data)
                f.nazwa = "Badanie dopuszczenia windy hydraulicznej lub HDS"
                f.pojazd = unit
                f.save()
                return redirect(f'/details/{id}')
        else:
            return redirect('wrong/')

class AddTdtView(LoginRequiredMixin, View):
    def get(self, request, id):
        unit = PojazdyModel.objects.get(id=id)
        if TDT.objects.filter(pojazd=unit).exists():
            bt_unit = TDT.objects.get(pojazd=unit)
            form = TDT_Form(instance=bt_unit)
        else:
            form = TDT_Form()
        ctx = {'unit': unit, 'form': form}
        return render(request, 'addudt.html', ctx)
    def post(self,request, id):
        unit = PojazdyModel.objects.get(id=id)
        form = TDT_Form(request.POST)
        if form.is_valid():
            if TDT.objects.filter(pojazd=unit).exists():
                record = TDT.objects.update(nazwa="Badania elementów podlegających pod TDT",
                                           instytucja=form.cleaned_data['instytucja'],
                                           wymagane=form.cleaned_data['wymagane'],
                                           data_konc=form.cleaned_data['data_konc'],
                                           pojazd=unit)
                return redirect(f'/details/{id}')
            else:
                f = TDT(**form.cleaned_data)
                f.nazwa = "Badania elementów podlegających pod TDT"
                f.pojazd = unit
                f.save()
                return redirect(f'/details/{id}')
        else:
            return redirect('wrong/')
class AddEuroView(LoginRequiredMixin, View):
    def get(self, request, id):
        unit = PojazdyModel.objects.get(id=id)
        if NormaCzystosciSpalin.objects.filter(pojazd=unit).exists():
            bt_unit = NormaCzystosciSpalin.objects.get(pojazd=unit)
            form = EURO_Form(instance=bt_unit)
        else:
            form = EURO_Form()
        ctx = {'unit': unit, 'form': form}
        return render(request, 'addeuro.html', ctx)
    def post(self,request, id):
        unit = PojazdyModel.objects.get(id=id)
        form = EURO_Form(request.POST)
        if form.is_valid():
            if NormaCzystosciSpalin.objects.filter(pojazd=unit).exists():
                bt_unit = NormaCzystosciSpalin.objects.get(pojazd=unit)
                bt_unit.norma=form.cleaned_data['norma']
                bt_unit.wymagane=form.cleaned_data['wymagane']
                bt_unit.save()
            else:
                bt_unit = NormaCzystosciSpalin(**form.cleaned_data)
                bt_unit.pojazd = unit
                bt_unit.save()
            return redirect(f'/details/{id}')
        else:
            info = 'Niepoprawne dane !'
            return redirect('wrong/')
class AddUkView(LoginRequiredMixin, View):
   def get(self, request, id):
        unit = PojazdyModel.objects.get(id=id)
        form = UK_Form()
        if UKO.objects.filter(pojazd=unit).exists():
            bt_unit = UKO.objects.get(pojazd=unit)
            form = UK_Form(instance=bt_unit)
        ctx = {'unit': unit, 'form': form}
        return render(request, 'adduk.html', ctx)
   def post(self,request, id):
       unit = PojazdyModel.objects.get(id=id)
       form = UK_Form(request.POST)
       if form.is_valid():
           if UKO.objects.filter(pojazd=unit).exists():
               record = UKO.objects.update(
                                           instytucja=form.cleaned_data['instytucja'],
                                           data_konc=form.cleaned_data['data_konc'],
                                           OC=form.cleaned_data['OC'],
                                           AC=form.cleaned_data['AC'],
                                           NNW=form.cleaned_data['NNW'],
                                           nr_polisy=form.cleaned_data['nr_polisy'],
                                           pojazd=unit)
               return redirect(f'/details/{id}')
           else:
               f = UKO(**form.cleaned_data)
               f.pojazd = unit
               f.save()
               return redirect(f'/details/{id}')
       else:
           return redirect('wrong/')
class AddFrcView(LoginRequiredMixin, View):
    def get(self, request, id):
        unit = PojazdyModel.objects.get(id=id)
        if FRC.objects.filter(pojazd=unit).exists():
            bt_unit = FRC.objects.get(pojazd=unit)
            form = FRC_Form(instance=bt_unit)
        else:
            form = FRC_Form()
        ctx = {'unit': unit, 'form': form}
        return render(request, 'addfrc.html', ctx)
    def post(self,request, id):
        unit = PojazdyModel.objects.get(id=id)
        form = FRC_Form(request.POST)
        if form.is_valid():
            if FRC.objects.filter(pojazd=unit).exists():
                record = FRC.objects.update(nazwa="Certyfikat FRC",
                                           instytucja=form.cleaned_data['instytucja'],
                                           wymagane=form.cleaned_data['wymagane'],
                                           data_konc=form.cleaned_data['data_konc'],
                                           pojazd=unit)
            else:
                f = FRC(**form.cleaned_data)
                f.nazwa = "Certyfikat FRC"
                f.pojazd = unit
                f.save()
            return redirect(f'/details/{id}')
        else:
            return redirect('wrong/')
class BookShowView(LoginRequiredMixin, View):
    def get(self, request):
        form = BridgeForm()
        return render(request, 'bridge_book.html', {'form': form})
    def post(self, request):
        form = BridgeForm(request.POST)
        if form.is_valid():
            if PojazdyModel.objects.filter(id=form.cleaned_data['nr']).exists():
                object = PojazdyModel.objects.get(id=form.cleaned_data['nr'])
                return redirect(f'/details/{object.id}')
            else:
                info = 'Brak pojazdu o takim ID'
                return render(request, 'bridge_book.html', {'form': form, 'info': info})
        else:
            return redirect('wrong/')
class BridgeDateView(LoginRequiredMixin, View):
    def get(self, request):
        form = BridgeDateForm()
        return render(request, 'dedline_bridge.html', {'form': form})
    def post(self, request):
        form = BridgeDateForm(request.POST)
        if form.is_valid():
            date2 = form.cleaned_data['date2']
            return redirect(f'/dedlinevehicle/{date2}')
        else:
            info = "Nieprawidłowe dane"
            return render(request, 'dedline_bridge.html', {'form': form, 'info': info})

class DedlineVehicleView(LoginRequiredMixin, View):
    def get(self, request, date_string):
        dedline = datetime.strptime(date_string, "%Y-%m-%d")
        dedline = datetime.date(dedline)
        pojazdy = PojazdyModel.objects.filter(
            Q(przegladtech__data_konc__lte=dedline)|
            Q(przegladtacho__data_konc__lte=dedline)|
            Q(przegladadr__data_konc__lte=dedline)|
            Q(przegladtdt__data_konc__lte=dedline)|
            Q(przegladudt__data_konc__lte=dedline)|
            Q(komunikacyjne__data_konc__lte=dedline)|
            Q(przegladfrc__data_konc__lt=dedline)
        )
        note = f"(Pojazdy z końcem terminu). Liczba pojazdów ze zbliżającym się terminem: {len(pojazdy)}"
        return render(request, 'show_all.html', {'pojazdy': pojazdy, 'note': note})

class HelpView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'help.html', {})

class AboutView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'about.html', {})

class WrongDataView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'bad_data.html', {})
