from django.contrib import admin
from members.models import TeamMembers
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.admin import AdminSite

# # @admin.register(TeamMembers)
# class AppAdmin(AdminSite):
#     def index(self, request, extra_context=None):
#         # Update extra_context with new variables
#         return super().index(request, extra_context)

admin.site.register(TeamMembers)
