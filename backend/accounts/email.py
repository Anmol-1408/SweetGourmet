from djoser import email
import logging

logger = logging.getLogger(__name__)

class ActivationEmail(email.ActivationEmail):
    def get_context(self):
        context = super().get_context()
        # Add your custom domain to the activation URL
        context['activation_url'] = f"https://authmate.xyz/{context['activation_url']}"
        return context

    template_name = 'accounts/activation.html'


class ConfirmationEmail(email.ConfirmationEmail):
    def get_context(self):
        context = super().get_context()
        # Add your custom domain to the confirmation URL
        context['confirmation_url'] = f"https://authmate.xyz/{context['confirmation_url']}"
        return context

    template_name = 'accounts/confirmation.html'


class PasswordResetEmail(email.PasswordResetEmail):
    def get_context(self):
        context = super().get_context()
        # Add your custom domain to the reset password URL
        context['reset_password_url'] = f"https://authmate.xyz/{context['reset_password_url']}"
        return context

    template_name = 'accounts/password_reset.html'


class PasswordChangedConfirmationEmail(email.PasswordChangedConfirmationEmail):
    def get_context(self):
        context = super().get_context()
        # Add your custom domain to the password changed confirmation URL
        context['password_changed_url'] = f"https://authmate.xyz/{context['password_changed_url']}"
        return context

    template_name = 'accounts/password_changed_confirmation.html'