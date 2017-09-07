"""
Django model file
"""

import os
import uuid
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

def get_upload_path_images_payment(instance, filename):
    """
        Function to get upload image payment proof dir path
    """
    upload_dir = os.path.join('media', "%s" % instance.team_name)
    print(upload_dir)
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    return os.path.join(upload_dir, filename)

def get_upload_path_images_student_card(instance, filename):
    """
        Function to get upload image student card dir path
    """
    upload_dir = os.path.join('media', "%s" % instance.team.team_name)
    upload_dir = os.path.join(upload_dir, "%s" % instance.name)
    print(upload_dir)
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    return os.path.join(upload_dir, filename)

def get_upload_path_images_gallery(instance, filename):
    """
        Function to get upload image gallery dir path
    """
    upload_dir = os.path.join('media', 'gallery')
    print(upload_dir)
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    return os.path.join(upload_dir, filename)

# Create your models here.

class AccountManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            password=password
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, email_):
        return self.get(email=email_)

class Team(models.Model):
    """
        Team Model
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    team_name = models.CharField(max_length=50, null=False, unique=True)
    supervisor_name = models.CharField(max_length=50, null=False)
    school_name = models.CharField(max_length=150, null=False)
    proof_of_payment = models.FileField(upload_to=get_upload_path_images_payment)
    student_name_1 = models.CharField(max_length=50, null=True)
    student_phone_number_1 = models.CharField(max_length=50, null=True)
    student_id_card_1 = models.CharField(max_length=50, null=True)
    student_card_image_1 = models.FileField(upload_to=get_upload_path_images_student_card, null=True)
    student_name_2 = models.CharField(max_length=50, null=True)
    student_phone_number_2 = models.CharField(max_length=50, null=True)
    student_id_card_2 = models.CharField(max_length=50, null=True)
    student_card_image_2 = models.FileField(upload_to=get_upload_path_images_student_card, null=True)
    def __str__(self):
        return self.team_name

    def save(self, *args,**kwargs):
        self.validate_unique()
        super(Team,self).save(*args, **kwargs)

class Account(AbstractBaseUser):
    """
    Account model
    """
    password = models.CharField(max_length=50, null=False)
    email = models.EmailField(null=False, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    email_confirmed = models.BooleanField(default=False)
    objects = AccountManager()
    team = models.OneToOneField(Team, on_delete=models.CASCADE, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def natural_key(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_admin

    def save(self, *args,**kwargs):
        self.validate_unique()
        super(Account,self).save(*args, **kwargs)

class Gallery(models.Model):
    """
        Gallery model
    """
    image_file = models.FileField(upload_to=get_upload_path_images_gallery)
    def __str__(self):
        return self.image_file
