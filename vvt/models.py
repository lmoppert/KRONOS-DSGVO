from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
from django.db import models


class PersonCategory(models.Model):
    name = models.CharField(
        max_length=50, verbose_name=_("Category of affected individuals"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Person Category")
        verbose_name_plural = _("Person Categories")


class DataCategory(models.Model):
    name = models.CharField(
        max_length=50, verbose_name=_("Categories of personal data"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Data Category")
        verbose_name_plural = _("Data Categories")


class RecipientCategory(models.Model):
    name = models.CharField(
        max_length=50, verbose_name=_("Categories of recipients"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Recipient Category")
        verbose_name_plural = _("Recipient Categories")


class Department(models.Model):
    name = models.CharField(max_length=50, verbose_name=_("Department"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Department")
        verbose_name_plural = _("Departments")



class Contact(models.Model):
    name = models.CharField(max_length=50, verbose_name=_("Contact"))
    email = models.CharField(max_length=50, verbose_name=_("Email"),
                             blank=True, )
    phone = models.CharField(max_length=50, verbose_name=_("Phone"), blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE,
                                   verbose_name=_("Department"))

    def __str__(self):
        return ("{} ({})".format(self.name, self.department))

    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")



class ProcessingActivity(models.Model):
    name = models.CharField(
        max_length=200, verbose_name=_("Processing Activity"))
    created = models.DateField(auto_now_add=True, verbose_name=_("Created on"))
    changed = models.DateField(auto_now=True, verbose_name=_("Changed on"))
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE,
                                   verbose_name=_("Department"))
    reason = models.TextField(verbose_name=_("Reason"))
    person_categories = models.ManyToManyField(
        PersonCategory, verbose_name=_("Categories of affected individuals"))
    data_categories = models.ManyToManyField(
        DataCategory, verbose_name=_("Categories of personal data"))
    recipient_categories = models.ManyToManyField(
        RecipientCategory, verbose_name=_("Categories of recipients"))
    transfer = models.TextField(verbose_name=_("Transfer to third countries"))
    transfer_warrant = models.TextField(verbose_name=_("Transfer warrant"))
    retention = models.CharField(
        max_length=200, verbose_name=_("Retention period"))
    processors = models.TextField(verbose_name=_("Order processors"))

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('pdf_view', args=[str(self.id)])

    class Meta:
        verbose_name = _("Processing Activity")
        verbose_name_plural = _("Processing Activities")
