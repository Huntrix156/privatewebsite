from django.shortcuts import render

# Create your views here.
def Album(request):
    return render(request,'Album.html')
def Detail(request):
    return render(request,'Detail.html')
def Gallery(request):
    return render(request,'Gallery.html')
def Upload(request):
    return render(request,'Upload.html')
