from django.http import HttpResponseRedirect
from django.shortcuts import render,HttpResponse
from home.models import ToDo

# Create your views here.
def home(request):
    context ={'success':False,'activeHomePage':"active"}
    if request.method=="POST":
        taskname = request.POST['taskName']
        desc = request.POST['description']
        context = {'success':True}
        instance = ToDo(TaskName = taskname,Description = desc)
        instance.save()

    return render(request,'home.html',context)

def tasks(request):
    mytodo = ToDo.objects.all()
    context={'mytasks':mytodo,'activeTaskPage':"active"}
    return render(request,'tasks.html',context)

def delete(request):
    ToDo.objects.filter(id=request.GET['id']).delete()
    return HttpResponseRedirect("tasks")

def update(request):
    taskid = request.GET['id']
    taskTitle= taskDesc = "Not_available"
    for data in ToDo.objects.filter(id = request.GET['id']):
        taskTitle = data.TaskName
        taskDesc = str(data.Description)
    context = {'taskTitle':taskTitle, 'taskDesc': taskDesc,'ID':taskid}
    return render(request,'update.html',context)

def dataupdate(request):
    if request.method =="POST":
        ID = request.GET['id']
        taskname = request.POST['taskName']
        desc = request.POST['description']
        ToDo.objects.filter(id = ID).update(TaskName = taskname,Description = desc)
        return HttpResponseRedirect("tasks")