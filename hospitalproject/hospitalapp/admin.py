from django.contrib import admin

from hospitalapp.models import Departments, Doctors

# Register your models here.
admin.site.register(Departments)
admin.site.register(Doctors)