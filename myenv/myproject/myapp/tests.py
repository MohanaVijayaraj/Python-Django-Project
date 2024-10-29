from django.test import TestCase
from .forms import EmployeeForm

class EmployeeFormTest(TestCase):

    def test_employee_form_valid_data(self):
        """Test form with valid data, including the correct date format."""
        form_data = {
            'employee_name': 'John Doe',
            'date_of_joining': '2024-09-26'  # Valid date in YYYY-MM-DD format
        }
        form = EmployeeForm(data=form_data)
        self.assertTrue(form.is_valid())  # The form should be valid

    def test_employee_form_invalid_date_format(self):
        """Test form with an invalid date format (non-ISO format)."""
        form_data = {
            'employee_name': 'John Doe',
            'date_of_joining': '26-09-2024'  # Invalid date format (DD-MM-YYYY)
        }
        form = EmployeeForm(data=form_data)
        self.assertFalse(form.is_valid())  # The form should be invalid due to date format

    def test_employee_form_missing_name(self):
        """Test form when the employee_name is missing."""
        form_data = {
            'employee_name': '',  # Name is missing
            'date_of_joining': '2024-09-26'
        }
        form = EmployeeForm(data=form_data)
        self.assertFalse(form.is_valid())  # The form should be invalid due to missing name
        self.assertIn('employee_name', form.errors)  # Check if the error is related to the name field

    def test_employee_form_missing_date(self):
        """Test form when the date_of_joining is missing."""
        form_data = {
            'employee_name': 'John Doe',
            'date_of_joining': ''  # Date is missing
        }
        form = EmployeeForm(data=form_data)
        self.assertFalse(form.is_valid())  # The form should be invalid due to missing date
        self.assertIn('date_of_joining', form.errors)  # Check if the error is related to the date field

    def test_employee_form_invalid_characters_in_name(self):
        """Test form with invalid characters in employee_name."""
        form_data = {
            'employee_name': 'John123',  # Invalid name (includes numbers)
            'date_of_joining': '2024-09-26'
        }
        form = EmployeeForm(data=form_data)
        self.assertFalse(form.is_valid())  # The form should be invalid
        self.assertIn('employee_name', form.errors)  # Check if the error is related to the name field

    def test_employee_form_future_date(self):
        """Test form with a future date."""
        form_data = {
            'employee_name': 'John Doe',
            'date_of_joining': '2025-01-01'  # A future date
        }
        form = EmployeeForm(data=form_data)
        self.assertTrue(form.is_valid())  # Assuming future dates are allowed, the form should be valid

    def test_employee_form_past_date(self):
        """Test form with a past date."""
        form_data = {
            'employee_name': 'John Doe',
            'date_of_joining': '2000-01-01'  # A past date
        }
        form = EmployeeForm(data=form_data)
        self.assertTrue(form.is_valid())  # Assuming past dates are allowed, the form should be valid
