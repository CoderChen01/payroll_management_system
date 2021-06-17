from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

# Register your models here.


admin.site.register(MAddress)
admin.site.register(MCompany)
admin.site.register(MDepartment)
admin.site.register(MEmployee)
admin.site.register(MGrade)
admin.site.register(MPay)
admin.site.register(MPaygrade)
admin.site.register(MState)
admin.site.register(TAchievement)
admin.site.register(TLeave)
