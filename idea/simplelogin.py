"""
@auto simplelogin.py - a Django authentication agent that doesn't
require passwords.

Terry N. Brown, Brown.TerryN@epa.gov, Tue Jan 31 09:27:19 2017
"""

from django.contrib.auth.models import User

class SimpleLogin(object):

    def authenticate(self, username=None, password=None, email=None):
        # NOTE: this won't be called if it doesn't accept password
        return self.user_by_username(
            username=username,
            email=email,
        )

    def get_user(self, user_id):
        return User.objects.get(id=user_id)

    def user_by_username(self, username=None, email=None):
        user = User.objects.get_or_create(
            defaults = {'email': email or ""},
            username=username,
        )[0]
        if user.is_staff or user.is_superuser:
            return None
        return user
