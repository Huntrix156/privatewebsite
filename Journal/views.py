from django.shortcuts import render

# Create your views here.
def Add_Journal(request):
    return render(request,'Journal_detail.html')
def Delete_Journal(request):
    return render(request,'Journal_detail.html')
def Edit_Journal(request):
    return render(request,'Journal_detail.html')
def Journal_details(request):
    return render(request,'Journal_detail.html')