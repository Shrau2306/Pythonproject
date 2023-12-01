from django.contrib import admin
from .models import Company,UserProfile,File,Folder

# Register your models here.
admin.site.register(Company)
admin.site.register(UserProfile)
admin.site.register(File)
admin.site.register(Folder)