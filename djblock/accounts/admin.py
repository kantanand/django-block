from django.contrib import admin
from accounts.models import UserProfile, UserRole

class UserProfileAdmin(admin.ModelAdmin):
    # Code May Required in Future 
    # fieldsets = [
    #     ('UserProfile', {
    #         'fields': [
    #             'user',
    #             'user_name',
    #             'user_email',
    #             'picture',
    #             'created_by',
    #             'modified_by'
    #         ]
    #     }),
    #     # ('Date Information', {
    #     #     'fields': [
    #     #         'created',
    #     #         'modified'
    #     #     ],
    #     #     'classes': ['collapse']
    #     # }),
    # ]
    list_display = ('user_name', 'user_email', 'picture')
    list_filter = ['user_name', 'user_email']
    search_fields = ['user_name', 'user_email']

# Register your models here.
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(UserRole)