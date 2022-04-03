from django.contrib import admin
from account.models import Account
#from django.contrib.auth.admin import UserAdmin
# from django.contrib.admin import AdminSite

# class AppAdmin(AdminSite):
#     def index(self, request, extra_context=None):
#         # Update extra_context with new variables
#         return super().index(request, extra_context)

admin.site.register(Account)

# class AccountAdmin(UserAdmin):
#     list_display = ('email', 'username', 'date_joined', 'last_login', 'is_admin', 'is_staff')
#     search_fields = ('username', 'email')
#     readonly_fields = ('date_joined', 'last_login')

#     filter_horizontal = ()
#     list_filter = ()
#     fieldsets = ()



