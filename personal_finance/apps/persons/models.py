from django.db.models import CharField, EmailField
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django_softdelete.models import SoftDeleteModel
from phonenumber_field.modelfields import PhoneNumberField
from django_address.fields import AddressField


class Person(SoftDeleteModel):
    ID_TYPE_ABBREVIATIONS = [
        ('CC', _("citizenship card")),
        ('BC', _("birth certificate")),
        ('ID', _("identity card")),
        ('PAS', _("passport")),
        ('FOID', _("foreigner's identity card")),
        ('DLIC', _("driver's license")),
    ]
    first_name = CharField(_("first name"), max_length=64)
    middle_name = CharField(_("middle name"), max_length=64, blank=True)
    last_name = CharField(_("last name"), max_length=64)
    second_last_name = CharField(
        _("second_last name"), max_length=64, blank=True)
    id_type = CharField(
        _("identification type"), max_length=4, choices=ID_TYPE_ABBREVIATIONS)
    identification = CharField(_("identification"), max_length=64)
    email = EmailField(_("email"), max_length=254, blank=True)
    phone = PhoneNumberField(_("phone"), blank=True)
    address = AddressField(verbose_name=_("address"))

    @property
    def full_name(self):
        return ' '.join([s for s in (
            self.first_name,
            self.middle_name,
            self.last_name,
            self.second_last_name
        ) if s])

    class Meta:
        verbose_name = _("person")
        verbose_name_plural = _("persons")

    def __str__(self):
        return f"{self.full_name}"

    def get_absolute_url(self):
        return reverse("person_detail", kwargs={"pk": self.pk})
