from django.contrib import admin
from .models import Doctor,Designation,AvailableTime,Specialization
# Register your models here.

class DoctorAdminModel(admin.ModelAdmin):
    list_display=['first_name','last_name',]

    def first_name(self,obj):
        return obj.user.first_name

    def last_name(self,obj):
        return obj.user.last_name

class SpecializationAdminModel(admin.ModelAdmin):
    readonly_fields=('slug',)
    list_display=['name','slug']

class DesignationAdminModel(admin.ModelAdmin):
    readonly_fields=('slug',)
    list_display=['name','slug']

admin.site.register(Doctor,DoctorAdminModel)
admin.site.register(Designation,DesignationAdminModel)
admin.site.register(AvailableTime)
admin.site.register(Specialization,SpecializationAdminModel)