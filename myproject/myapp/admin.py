from django.contrib import admin
from .models import Student, Lecturer, Exam, Subject, Chair

admin.site.register(Student)
admin.site.register(Lecturer)
admin.site.register(Exam)
admin.site.register(Subject)
admin.site.register(Chair)


#@admin.register(Student)
#class StudentAdmin(admin.ModelAdmin):
#    list_display = ('name', 'date_of_birth', 'email')
#   search_fields = ('name', 'email')
