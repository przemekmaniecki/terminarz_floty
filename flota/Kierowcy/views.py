from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views import View

from Pojazdy.forms import BridgeDateForm, SearchForm
from .forms import AddDriverForm, BridgeForm, AddPjForm, AddKwForm, AddAdrForm
from Kierowcy.models import *
from datetime import date, datetime

class AddDriverView(LoginRequiredMixin, View):
    def get(self, request):
        form = AddDriverForm()
        return render(request, 'add_driver.html', {'form':form})
    def post(self, request):
        global info
        form = AddDriverForm(request.POST)
        info = ''
        if form.is_valid():
            new = Kierowcy.objects.create(**form.cleaned_data)
            info = "Dodano nowego kierowcę do bazy danych"
        return render(request, 'add_vehicle.html', {'form': form, 'info': info})


class EditDriverView(LoginRequiredMixin, View):
    def get(self, request, id):
        if Kierowcy.objects.filter(id=id).exists():
            unit = Kierowcy.objects.get(id=id)
            form = AddDriverForm(instance=unit)
        else:
            form = AddDriverForm()
        return render(request, 'edit_driver.html', {'form': form})
    def post(self, request, id):
        unit = Kierowcy.objects.get(id=id)
        form = AddDriverForm(request.POST, instance=unit)
        if form.is_valid():
            form.save()
        return redirect(f'/detailsofdriver/{id}')

class EditDriverBridgeView(LoginRequiredMixin, View):
    def get(self, request):
        form = BridgeForm()
        return render(request, 'bridge_edit_driver.html', {'form':form})
    def post(self, request):
        form = BridgeForm(request.POST)
        if form.is_valid():
            object = Kierowcy.objects.filter(id=form.cleaned_data['id'])
            if object.exists():
                return redirect(f'/editdriver/{object[0].id}')
            else:
                info = 'Brak pojazdu o takim ID'
                return render(request, 'bridge_edit_driver.html', {'form': form, 'info': info})
        else:
            info = 'Niepoprawne dane'
            return render(request, 'bridge_edit_driver.html', {'form': form, 'info': info})

class ShowDriversView(LoginRequiredMixin, View):
    def get(self, request):
        drivers = Kierowcy.objects.all()
        note = f"Kierowców w bazie {len(drivers)}"
        return render(request, 'show_drivers.html', {'drivers': drivers, 'note': note})

class BookOfDriverView(LoginRequiredMixin, View):
    def get(self, request, id):
        driver = Kierowcy.objects.get(id=id)
        today = date.today()
        return render(request, 'bookdriver.html', {'driver': driver,
                                                   'today': today})

class AddPjView(LoginRequiredMixin, View):
    def get(self, request, id):
        unit = Kierowcy.objects.get(id=id)
        if PrawoJazdy.objects.filter(kierowca=unit).exists():
            bt_unit = PrawoJazdy.objects.get(kierowca=unit)
            form =AddPjForm(instance=bt_unit)
        else:
            form = AddPjForm()
        ctx = {'unit': unit, 'form': form}
        return render(request, 'editprawojazdy.html', ctx)
    def post(self,request, id):
        unit = Kierowcy.objects.get(id=id)
        form = AddPjForm(request.POST)
        if form.is_valid():
            record = PrawoJazdy(**form.cleaned_data)
            record.kierowca = unit
            record.save()
            return redirect(f'/detailsofdriver/{id}')

class AddKwView(LoginRequiredMixin, View):
    def get(self, request, id):
        unit = Kierowcy.objects.get(id=id)
        if Kwalifikacja.objects.filter(kierowca=unit).exists():
            bt_unit = Kwalifikacja.objects.get(kierowca=unit)
            form =AddKwForm(instance=bt_unit)
        else:
            form = AddKwForm()
        ctx = {'unit': unit, 'form': form}
        return render(request, 'kwalifikacja.html', ctx)
    def post(self,request, id):
        form = AddKwForm(request.POST)
        unit = Kierowcy.objects.get(id=id)
        if form.is_valid():
            record = Kwalifikacja(**form.cleaned_data)
            record.kierowca = unit
            record.save()
            return redirect(f'/detailsofdriver/{id}')


