from django.shortcuts import render,redirect
from django.views import View
# Create your views here.
from .models import Task


class TaskList(View):
    def get(self, request):
        tasks = Task.objects.all().order_by('-updated')
        context = {'tasks':tasks}
        return render(request, 'base/index.html', context)

    def post(self, request):
        task = Task.objects.create(
            body=request.POST.get('body')
        )
        task.save()
        return redirect('tasks')


class TaskDetail(View):
    def get(self, request, pk):
        task = Task.objects.get(id=pk)
        context = {'task':task}
        return render(request, 'base/task.html', context)

    def post(self, request, pk):
        task = Task.objects.get(id=pk)
        task.body = request.POST.get('body')
        task.save()
        return redirect('tasks')


class TaskDelete(View):
    def get(self, request, pk):
        task = Task.objects.get(id=pk)
        context = {'task':task}   
        return render(request, 'base/delete.html', context)

    def post(self, request, pk):
        task = Task.objects.get(id=pk)
        task.delete()
        return redirect('tasks')



