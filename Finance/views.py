from django.shortcuts import render

# Create your views here.
def Add_transaction(request):
    return render(request,'Add_transaction.html')
def Total_transaction_by_category(request):
    return render(request,'Total_transaction_by_category.html')
def Transaction_details(request):
    return render(request,'Transaction_details.html')