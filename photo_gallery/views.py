from django.shortcuts import render

def index(request):
    return render(request, 'photo_gallery/index.html', {})
