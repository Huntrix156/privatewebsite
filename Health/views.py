from django.shortcuts import render

# Create your views here.
def Add_record(request):
    return render(request,'Add_record.html')
def Emergency_contact(request):
    return render(request,'Emergency_contact.html')
def Record_details(request):
    return render(request,'Record_details.html')
def Record_list(request):
    return render(request,'Record_list.html')
