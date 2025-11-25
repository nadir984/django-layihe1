from django.shortcuts import render

def index(request):
    """
    Ana səhifə üçün view funksiyası.
    index.html şablonunu render edir.
    """
    return render(request, 'index.html')
