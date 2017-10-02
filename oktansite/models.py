"""
Django model file
"""

import os
import uuid
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from datetime import datetime

def get_upload_path_images_payment(instance, filename):
    """
        Function to get upload image payment proof dir path
    """
    upload_dir = "%s" % instance.team_name
    extension = os.path.splitext(filename)[1]
    filename = "payment_" + instance.team_name + extension
    return os.path.join(upload_dir, filename)

def get_upload_path_images_student_card(instance, filename):
    """
        Function to get upload image student card dir path
    """
    upload_dir = "%s" % instance.team_name
    extension = os.path.splitext(filename)[1]
    filename = "student_id_" + extension
    print(upload_dir)
    return os.path.join(upload_dir, filename)

def get_upload_path_images_student_card1(instance, filename):
    """
        Function to get upload image student card dir path
    """
    upload_dir = "%s" % instance.team_name
    extension = os.path.splitext(filename)[1]
    filename = "student_id_1" + extension
    print(upload_dir)
    return os.path.join(upload_dir, filename)

def get_upload_path_images_student_card2(instance, filename):
    """
        Function to get upload image student card dir path
    """
    upload_dir = "%s" % instance.team_name
    extension = os.path.splitext(filename)[1]
    filename = "student_id_2" + extension
    print(upload_dir)
    return os.path.join(upload_dir, filename)

def get_upload_path_images_sponsor(instance, filename):
    upload_dir = "sponsor"
    extension = os.path.splitext(filename)[1]
    filename = "sponsor"+extension
    return os.path.join(upload_dir, filename)

def get_upload_path_image_sponsor(instance, filename):
    upload_dir = "sponsor"
    extension = os.path.splitext(filename)[1]
    filename = "sponsor"+extension
    return os.path.join(upload_dir, filename)

def get_upload_path_images_gallery(instance, filename):
    """
        Function to get upload image gallery dir path
    """
    upload_dir = "gallery"
    return os.path.join(upload_dir, filename)

def get_upload_path_images_media_partner(instance, filename):
    """
        Function to get upload image gallery dir path
    """
    upload_dir = "mediaPartner"
    extension = os.path.splitext(filename)[1]
    filename = "mediaPartner"+extension
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
    supervisor_name = models.CharField(max_length=100, null=False)
    school_name = models.CharField(max_length=150, null=False)
    proof_of_payment = models.FileField(upload_to=get_upload_path_images_payment)
    student_name_1 = models.CharField(max_length=100, null=True)
    student_phone_number_1 = models.CharField(max_length=50, null=True)
    student_id_number_1 = models.CharField(max_length=100, null=True)
    student_card_image_1 = models.ImageField(upload_to=get_upload_path_images_student_card1, null=True)
    student_name_2 = models.CharField(max_length=100, null=True)
    student_phone_number_2 = models.CharField(max_length=50, null=True)
    student_id_number_2 = models.CharField(max_length=100, null=True)
    student_card_image_2 = models.ImageField(upload_to=get_upload_path_images_student_card2, null=True)
    def __str__(self):
        return self.team_name

    def save(self, *args,**kwargs):
        self.validate_unique()
        try:
            this = Team.objects.get(id=self.id)
            if this.proof_of_payment != self.proof_of_payment:
                this.proof_of_payment.delete(save=False)
            if this.student_card_image_2 != self.student_card_image_2:
                this.student_card_image_2.delete(save=False)
            if this.student_card_image_1 != self.student_card_image_1:
                this.student_card_image_1.delete(save=False)
        except: pass # when new photo then we do nothing, normal case
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

class PhotoGallery(models.Model):
    id = models.AutoField(primary_key=True)
    src = models.ImageField(upload_to=get_upload_path_images_gallery)
    def __str__(self):
        return self.src

    def save(self, *args,**kwargs):
        try:
            this = PhotoGallery.objects.get(id=self.id)
            if this.src != self.src:
                this.src.delete(save=False)
        except: pass # when new photo then we do nothing, normal case
        super(PhotoGallery,self).save(*args, **kwargs)

class News(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=120)
    text = models.TextField()
    pub_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.id

class About(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField()

class Timeline(models.Model):
    id = models.AutoField(primary_key=True)
    tanggal = models.CharField(max_length=120)
    text = models.TextField()

class Sponsor(models.Model):
    id = models.AutoField(primary_key=True)
    src = models.ImageField(upload_to=get_upload_path_images_sponsor)
    def __str__(self):
        return self.id

    def save(self, *args,**kwargs):
        try:
            this = Sponsor.objects.get(id=self.id)
            if this.src != self.src:
                this.src.delete(save=False)
        except: pass # when new photo then we do nothing, normal case
        super(Sponsor,self).save(*args, **kwargs)

class MediaPartner(models.Model):
    id = models.AutoField(primary_key=True)
    src = models.ImageField(upload_to=get_upload_path_images_media_partner)
    def __str__(self):
        return self.src

    def save(self, *args,**kwargs):
        try:
            this = MediaPartner.objects.get(id=self.id)
            if this.src != self.src:
                this.src.delete(save=False)
        except: pass # when new photo then we do nothing, normal case
        super(MediaPartner,self).save(*args, **kwargs)
