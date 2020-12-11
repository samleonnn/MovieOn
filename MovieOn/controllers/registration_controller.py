from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def index(request):
    msg = ''
    if request.method == 'POST':
        req = request.POST.dict()
        username = req['username']
        password = req['password']
        email = req['email']
        try:
            user = User.objects.get(username=username)
            msg = 'Username or E-Mail is already registered'
        except User.DoesNotExist:
            user = User.objects.create_user(username, email, password)
            user.save()
            msg = ''
            html_message = render_to_string('regis_email.html', {'context': 'values'}, username)
            send_mail(
                'Welcome to MovieOn journey!',
                'You are now a member of MovieOn',
                settings.EMAIL_HOST_USER,
                [email],
                html_message = html_message,
                fail_silently=True,
            )
        return HttpResponseRedirect('accounts/login?next=/')

    data = {
        'user_exists_error': msg,
    }
    
    return render(request, 'registration.html', data)