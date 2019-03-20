from __future__ import unicode_literals

import os
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

from accounts.storage import OverwriteStorage, profile_picture_name


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    user_email = models.CharField(max_length=250)
    picture = models.ImageField(upload_to=profile_picture_name, storage=OverwriteStorage(), blank=True)
    # Record Tracking
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="profile_created_by")
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="profile_modified_by")
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    # User Roles
    # is_admin = models.BooleanField(default=0)
    # is_member = models.BooleanField(default=0)
    class Meta:
        verbose_name = 'UserProfile'
        verbose_name_plural = 'UserProfiles'

    # override the unicode method to return the username on this model
    def __unicode__(self):
        return self.user.username
    
    def __str__(self):
        return self.user.username

    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(
                user=instance, user_email=instance.username)
    post_save.connect(create_user_profile, sender=User)

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])


class UserRole(models.Model):
	'''
	User Role Master Table
	'''
	role_name = models.CharField(max_length=100)
	created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_by')
	modified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='modified_by')
	created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
	modified_date = models.DateTimeField(auto_now=True, blank=True, null=True)

	class Meta:
		verbose_name = 'UserRole'
		verbose_name_plural = 'UserRoles'

    # override the unicode method to return the username on this model
	def __str__(self):
		return self.role_name