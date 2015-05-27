from django.contrib import admin

from .models import Employee, Parameter, Employee_Para


class Employee_ParaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['employee','parameter','weightage','score']}),
        ('Month information', {'fields': ['pub_month'], 'classes': ['collapse']}),
    ]




admin.site.register(Employee)
admin.site.register(Parameter)
admin.site.register(Employee_Para, Employee_ParaAdmin)
# Register your models here.
