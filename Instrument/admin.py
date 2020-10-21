from django.contrib import admin

from .models import Section
from .models import Instrument

# Register your models here.
admin.site.register(Section)
admin.site.register(Instrument)
