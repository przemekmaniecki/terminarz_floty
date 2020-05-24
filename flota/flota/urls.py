"""flota URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#import form Pojazdy app:
from django.contrib import admin
from django.urls import path, re_path
from Pojazdy.views import AddVehicleView, ShowVehicleView, DeleteVehicleView, DedlineVehicleView, \
    HelpView, AboutView, WrongDataView
from Pojazdy.views import SearchVehicleView, EditVehicleView, BridgeEditView, BridgeDelView
from Pojazdy.views import VehicleDetailsView, AddBtView, AddTachoView, AddAdrVehView
from Pojazdy.views import AddUdtView, AddTdtView, AddEuroView, AddUkView, AddFrcView
from Pojazdy.views import BookShowView, BridgeDateView
#import from Kierowcy app:
from Kierowcy.views import AddDriverView, EditDriverView, AddPjView, EditDriverBridgeView, AddKwView, DedlinePersonView, \
    SearchPersonView
from Kierowcy.views import ShowDriversView, BookOfDriverView, AddAdrView,  DeleteDriverView, DelDriverBridgeView
from Kierowcy.views import DetailsDriverBridgeView, BridgeDatePersonView
from system.views import StartView, LoginView, LogoutView, AlphaView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', StartView.as_view(), name="index"),
    path('login/', LoginView.as_view(), name="log-in"),
    path('login/start/', AlphaView.as_view(), name="front-site"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('add_vehicle/', AddVehicleView.as_view(), name="add-vehicle"),
    path('wykaz_pojazdow/<int:select>/', ShowVehicleView.as_view(), name="list-of-vehicle"),
    path('delete/<int:id>/', DeleteVehicleView.as_view(), name="delete-vehicle"),
    path('search/', SearchVehicleView.as_view(), name="search-vehicle"),
    path('searchperson/', SearchPersonView.as_view(), name="search-person"),
    path('edit/<str:nr>/', EditVehicleView.as_view(), name="edit-view"),
    path('edit/', BridgeEditView.as_view(), name="edit"),
    path('del/', BridgeDelView.as_view(), name="del"),
    path('details/<int:id>/', VehicleDetailsView.as_view(), name="vehicle-details"),
    path('addbt/<int:id>/', AddBtView.as_view(), name="add-bt"),
    path('addtacho/<int:id>', AddTachoView.as_view(), name="add-tacho"),
    path('addadr/<int:id>', AddAdrVehView.as_view(), name="add-adr"),
    path('addudt/<int:id>', AddUdtView.as_view(), name="add-udt"),
    path('addtdt/<int:id>', AddTdtView.as_view(), name="add-tdt"),
    path('addeuro/<int:id>', AddEuroView.as_view(), name="add-euro"),
    path('adduk/<int:id>', AddUkView.as_view(), name="add-uk"),
    path('addfrc/<int:id>', AddFrcView.as_view(), name="add-frc"),
    path('details/', BookShowView.as_view(), name="book-show"),
    path('adddriver/', AddDriverView.as_view(), name="add-driver"),
    path('editdriver/<int:id>', EditDriverView.as_view(), name="edit-driver"),
    path('editdriver/', EditDriverBridgeView.as_view(), name="edit-driver-2"),
    path('drivers/', ShowDriversView.as_view(), name="drivers-all"),
    path('detailsofdriver/<int:id>', BookOfDriverView.as_view(), name="driver-detail"),
    path('prawojazdyedit/<int:id>', AddPjView.as_view(), name="add-pj"),
    path('kwalifikacjaedit/<int:id>', AddKwView.as_view(), name="add-kw"),
    path('adrdriveredit/<int:id>', AddAdrView.as_view(), name="add-adr-driver"),
    path('wrong/', WrongDataView.as_view(), name="bad-data-in-form"),
    path('deletedriver/<int:id>', DeleteDriverView.as_view(), name="delete-driver"),
    path('deletedriver/', DelDriverBridgeView.as_view(), name="del-bridge-driver"),
    path('detailsofdriver/', DetailsDriverBridgeView.as_view(), name="detail-driver-bridge"),
    path('dedlineveh/', BridgeDateView.as_view(), name="dedline-veh-bridge"),
    re_path(r'^dedlinevehicle/(?P<date_string>\d{4}-\d{2}-\d{2})', DedlineVehicleView.as_view(),name="dedline-veh"),
    path('dedlineperson/', BridgeDatePersonView.as_view(), name="dedline-person-bridge"),
    re_path(r'^dedlineperson/(?P<date_string>\d{4}-\d{2}-\d{2})', DedlinePersonView.as_view(), name="dedline-person"),
    path('help/', HelpView.as_view(), name="help-view"),
    path('about/', AboutView.as_view(), name="about-view"),
]
