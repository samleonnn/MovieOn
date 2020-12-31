from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def index(request):
    error = ''
    if request.method == 'POST':
        req = request.POST.dict()
        username = req['username']
        password = req['password1']
        verify = req['password2']
        email = req['email']

        if password != verify:
            error = 'Password is not match! Please try again'
        else:
            try: 
                user = User.objects.get(username=username)
                error = 'Sorry, Username already Exist'
            except User.DoesNotExist: 
                user = User.objects.create_user(username, email, password) 
                user.save()
                error = ''
                html_message = render_to_string('regis_email.html', {'context': 'values', 'username':username})
                send_mail(
                    'Welcome to MovieOn journey!',
                    'You are now a member of MovieOn',
                    settings.EMAIL_HOST_USER,
                    [email],
                    html_message = html_message,
                    fail_silently=True,
                )
                return redirect('login')
    data = {
        'user_exists_error': error,
    }
    return render(request, 'registration.html', data)