from django.contrib import admin
from django.contrib.auth import get_user_model


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'username', 'facebook_id', 'first_name', 'last_name')


admin.site.register(get_user_model(), UserAdmin)
