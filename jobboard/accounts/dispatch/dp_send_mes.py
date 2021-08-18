from django.dispatch import Signal
from jobboard.settings import ALLOWED_HOSTS
from django.core.signing import Signer
from django.template.loader import render_to_string


signer = Signer()


def user_register_dispatch(sender, **kwargs):
    if ALLOWED_HOSTS:
        host = 'http://' + ALLOWED_HOSTS[0]
    else:
        host = 'http://localhost:8000'
    context = {'user': kwargs['user'],
               'host': host,
               'sign': signer.sign(kwargs['user'].username)}
    subject = render_to_string('email/subject.txt', context)
    body = render_to_string('email/email_activate_user.txt', context)
    kwargs['user'].email_user(subject, body)


send_messages = Signal(providing_args=['user'])
send_messages.connect(user_register_dispatch)
