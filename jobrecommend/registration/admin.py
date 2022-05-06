from django.contrib import admin
from .models import userregistration,userprofile,usercv
# Register your models here.
admin.site.register(userregistration)
admin.site.register(userprofile)
admin.site.register(usercv)