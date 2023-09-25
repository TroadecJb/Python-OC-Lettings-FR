from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator
import logging

class Address(models.Model):
    """
    Class to represent an address.

    Attributes
    ----------
    number : int
        number of the street for the address
    street : str
        street's name of the address
    city : str
        city's name of the address
    state : str
        state's of the address
    zip_code : int
        zip code of the address
    country_iso_code : str
        country iso code of the address
    """

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(
        max_length=3, validators=[MinLengthValidator(3)]
    )

    def __str__(self):
        return f"{self.number} {self.street}"

    class Meta:
        """
        Fix plural of "address" in the admin page.
        """

        verbose_name = "Address"
        verbose_name_plural = "Addresses"


class Letting(models.Model):
    """
    Class to represent a letting

    Attributes
    ----------
    title : str
        title of the letting
    address : int
        Foreign key of the letting's address id, from table lettings_address
    """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
