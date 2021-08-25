from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.core.exceptions import ValidationError

class UserManager(BaseUserManager):
    def _create_user(self, username, name, surname, phone, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            username = username,
            name = name,
            surname = surname,
            phone = phone,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, name, surname, phone, password=None, **extra_fields):
        return self._create_user(username, name, surname, phone, password, True, False, **extra_fields)

    def create_superuser(self, username, name, surname, phone, password=None, **extra_fields):
        return self._create_user(username, name, surname, phone, password, True, True, **extra_fields)

def validate_phone(value):
    if not (len(value) == 9):
        raise ValidationError("El número debe tener 9 dígitos")

class User(AbstractBaseUser, PermissionsMixin):
    
    username = models.EmailField(max_length = 255, unique = True )
    name = models.CharField(max_length = 255, blank = True, null = True)
    surname = models.CharField(max_length = 255, blank = True, null = True)
    phone = models.CharField(max_length = 9, blank = True, null = True, validators=[validate_phone])
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name','surname', 'phone']

    def __str__(self):
        return f'{self.name} {self.surname}'

class Address(models.Model):
    address = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.address