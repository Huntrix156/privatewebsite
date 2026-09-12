from django.shortcuts import render, redirect

from Media import models
from Media.ProjectForm import ProjectForm


# Create your views here.
def Album(request):
    return render(request,'Album.html')
def Detail(request):
    return render(request,'Detail.html')
def Gallery(request):
    return render(request,'Gallery.html')
def Upload(request):
    return render(request,'Upload.html')
def project_achieved(request):
    projects = models.Project.objects.all()
    return render(request,'project_achieved.html',{'projects':projects})
def Add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('project_achieved')

    else:
        form = ProjectForm()
    return render(request,'Add_project.html',{'form':form})
