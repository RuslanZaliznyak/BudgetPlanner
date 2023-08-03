from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from users.utils.token_generator import TokenGenerator


def send_registration_email(request, user_instance):
    message = render_to_string(
        'users_auth/registration_email.html',
        context={
            'user': user_instance,
            'domain': get_current_site(request),
            'uid': urlsafe_base64_encode(force_bytes(user_instance.pk)),
            'token': TokenGenerator().make_token(user_instance)
        }
    )
    print(message)

    email = EmailMessage(
        subject='blabla',
        body=message,
        to=[user_instance.email],
    )
    email.content_subtype = 'html'
    email.send()