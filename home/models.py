# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Properties(models.Model):

    #__Properties_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    address = models.TextField(max_length=255, null=True, blank=True)
    area = models.IntegerField(null=True, blank=True)
    active = models.BooleanField()
    activefrom = models.DateTimeField(blank=True, null=True, default=timezone.now)
    type = models.CharField(max_length=255, null=True, blank=True)
    owner 1 = models.CharField(max_length=255, null=True, blank=True)
    owner 2 = models.CharField(max_length=255, null=True, blank=True)
    owner 3 = models.CharField(max_length=255, null=True, blank=True)
    occupied = models.BooleanField()
    currentexpectedprice = models.IntegerField(null=True, blank=True)
    purchasedate = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Properties_FIELDS__END

    class Meta:
        verbose_name        = _("Properties")
        verbose_name_plural = _("Properties")


class Tenant(models.Model):

    #__Tenant_FIELDS__
    contactphone = models.IntegerField(null=True, blank=True)
    property = models.ForeignKey(properties, on_delete=models.CASCADE)
    moveindate = models.DateTimeField(blank=True, null=True, default=timezone.now)
    moveoutdate = models.DateTimeField(blank=True, null=True, default=timezone.now)
    active = models.BooleanField()
    contactemail = models.CharField(max_length=255, null=True, blank=True)
    type = models.CharField(max_length=255, null=True, blank=True)
    profession = models.CharField(max_length=255, null=True, blank=True)
    rent = models.IntegerField(null=True, blank=True)
    deposit = models.IntegerField(null=True, blank=True)

    #__Tenant_FIELDS__END

    class Meta:
        verbose_name        = _("Tenant")
        verbose_name_plural = _("Tenant")


class Agreements(models.Model):

    #__Agreements_FIELDS__
    tenant = models.ForeignKey(tenant, on_delete=models.CASCADE)
    property = models.ForeignKey(properties, on_delete=models.CASCADE)
    agreementdate = models.DateTimeField(blank=True, null=True, default=timezone.now)
    agreementterm = models.IntegerField(null=True, blank=True)
    startdate = models.DateTimeField(blank=True, null=True, default=timezone.now)
    enddate = models.DateTimeField(blank=True, null=True, default=timezone.now)
    agreementlawyer = models.CharField(max_length=255, null=True, blank=True)

    #__Agreements_FIELDS__END

    class Meta:
        verbose_name        = _("Agreements")
        verbose_name_plural = _("Agreements")


class Transactions(models.Model):

    #__Transactions_FIELDS__
    amount = models.IntegerField(null=True, blank=True)
    type = models.CharField(max_length=255, null=True, blank=True)
    category = models.CharField(max_length=255, null=True, blank=True)
    bankaccount = models.ForeignKey(bankAccounts, on_delete=models.CASCADE)
    modeofpayment = models.CharField(max_length=255, null=True, blank=True)

    #__Transactions_FIELDS__END

    class Meta:
        verbose_name        = _("Transactions")
        verbose_name_plural = _("Transactions")


class Bankaccounts(models.Model):

    #__Bankaccounts_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    accountnumber = models.CharField(max_length=255, null=True, blank=True)

    #__Bankaccounts_FIELDS__END

    class Meta:
        verbose_name        = _("Bankaccounts")
        verbose_name_plural = _("Bankaccounts")



#__MODELS__END
