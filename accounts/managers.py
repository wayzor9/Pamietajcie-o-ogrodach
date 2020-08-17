from django.contrib.auth.models import BaseUserManager

# from .models import UserProfile


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):

        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        self.create_user_profile(user)
        return user

    def create_superuser(self, email, password, **extrafields):
        extrafields.setdefault("is_staff", True)
        extrafields.setdefault("is_superuser", True)
        extrafields.setdefault("is_active", True)
        return self.create_user(email, password, **extrafields)

    # def create_user_profile(self, user):
    #     return UserProfile.objects.get_or_create(user=user)
    # TODO: avoid recursion while creating user profile
