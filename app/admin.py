from django.contrib import admin
from .models import Education, Experience, Profile, Work
# Register your models here.

admin.site.register(Profile)
admin.site.register(Work)
admin.site.register(Experience)
admin.site.register(Education)