from django.contrib import admin

from .models import (AddressOperation, Customer, CustomerContact, Engine,
                     EngineHours, EngineNumber, EngineNumberRepair, Repair,
                     RepairType, Еquipment)


class EngineAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'slug', 'cylinders')
    list_editable = ('title', 'cylinders')
    search_fields = ('title', 'cylinders')
    list_filter = ('cylinders',)
    empty_value_display = '-пусто-'


class RepairTypeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'slug')
    list_editable = ('title',)
    search_fields = ('title',)
    empty_value_display = '-пусто-'


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug')
    list_editable = ('name',)
    search_fields = ('name',)
    empty_value_display = '-пусто-'


class CustomerContactAdmin(admin.ModelAdmin):
    list_display = ('pk', 'last_name', 'name', 'surname',
                    'phone_number', 'customer')
    list_editable = ('last_name', 'name', 'surname',
                     'phone_number', 'customer')
    search_fields = ('last_name', 'name', 'surname')
    list_filter = ('customer',)
    empty_value_display = '-пусто-'


class AddressOperationAdmin(admin.ModelAdmin):
    list_display = ('pk', 'address', 'slug')
    list_editable = ('address',)
    search_fields = ('address',)
    empty_value_display = '-пусто-'


class ЕquipmentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'name_equipment', 'slug')
    list_editable = ('title', 'name_equipment')
    search_fields = ('title', 'name_equipment')
    list_filter = ('title',)
    empty_value_display = '-пусто-'


class EngineNumberAdmin(admin.ModelAdmin):
    list_display = ('pk', 'engine_number', 'engine', 'equipment',
                    'equipment_number', 'owner', 'address',
                    'start_date', 'slug')
    list_editable = ('engine_number', 'engine', 'equipment',
                     'equipment_number', 'owner', 'address',
                     'start_date')
    search_fields = ('engine_number', 'engine__title',
                     'equipment__name_equipment', 'equipment_number',
                     'owner__name', 'address__address',
                     'start_date')
    list_filter = ('engine', 'owner', 'equipment')
    empty_value_display = '-пусто-'


class EngineHoursAdmin(admin.ModelAdmin):
    list_display = ('pk', 'pub_date', 'engine_hours', 'engine_number')
    list_editable = ('engine_hours', 'engine_number')
    search_fields = ('engine_number__engine_number',)
    empty_value_display = '-пусто-'


class RepairAdmin(admin.ModelAdmin):
    list_display = ('pk', 'pub_date', 'repair_number',
                    'customer', 'customer_contacts',
                    'repair_type', 'address', 'author', 'description')
    list_editable = ('repair_number',
                     'customer', 'customer_contacts',
                     'repair_type', 'address', 'description')
    search_fields = ('repair_number', 'engine_numbers__engine_number',
                     'customer__name', 'customer_contacts__name',
                     'customer_contacts__last_name', 'description',
                     'repair_type__title', 'address__address',
                     'author__username')
    list_filter = ('engine_numbers', 'customer',
                   'repair_type', 'author')
    empty_value_display = '-пусто-'


class EngineNumberRepairAdmin(admin.ModelAdmin):
    list_display = ('pk', 'repair', 'engine_number',)
    list_editable = ('repair', 'engine_number',)
    search_fields = ('repair__repair_number', 'engine_number__engine_number',)
    list_filter = ('repair__repair_number', 'engine_number__engine_number',)
    empty_value_display = '-пусто-'


admin.site.register(Engine, EngineAdmin)
admin.site.register(RepairType, RepairTypeAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(CustomerContact, CustomerContactAdmin)
admin.site.register(AddressOperation, AddressOperationAdmin)
admin.site.register(Еquipment, ЕquipmentAdmin)
admin.site.register(EngineNumber, EngineNumberAdmin)
admin.site.register(EngineHours, EngineHoursAdmin)
admin.site.register(Repair, RepairAdmin)
admin.site.register(EngineNumberRepair, EngineNumberRepairAdmin)
