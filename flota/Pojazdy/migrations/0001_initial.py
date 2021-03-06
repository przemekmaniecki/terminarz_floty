# Generated by Django 2.2.11 on 2020-05-17 11:05

import Pojazdy.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PojazdyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rodzaj', models.CharField(choices=[('ciągnik siodłowy', 'ciągnik siodłowy'), ('samochód ciężarowy firana', 'samochód ciężarowy firana'), ('samochód ciężarowy wywrotka 3-4 osie.', 'samochód ciężarowy wywrotka 3-4 osie'), ('samochód ciężarowy tandem', 'samochód ciężarowy tandem'), ('przyczepa 2 osie', 'przyczepa 2 osie'), ('przyczepa tandem firana', 'przyczepa tandem firana'), ('naczepa firana', 'naczepa firana'), ('naczepa firana low deck', 'naczepa firana low deck'), ('naczepa plandeka burty', 'naczepa plandeka burty'), ('naczepa platforma', 'naczepa platforma'), ('naczepa szkielet.kontener BDF', 'naczepa szkielet.kontener BDF'), ('naczepa samowyładowcza walking-floor', 'naczepa samowyładowcza walking-floor'), ('naczepa wywrotka', 'naczepa wywrotka'), ('naczepa silos', 'naczepa silos'), ('naczepa cysterna ciecz', 'naczepa cysterna ciecz'), ('naczepa cysterna gaz', 'naczepa cysterna gaz'), ('naczepa cysterna paszowóz', 'naczepa cysterna paszowóz'), ('naczepa laweta niskopodwoz.', 'naczepa laweta niskopodwoz.'), ('naczepa chłodnia', 'naczepa chłodnia'), ('naczepa izoterma', 'naczepa izoterma')], max_length=64)),
                ('marka', models.CharField(choices=[('DAF', 'DAF'), ('MAN', 'MAN'), ('VOLVO', 'VOLVO'), ('SCANIA', 'SCANIA'), ('IVECO', 'IVECO'), ('RENAULT', 'RENAULT'), ('MERCEDES', 'MERCEDES'), ('Krone', 'Krone'), ('Schwartzmüller', 'Schwartzmüller'), ('Schmitz', 'Schmitz'), ('Wielton', 'Wielton'), ('Mega', 'Mega'), ('Kassbohrer', 'Kassbohrer'), ('Kögel', 'Kögel'), ('inne', 'inne')], max_length=16)),
                ('model', models.CharField(blank=True, max_length=32)),
                ('VIN', models.CharField(max_length=17, unique=True, validators=[Pojazdy.models.VIN_walidator])),
                ('nr_rej', models.CharField(max_length=8, unique=True, validators=[Pojazdy.models.REJ_walidator], verbose_name='nr rej.')),
                ('rok_prod', models.PositiveSmallIntegerField(choices=[(2021, '2021'), (2020, '2020'), (2019, '2019'), (2018, '2018'), (2017, '2017'), (2016, '2016'), (2015, '2015'), (2014, '2014'), (2013, '2013'), (2012, '2012'), (2011, '2011'), (2010, '2010'), (2009, '2009'), (2008, '2008'), (2007, '2007'), (2006, '2006'), (2005, '2005'), (2004, '2004'), (2003, '2003'), (2002, '2002'), (2001, '2001'), (2000, '2000'), (1999, '1999'), (1998, '1998'), (1997, '1997'), (1996, '1996'), (1995, '1995'), (1994, '1994'), (1993, '1993'), (1992, '1992'), (1991, '1991'), (1990, '1990'), (1989, '1989'), (1988, '1988'), (1987, '1987'), (1986, '1986'), (1985, '1985'), (1984, '1984'), (1983, '1983'), (1982, '1982')], verbose_name='rok produkcji')),
            ],
        ),
        migrations.CreateModel(
            name='ADR',
            fields=[
                ('nazwa', models.CharField(default='Dopuszczenie do przewodu ADR', max_length=32)),
                ('instytucja', models.CharField(default='TDT', max_length=40)),
                ('wymagane', models.BooleanField(default=False)),
                ('data_konc', models.DateField(blank=True, null=True)),
                ('pojazd', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='przegladadr', serialize=False, to='Pojazdy.PojazdyModel')),
            ],
        ),
        migrations.CreateModel(
            name='BT',
            fields=[
                ('nazwa', models.CharField(default='Przegląd techniczy pojazdu', max_length=32)),
                ('instytucja', models.CharField(default='Okręgowa Stacja Kontroli Pojazdów', max_length=40, null=True)),
                ('wymagane', models.BooleanField(default=True)),
                ('data_konc', models.DateField(null=True)),
                ('pojazd', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='przegladtech', serialize=False, to='Pojazdy.PojazdyModel')),
            ],
        ),
        migrations.CreateModel(
            name='FRC',
            fields=[
                ('nazwa', models.CharField(default='Badanie termiczne chłodni ATP/FRC', max_length=32)),
                ('instytucja', models.CharField(default='Politechnika Poznańska, IMRiPS', max_length=40)),
                ('wymagane', models.BooleanField(default=False)),
                ('data_konc', models.DateField(blank=True, null=True)),
                ('pojazd', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='przegladfrc', serialize=False, to='Pojazdy.PojazdyModel')),
            ],
        ),
        migrations.CreateModel(
            name='NormaCzystosciSpalin',
            fields=[
                ('norma', models.CharField(choices=[('Euro 7', 'Euro 7'), ('Euro 6', 'Euro 6'), ('Euro 5', 'Euro 5'), ('Euro 4', 'Euro 4'), ('Euro 3', 'Euro 3'), ('Euro 2', 'Euro 2'), ('Euro 1', 'Euro 1'), ('Euro 0', 'Euro 0'), ('N49', 'N49'), ('nie dotyczy', 'nie dotyczy')], default='nie dotyczy', max_length=12, null=True)),
                ('wymagane', models.BooleanField(default=False)),
                ('pojazd', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='normaeuro', serialize=False, to='Pojazdy.PojazdyModel')),
            ],
        ),
        migrations.CreateModel(
            name='TDT',
            fields=[
                ('nazwa', models.CharField(default='Dozór zbiorników', max_length=64)),
                ('instytucja', models.CharField(default='Transportowy Dozór Techniczny', max_length=40)),
                ('wymagane', models.BooleanField(default=False)),
                ('data_konc', models.DateField(blank=True, null=True)),
                ('pojazd', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='przegladtdt', serialize=False, to='Pojazdy.PojazdyModel')),
            ],
        ),
        migrations.CreateModel(
            name='UDT',
            fields=[
                ('nazwa', models.CharField(default='Badanie dopuszczenia windy hydraulicznej lub HDS', max_length=60)),
                ('instytucja', models.CharField(default='Urząd Dozoru Techniczego', max_length=40)),
                ('wymagane', models.BooleanField(default=False)),
                ('data_konc', models.DateField(blank=True, null=True)),
                ('pojazd', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='przegladudt', serialize=False, to='Pojazdy.PojazdyModel')),
            ],
        ),
        migrations.CreateModel(
            name='UKO',
            fields=[
                ('instytucja', models.CharField(default='Zakład Ubezpieczeń', max_length=72, null=True)),
                ('OC', models.BooleanField(default=True)),
                ('AC', models.BooleanField(default=False)),
                ('NNW', models.BooleanField(default=False)),
                ('data_konc', models.DateField(blank=True, null=True)),
                ('nr_polisy', models.CharField(max_length=32, null=True)),
                ('pojazd', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='komunikacyjne', serialize=False, to='Pojazdy.PojazdyModel')),
            ],
        ),
        migrations.CreateModel(
            name='tacho',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(default='Przegląd tachografu', max_length=60)),
                ('instytucja', models.CharField(default='Okręgowa Stacja Kontroli Pojazdów', max_length=40)),
                ('wymagane', models.BooleanField(default=False)),
                ('data_konc', models.DateField(blank=True, null=True)),
                ('pojazd', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='przegladtacho', to='Pojazdy.PojazdyModel')),
            ],
        ),
    ]
