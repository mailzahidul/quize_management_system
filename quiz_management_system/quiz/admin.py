from django.contrib import admin
from .models import Quiz, Course, Semester, Department


admin.site.register(Quiz)
admin.site.register(Course)
admin.site.register(Semester)
admin.site.register(Department)

# Register your models here.
