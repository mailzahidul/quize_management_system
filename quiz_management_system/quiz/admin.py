from django.contrib import admin
from .models import Quiz, Course, Semester, Department, Result


admin.site.register(Quiz)
admin.site.register(Course)
admin.site.register(Semester)
admin.site.register(Department)
admin.site.register(Result)

# Register your models here.
