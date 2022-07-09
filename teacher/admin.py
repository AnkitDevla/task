from django.contrib import admin
from .models import Teacher,Attendane
# from django_object_actions import DjangoObjectActions

admin.site.register(Teacher)
admin.site.register(Attendane)


# class ImportAdmin(DjangoObjectActions, admin.ModelAdmin):
#     def imports(modeladmin, request, queryset):
#         print("Imports button pushed")

#     changelist_actions = ('imports', )