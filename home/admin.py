from django.contrib import admin
from .models import Contact,StudentProject,StudentProfile
from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(Contact)
class ContactDet(ImportExportModelAdmin):
    pass
@admin.register(StudentProject)
class StudentProjectDet(ImportExportModelAdmin):
    pass

@admin.register(StudentProfile)
class StudentProfileDet(ImportExportModelAdmin):
    pass