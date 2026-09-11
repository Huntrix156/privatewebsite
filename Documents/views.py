from django.shortcuts import render

# Create your views here.
def Add_page(request):
    return render(request,'Add_page.html')
def Detail_page(request):
    return render(request,'Detail_page.html')
def Edit_page(request):
    return render(request,'Edit_page.html')
def list_page(request):
    return render(request,'list_page.html')
