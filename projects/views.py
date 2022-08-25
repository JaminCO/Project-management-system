from django.http import HttpResponse
from .models import Projects, Task
from django.shortcuts import render, redirect
from datetime import  datetime
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic import DeleteView, UpdateView
from django.views.generic.list import ListView
from .forms import ProjectForm, ProjectUpdateForm, TaskForm, TaskUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required
def home_view(request):
    project_count = Projects.objects.all().count()
    
    if project_count == 0:
        isempty = True
    else:
        isempty = False

    project = Projects.objects.all()
    for i in project:
        task = Task.objects.get(project=i) 

    context = {
        "project":project,
        "task":task,
        "isempty":isempty
	}

    return render(request, 'projects/dashboard.html', context)


# task = Task.objects.all().filter(project=project)
#         # context['object'] = Projects.objects.all().filter(user=self.request.user and complete=False)
#         context['Task'] = task


class ProjectDetailView(LoginRequiredMixin, DetailView):

    model = Projects
    template_name = 'projects/project_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        g = context['object']
        ik = g.pk
        project = Projects.objects.get(pk=ik)

        context['task_object'] =  Task.objects.all().filter(project=project)
        test = context['task_object']
        context['active_count'] = context['task_object'].filter(complete=False).count()
        context['active'] = context['task_object'].filter(complete=False)
        context['inactive_count'] = context['task_object'].filter(complete=True).count()
        context['inactive'] = context['task_object'].filter(complete=True)
        return context


class ProjectListView(LoginRequiredMixin, ListView):

    model = Projects
    paginate_by = 5  # if pagination is desired
    template_name = 'projects/dashboard.html'
    # context_object_name = 'projects'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = Projects.objects.filter(user=self.request.user)
        test = context['object']
        search_input = self.request.GET.get('q') or ''
        if search_input:
            context['object_list'] = test.filter(name__icontains=search_input)
        context['search_input'] = search_input
        context['active_count'] = context['object'].filter(complete=False).count()
        context['object_list'] = context['object'].filter(complete=False)
        context['inactive_count'] = context['object'].filter(complete=True).count()
        context['inactive'] = context['object'].filter(complete=True)
        return context


class TaskDetailView(LoginRequiredMixin, DetailView):

    model = Task
    template_name = 'projects/task_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # g = context['object']
        # ik = g.project
        # project = Projects.objects.get(project=ik)
        # task = Task.objects.all().filter(project=project)
        # context['object'] = Projects.objects.all().filter(user=self.request.user and complete=False)
        # context['project'] = project
        return context

@login_required
def form(request):
    form = ProjectForm(request.POST or None)
    # dateform = DateForm(request.POST or None)
    if request.method == 'POST':
        form = ProjectForm(request.POST or None)
        # dateform = DateForm(request.POST or None)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            # post_added = True
            # form.save()
            messages.success(request, ('Project has been Created!'))
            return redirect('projects:home-view')
        return render(request, 'projects/forms.html', {'form':form})

    else:
        return render(request, "projects/forms.html", {'form':form})


@login_required
def task_form(request, *args, **kwargs):
    form = TaskForm(request.POST or None)
    # dateform = DateForm(request.POST or None)
    if request.method == 'POST':
        form = TaskForm(request.POST or None)
        # dateform = DateForm(request.POST or None)

        if form.is_valid():
            instance = form.save(commit=False)
            pk = kwargs.get('pk')
            pros = Projects.objects.get(pk=pk)
            instance.project = pros
            instance.save()
            # post_added = True
            # form.save()
            messages.success(request, ('Task has been Created!'))
            return redirect('projects:home-view')
        return render(request, 'projects/task_forms.html', {'form':form})

    else:
        return render(request, "projects/task_forms.html", {'form':form})



class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    form_class = ProjectUpdateForm
    model = Projects
    template_name = 'projects/project_update.html'
    success_url = reverse_lazy('projects:home-view')

    
    def form_valid(self, form):
        print(form.instance.user)
        # return super().form_valid(form)
        if form.instance.user == self.request.user:
            return super().form_valid(form)
        else:
            form.add_error(None, "You need to be the author of the project in order to update it")
            messages.warning(self.request, "You need to be the author of the project in order to update it")
            return super().form_invalid(form)
            


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Projects
    template_name = 'projects/project_confirm_del.html'
    success_url = reverse_lazy('projects:home-view')
    # success_url = 'dashboard/'

    def get_object(self, *args, **kwargs):
        # pk = self.kwargs.get('pk')
        # obj = Projects.objects.get(pk=pk)
        # return obj
        pk = self.kwargs.get('pk')
        obj = Projects.objects.get(pk=pk)
        if obj.user != self.request.user:
            messages.warning(self.request, 'You need to be the author of the project in order to delete it')
            # return obj
        elif obj.user == self.request.user:
            return obj

def project_incomplete(request, *args, **kwargs):
    pk = kwargs.get('pk')
    obj = Projects.objects.get(pk=pk)
    if obj.user != request.user:
            messages.warning(request, 'You need to be the author of the project in order to commit any changesto this project')
    elif obj.user == request.user:
        pname = obj.name
        obj.complete = False
        obj.save()
        messages.success(request, (f'{pname} has been Changed to inconplete project!'))
    return redirect('projects:dashboard')

def project_complete(request, *args, **kwargs):
    pk = kwargs.get('pk')
    obj = Projects.objects.get(pk=pk)
    if obj.user != request.user:
            messages.warning(request, 'You need to be the author of the project in order to commit any changesto this project')
    elif obj.user == request.user:
        pname = obj.name
        obj.complete = True
        obj.save()
        messages.success(request, (f'{pname} has been Completed!'))
    return redirect('projects:dashboard')


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    form_class = TaskUpdateForm
    model = Task
    template_name = 'projects/task_update.html'
    success_url = reverse_lazy('projects:home-view')

    
    def form_valid(self, form):
        # print(form.instance.user)
        # return super().form_valid(form)

        task_pk = self.kwargs.get('pk')
        # project = project.get(pk=pk)
        task = Task.objects.get(pk=task_pk)
        tname = task.project
        project = Projects.objects.get(name=tname)
        # obj = task
        if project.user == self.request.user:
            return super().form_valid(form)
        else:
            # form.add_error(None, "You need to be the author of the project in order to update it")
            messages.warning(self.request, "You need to be the author of the project in order to update it")
            return super().form_invalid(form)            


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'projects/task_confirm_del.html'
    success_url = reverse_lazy('projects:home-view')
    # success_url = 'dashboard/'

    def get_object(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        obj = Task.objects.get(pk=pk)
        return obj
        
        # task_pk = self.kwargs.get('pk')
        # project = project.get(pk=pk)
        # project = Projects.objects.get(pk=pk)
        # task = Task.objects.get(pk=pk)
        # obj = task
        # if project.user != self.request.user:
        #     messages.warning(self.request, 'You need to be the author of the project in order to delete it')
        #     # return obj
        # elif project.user == self.request.user:
        # return obj

def task_complete(request, *args, **kwargs):
    pk = kwargs.get('pk')
    obj = Task.objects.get(pk=pk)
    pname = obj.taskname
    obj.complete = True
    obj.save()
    messages.success(request, (f'task {pname} has been Completed!'))
    return redirect('projects:dashboard')

def task_incomplete(request, *args, **kwargs):
    pk = kwargs.get('pk')
    obj = Task.objects.get(pk=pk)
    pname = obj.taskname
    obj.complete = False
    obj.save()
    messages.success(request, (f'{pname} has been Changed to inconplete task!'))
    return redirect('projects:dashboard')
