# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django import forms
from django.shortcuts import render, redirect

# Models we need
from .models import Part, StorageItem

# i18n (just in case)
from django.utils.translation import ugettext_lazy as _

# Logging
import logging
logger = logging.getLogger(__name__)


class MergeStorageItemsForm(forms.Form):
    storageitem1 = forms.ModelChoiceField(
        queryset=StorageItem.objects.all())


class StockTakingForm(forms.Form):
    amount = forms.DecimalField(
        label=_("Parts now inside storage"),
        max_digits=10,
        decimal_places=4,
        help_text=_("The amount of currently inside storage place."))
