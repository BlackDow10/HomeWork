from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager

#Создаём модель с регистрицией по email и имени пользователя. 
class CustomUser(AbstractUser):
    username = models.CharField(max_length=14, unique=True)
    email = models.EmailField(unique=True)
    confirmed = models.BooleanField(default=False)
    reg_key = models.IntegerField(blank=True)
    


    USERNAME_FIELD = email
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()
    
    def __str__(self):
        return self.email