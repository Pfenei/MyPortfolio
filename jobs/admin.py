from django.contrib import admin
from .models import Job, Technology, Study, Framework, Course

# Register your models here.
admin.site.register(Job)
admin.site.register(Technology)
admin.site.register(Study)
admin.site.register(Framework)
admin.site.register(Course)