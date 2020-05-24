from django.contrib import admin
from .models import PojazdyModel, BT, ADR, NormaCzystosciSpalin, FRC, UDT, TDT
# Register your models here.

@admin.register(PojazdyModel)
class PojazdyModel(admin.ModelAdmin):
    pass

@admin.register(BT)
class BT(admin.ModelAdmin):
    pass
@admin.register(ADR)
class ADR(admin.ModelAdmin):
    pass
@admin.register(NormaCzystosciSpalin)
class NormaCzystosciSpalin(admin.ModelAdmin):
    pass
@admin.register(FRC)
class FRC(admin.ModelAdmin):
    pass
@admin.register(UDT)
class UDT(admin.ModelAdmin):
    pass
@admin.register(TDT)
class TDT(admin.ModelAdmin):
    pass
# @admin.register(UK)
# class UK(admin.ModelAdmin):
#     pass
