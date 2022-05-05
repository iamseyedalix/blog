from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from users.models import UserProfile
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['view_username','first_name', 'last_name','age', 'phone_number']
    @admin.display(empty_value='???')
    def view_username(self, obj):
        return obj.user.username

admin.site.register(UserProfile, UserProfileAdmin)