class AddAdrView(LoginRequiredMixin, View):
    def get(self, request, id):
        unit = Kierowcy.objects.get(id=id)
        if ADRdriver.objects.filter(kierowca=unit).exists():
            bt_unit = ADRdriver.objects.get(kierowca=unit)
            form = AddAdrForm(instance=bt_unit)
        else:
            form = AddAdrForm()
        ctx = {'unit': unit, 'form': form}
        return render(request, 'adrdriver.html', ctx)
    def post(self, request, id):
        unit = Kierowcy.objects.get(id=id)
        form = AddAdrForm(request.POST)
        if form.is_valid():
            record = ADRdriver(**form.cleaned_data)
            record.kierowca = unit
            record.save()
            return redirect(f'/detailsofdriver/{id}')

class DeleteDriverView(LoginRequiredMixin, View):
    def get(self, request, id):
        driver = Kierowcy.objects.get(id=id)
        driver.delete()
        return redirect('/drivers/')

class DelDriverBridgeView(LoginRequiredMixin, View):
    def get(self, request):
        form = BridgeForm()
        return render(request, 'bridge_del_driver.html', {'form': form})
    def post(self, request):
        form = BridgeForm(request.POST)
        if form.is_valid():
            id = form.cleaned_data['id']
            if Kierowcy.objects.filter(id=id).exists():
                return redirect(f'/deletedriver/{id}')
            else:
                info = "Brak kierowcy o podanym ID"
                return render(request, 'bridge_del_driver.html', {'form': form, 'info':info})

class DetailsDriverBridgeView(LoginRequiredMixin, View):
    def get(self, request):
        form = BridgeForm()
        return render(request, 'bridge_details_driver.html', {'form': form})
    def post(self, request):
        form = BridgeForm(request.POST)
        if form.is_valid():
            if Kierowcy.objects.filter(id=form.cleaned_data['id']).exists():
                object = Kierowcy.objects.get(id=form.cleaned_data['id'])
                return redirect(f'/detailsofdriver/{object.id}')
            else:
                info = 'Brak kierowcy o takim ID'
                return render(request, 'bridge_details_driver.html', {'form': form, 'info':info})

class BridgeDatePersonView(LoginRequiredMixin, View):
    def get(self, request):
        form = BridgeDateForm()
        return render(request, 'dedline_bridge.html', {'form': form})
    def post(self, request):
        form = BridgeDateForm(request.POST)
        if form.is_valid():
            date2 = form.cleaned_data['date2']
            return redirect(f'/dedlineperson/{date2}')
        else:
            info = "Nieprawidłowe dane"
            return render(request, 'dedline_bridge.html', {'form': form, 'info': info})


class DedlinePersonView(LoginRequiredMixin, View):
    def get(self, request, date_string):
        dedline = datetime.strptime(date_string, "%Y-%m-%d")
        dedline = datetime.date(dedline)
        drivers = Kierowcy.objects.filter(
                Q(prawojazdy__data_waznosci__lte=dedline)|
                Q(kwalifikacja__data_waznosci__lte=dedline)|
                Q(adr__data_waznosci__lte=dedline)
                )
        note = f"Kierowców z granicznymi terminami {len(drivers)}"
        return render(request, 'show_drivers.html', {'drivers': drivers, 'note': note})


class SearchPersonView(LoginRequiredMixin, View):
    def get(self, request):
        form = SearchForm(request.GET)
        form.is_valid()
        text = form.cleaned_data.get('text', '')
        result = Kierowcy.objects.filter(
            Q(imie__icontains=text)|
            Q(nazwisko__icontains=text))
        note = f"wyszukano {len(result)}"
        ctx ={
            'form': form,
            'drivers': result,
             'note': note,
             }
        return render(request, 'show_drivers.html', ctx)
