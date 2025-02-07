from django.contrib import admin
from .models import BeerStyle

# Registrace modelu BeerStyle v administraci
@admin.register(BeerStyle)
class BeerStyleAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'number')
    search_fields = ('name', 'category', 'number')
    list_filter = ('category',)
    # Zobrazení vypočítaných hodnot pouze v detailním pohledu
    readonly_fields = ('ebcmin_display', 'ebcmax_display', 'brixmin_display', 'brixmax_display')


    # Přidání metod pro zobrazení vypočítaných hodnot v detailu
    def ebcmin_display(self, obj):
        return obj.ebcmin
    ebcmin_display.short_description = 'EBC Min'

    def ebcmax_display(self, obj):
        return obj.ebcmax
    ebcmax_display.short_description = 'EBC Max'

    def brixmin_display(self, obj):
        return obj.brixmin
    brixmin_display.short_description = 'Brix Min'

    def brixmax_display(self, obj):
        return obj.brixmax
    brixmax_display.short_description = 'Brix Max'