from django.contrib import admin
from vvt import models


@admin.register(models.DataCategory)
class DataCategoryAdmin(admin.ModelAdmin):
    model = models.DataCategory


@admin.register(models.PersonCategory)
class PersonCategoryAdmin(admin.ModelAdmin):
    model = models.PersonCategory


@admin.register(models.Department)
class DepartmentAdmin(admin.ModelAdmin):
    model = models.Department


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    model = models.Contact


@admin.register(models.RecipientCategory)
class RecipientCategoryAdmin(admin.ModelAdmin):
    model = models.RecipientCategory


@admin.register(models.ProcessingActivity)
class ProcessingActivityAdmin(admin.ModelAdmin):
    model = models.ProcessingActivity
    list_display = ('active', 'name', 'contact', 'reason', 'transfer',
                    'retention')
    list_display_links = ('name', )
    list_filter = ('active', 'transfer', 'contact__department__name')
    search_fields = ['name', 'contact__name', 'contact__departnment__name',
                     'reason', 'transfer__recipient', 'transfer_warrant',
                     'retention', 'processors']
    filter_horizontal = ('recipient_categories', )
    fieldsets = (
        (None, {'fields': (
            'name', 'active', 'contact', 'reason')}),
        ('Categories', {'fields': (
            'person_categories', 'data_categories', 'recipient_categories')}),
        ('Transfer', {'fields': (
            'transfer', 'transfer_recipient', 'transfer_warrant')}),
        ('Retention Period', {'fields': ('retention', )}),
        ('Order Processors', {'fields': ('processors', )}),

    )
