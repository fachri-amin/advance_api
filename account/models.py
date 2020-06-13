from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.

#! customize User Model


class MyAccountManager(BaseUserManager):
    ''' this class will manage when the new user registrated'''

    def create_user(self, email, username, password=None):
        ''' this method will handle when normal user registrating'''
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        ''' this method will handle when super user registrating'''
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        ''' look bellow all role will return to True when you registrating new super user'''
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    '''this is will be user model'''

    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    #! is_admin, is_active, is_staff and is_superuser is required field to create customize User model

    USERNAME_FIELD = 'email'
    ''' the login process required what USERNAME_FIELD value as a field
        in this case email will be requierd field to login
        i am not using username to login '''

    REQUIRED_FIELDS = ['username']
    ''' the registration new user must have password, USERNAME_FIELD and REUQUIRED_FIELDS
        if you need first_name when registration new user, just add the field name to REQUIRED FIELD as string'''

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True

    ''' just copy last has_perm and has_module_perms method
        you don't need to know for what , HAHAHA'''
