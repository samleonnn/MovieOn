from django.shortcuts import render

def handler500(request):
    return render(request, 'error/500.html', status=500)