from django.contrib import admin
from vvt import models


@admin.register(models.ProcessingActivity)
class ProcessingActivityAdmin(admin.ModelAdmin):
    model = models.ProcessingActivity
    filter_horizontal = (
        # 'person_categories',
        # 'data_categories',
        'recipient_categories',
    )


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
