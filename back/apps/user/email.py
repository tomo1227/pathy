from logging import getLogger
from django.contrib.auth.tokens import default_token_generator
from django.conf import settings

from templated_mail.mail import BaseEmailMessage
from djoser import utils

logger = getLogger(__name__)
# ******************************************************************************
# 'view': <apps.user.email.ActivationEmail object at 0x7f2ba7cf3fa0>,
# 'user': <MyUser: tomo.soccer1227@gmail.com>,
# 'domain': 'localhost:8000',
# 'protocol': 'http',
# 'site_name': 'localhost:8000',
# 'username': 'tomomon1227',
# 'uid': 'NDY',
# 'token': 'bfsgy6-54a59f690ab5792a55e2b465967be546',
# 'url': 'api/v1/auth/users/activation/NDY/bfsgy6-54a59f690ab5792a55e2b465967be546'}
# ******************************************************************************


class EmailManager(BaseEmailMessage):
    def send(self, to, *args, **kwags):
        self.render()
        self.to = to
        self.cc = kwags.pop("cc", [])
        self.bcc = kwags.pop("bcc", [])
        self.reply_to = kwags.pop("reply_to", [])
        self.from_email = kwags.pop(
            "from_email", "pathy <" + settings.DEFAULT_FROM_EMAIL + ">"
        )
        super(BaseEmailMessage, self).send(*args, **kwags)


class ActivationEmail(EmailManager):
    template_name = "user/activation.html"

    def get_context_data(self):
        context = super().get_context_data()
        user = context.get("user")
        context["domain"] = "http://13.114.67.189:8080/"
        context["username"] = user.username
        context["uid"] = utils.encode_uid(user.pk)
        context["token"] = default_token_generator.make_token(user)
        context["url"] = settings.DJOSER["ACTIVATION_URL"].format(**context)
        logger.debug(context)
        return context


class ConfirmationEmail(EmailManager):
    template_name = "user/confirmation.html"

    def get_context_data(self):
        context = super().get_context_data()
        user = context.get("user")
        context["username"] = user.username
        return context


class PasswordResetEmail(EmailManager):
    template_name = "user/password_reset.html"

    def get_context_data(self):
        context = super().get_context_data()
        user = context.get("user")
        context["username"] = user.username
        context["uid"] = utils.encode_uid(user.pk)
        context["token"] = default_token_generator.make_token(user)
        context["url"] = settings.DJOSER["PASSWORD_RESET_CONFIRM_URL"].format(**context)
        return context


class PasswordChangedConfirmationEmail(EmailManager):
    template_name = "user/password_changed_confirmation.html"

    def get_context_data(self):
        context = super().get_context_data()
        user = context.get("user")
        context["username"] = user.username
        return context


class EmailResetEmail(EmailManager):
    template_name = "user/username_reset.html"

    def get_context_data(self):
        context = super().get_context_data()
        user = context.get("user")
        context["username"] = user.username
        context["uid"] = utils.encode_uid(user.pk)
        context["token"] = default_token_generator.make_token(user)
        context["url"] = settings.DJOSER["USERNAME_RESET_CONFIRM_URL"].format(**context)
        return context


class EmailChangedConfirmationEmail(EmailManager):
    template_name = "user/username_changed_confirmation.html"

    def get_context_data(self):
        context = super().get_context_data()
        user = context.get("user")
        context["username"] = user.username
        return context
