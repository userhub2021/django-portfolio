from django.contrib import admin
from .models import Concept, Education, Experience, Profile, Software, Technical, Work, Concept
# Register your models here.

admin.site.register(Profile)
admin.site.register(Work)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Software)
admin.site.register(Technical)
admin.site.register(Concept)