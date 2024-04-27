from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager

# Create your models here.

class UserAccountManager(BaseUserManager):
   def create_user(self,username,email,password=None):
      email=self.normalize_email(email)
      user = self.model(username=username,email=email)
      user.set_password(password)
      user.save()
      return user

class User(AbstractUser):
   email=models.EmailField(unique=True)
   is_staff=models.BooleanField(default=False)
   is_active=models.BooleanField(default=True)
     
   objects=UserAccountManager()

   USERNAME_FIELD = 'email'
   REQUIRED_FIELDS =[]
   def __str__(self) :
      return self.email