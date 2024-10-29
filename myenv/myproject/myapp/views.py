from django.http import HttpResponse
from django.shortcuts import render
from .forms import ExampleForm, EmployeeForm
from .models import Feature

def home(request):
    feature1 = Feature()
    feature1.id = 0
    feature1.name = 'Fast'
    feature1.details = 'Our Service is very quick'

    feature2 = Feature()
    feature2.id = 1
    feature2.name = 'Reliable'
    feature2.details = 'Our Service is very reliable'

    feature3 = Feature()
    feature3.id = 2
    feature3.name = 'Easy to use'
    feature3.details = 'Our Service is easy to use'

    feature4 = Feature()
    feature4.id = 3
    feature4.name = 'Affordable'
    feature4.details = 'Our Service is very affordable'

    return render(request, 'index.html', {'feature1' : feature1, 'feature2' : feature2, 'feature3' : feature3, 'feature4' : feature4 })

def counter(request):
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {'amount': amount_of_words})

def example_view(request):
    # import pdb; pdb.set_trace();
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # select_date = form.cleaned_data['select_date']
            return render(request, 'success.html')
    else:
        form = ExampleForm()

    return render(request, 'date_picker.html', {'form': form})

def employee_view(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee_name = form.cleaned_data['employee_name']
            date_of_joining = form.cleaned_data['date_of_joining']
            return render(request, 'success.html', {'employee_name': employee_name, 'date_of_joining': date_of_joining})
    else:
        form = EmployeeForm()

    return render(request, 'employee.html', {'form': form})
    