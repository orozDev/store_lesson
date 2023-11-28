from django.conf import settings
from django.core.mail import send_mail

from account.models import UserResetPassword


class ResetPasswordManager:

    def __init__(self, user):
        self.user = user
        self.reset_password = UserResetPassword.objects.get_or_create(user=self.user)[0]

    def send_key(self):
        key = self.reset_password.key

        subject, to, from_email = 'Reset Password | Oroz.kg', self.user.email, settings.EMAIL_HOST_USER
        message = f'this is a  <a href="">link</a> to reset password'

        send_mail(
            subject,
            message,
            from_email,
            [to],
        )