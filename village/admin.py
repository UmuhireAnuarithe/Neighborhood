from django.contrib import admin
from .models import Profile,Business,Village,Events
# Register your models here.
admin.site.register(Events)
admin.site.register(Business)
admin.site.register(Village)
admin.site.register(Profile)