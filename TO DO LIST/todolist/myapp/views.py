from django.shortcuts import render,HttpResponse,redirect
from myapp.models import student


# Create your views here.
def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,'about.html')

def form(request):
    return render(request,'form.html')



def login(request):
    return render(request,'login.html')


# def send(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         student.append(username)
#         print(student)
#         return redirect('/view')
#     else:
#         return render(request,"login.html")
    
# def view(request):
#     return render(request,'login.html',{"data":student})

# def delete_data(request,name):
#     student.remove(name)
#     print(student)
#     return redirect('/view')

# def form(request):
#     return render(request,'form.html')
def form(request):
    if request.method =="POST":
        name=request.POST['std_name']
        rollno=request.POST['rollno']
        course=request.POST['course']

        aa=student(Name=name,Rollno=rollno,Course=course)
        aa.save()
        if aa:
            return HttpResponse("done")
        else:
            return HttpResponse("try again")
    else:
        return render(request,"form.html")

def view_data(request):
    data = student.objects.all()
    return render(request,"table.html",{"data":data})

def delete_data(request,id):
    data = student.objects.get(id = id)
    data.delete()
    return redirect('/views') 

