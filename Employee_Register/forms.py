from django.forms import ModelForm
from .models import Employee
class EmployeeForm(ModelForm):
    class Meta:
        model=Employee
        fields=('fullname','Mob_number','Emp_code','position')
        labels={'fullname':'Name',
                'Emp_code':'Employee Code',
                'Mob_number':'Mobile_number',
                'position':'Job '}