from django.contrib import admin

from .models import Engine, RepairType, Customer, CustomerContact, Repair


class EngineAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'slug', 'cylinders')
    list_editable = ('title', 'slug', 'cylinders')
    search_fields = ('title', 'slug', 'cylinders')
    list_filter = ('cylinders',)
    empty_value_display = '-пусто-'


class RepairTypeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'slug')
    list_editable = ('title', 'slug')
    search_fields = ('title',)
    empty_value_display = '-пусто-'


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug')
    list_editable = ('name', 'slug')
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


class RepairAdmin(admin.ModelAdmin):
    list_display = ('pk', 'repair_number', 'customer',
                    'repair_type', 'engine', 'engine_number',
                    'customer_contacts', 'author', 'description')
    list_editable = ('repair_number', 'engine_number', 'customer',
                     'customer_contacts', 'repair_type',
                     'engine', 'author', 'description')
    search_fields = ('repair_number', 'engine_number', 'customer__name',
                     'customer_contacts__name', 'author__username',
                     'customer_contacts__last_name', 'description',
                     'repair_type__title', 'engine__title')
    list_filter = ('engine_number', 'customer',
                   'repair_type', 'engine', 'author')
    empty_value_display = '-пусто-'


admin.site.register(Engine, EngineAdmin)
admin.site.register(RepairType, RepairTypeAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(CustomerContact, CustomerContactAdmin)
admin.site.register(Repair, RepairAdmin)
