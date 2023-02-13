from django.contrib import admin
from .models import AdminUser, MessageAdmin

# Register your models here.
admin.site.register(AdminUser)
admin.site.register(MessageAdmin)
