from django.contrib.auth.base_user import BaseUserManager
import random
from django.core.mail import send_mail

def code():
    random.seed()
    return random.randint(1000,9999)

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, username):
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        username = self.username
        user = self.model(email=email, username=username, reg_key=code())
        user.set_password(password)

        user.save()
        send_mail(code(), 'Here is the message.', 'site16032021@rambler.ru',
                ['spinoza33@yandex.ru'], fail_silently=False)
        return user
