from django import forms

# class GlobalDatePicker(forms.DateInput):
#     input_type = 'date'
#     format = '%Y-%m-%d'  

class ExampleForm(forms.Form):
    date_field = forms.CharField(widget=forms.TextInput(attrs={'class': 'datepicker'}),  # Add 'datepicker' class
        label='Select Date'
    )

class EmployeeForm(forms.Form):
    employee_name = forms.CharField(label='Employee Name', max_length=100)
    # date_of_joining = forms.DateField(widget=GlobalDatePicker(format='%Y-%m-%d'), label='Date of Joining')
    date_of_joining = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'datepicker'}),  # Apply class for jQuery UI
        label='Date of Joining'
    )