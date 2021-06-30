from rest_framework import serializers
from EmployeeApp.models import Departments, Employees
# code from https://youtube.com/watch?v=f5ygXQKF6M8
class DepartmentSerializer(serializers.modelSerializer):
    class Meta
    model = Departments
    fields = ('DepartmentId',
              'DepartmentName')
            
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ('EmployeeId',
                'EmployeeName',
                'Department',
                'DateOfJoining',)
