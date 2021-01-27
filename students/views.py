from django.shortcuts import render, redirect
from students.forms import StudentsForm
from students.models import Students

# Create your views here.

## Post Functionality
def std(request):
    if request.method == "POST":
        form = StudentsForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/view')
            except:
                pass
    else:
        form = StudentsForm()
    # this like "retutn render(request, view, data which is displayed"
    return render(request,'index.html',{'form':form})

## View/ Read Functionality
def view(request):
    students = Students.objects.all()
    return render(request, "view.html", {'students': students})