from django.forms import ModelForm, TextInput
from.models import Projects, Task
from django import forms

class DateForm(forms.Form):
    date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])

class ProjectForm(ModelForm):
    class Meta:
        model = Projects 
        fields = ['name', 'starting', "deadline", "description"]
        widgets = {'name' : TextInput(attrs={'class' : 'input', 'placeholder' : 'Project Name'}), 'starting' : TextInput(attrs={'class' : 'input', 'type':'date', 'placeholder' : ''}), 'deadline' : TextInput(attrs={'class' : 'input', 'type':'date', 'placeholder' : ''})}


class ProjectUpdateForm(ModelForm):
    class Meta:
        model = Projects 
        fields = ['name', 'starting', "deadline", "description","complete"]
        widgets = {'name' : TextInput(attrs={'class' : 'input', 'placeholder' : 'Project Name'}), 'starting' : TextInput(attrs={'class' : 'input', 'type':'date', 'placeholder' : ''}), 'deadline' : TextInput(attrs={'class' : 'input', 'type':'date', 'placeholder' : ''})}


class TaskForm(ModelForm):
    class Meta:
        model = Task 
        fields = ['taskname', 'starting', "deadline", "description"]
        widgets = {'taskname' : TextInput(attrs={'class' : 'input', 'placeholder' : 'Task Name'}), 'starting' : TextInput(attrs={'class' : 'input', 'type':'date', 'placeholder' : ''}), 'deadline' : TextInput(attrs={'class' : 'input', 'type':'date', 'placeholder' : ''})}

class TaskUpdateForm(ModelForm):
    class Meta:
        model = Task 
        fields = ['taskname', 'starting', "deadline", "description"]
        widgets = {'taskname' : TextInput(attrs={'class' : 'input', 'placeholder' : 'Task Name'}), 'starting' : TextInput(attrs={'class' : 'input', 'type':'date', 'placeholder' : ''}), 'deadline' : TextInput(attrs={'class' : 'input', 'type':'date', 'placeholder' : ''})}
