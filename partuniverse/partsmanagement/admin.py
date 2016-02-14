# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import *

# Logging
import logging
logger = logging.getLogger(__name__)

admin.site.register(StorageType)
admin.site.register(Category)
admin.site.register(StoragePlace)
admin.site.register(Manufacturer)
admin.site.register(Distributor)
admin.site.register(Part)
admin.site.register(StorageItem)
admin.site.register(Transaction)
