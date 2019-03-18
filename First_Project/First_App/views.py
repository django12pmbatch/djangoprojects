from django.shortcuts import render

from django.http import HttpResponse
def emp(request):
    emp_data={
        'eno':100,
        'ename':'pavan',
        'esal':10000,
        'eaddrs':'Hyderbad'
    }
    res = "<h1>Employee Number:{}<br> Employee Name:{}<br> Employee Salary:{}<br> Employee Adderess:{}".format(emp_data['eno'],emp_data['ename'],emp_data['esal'],emp_data['eaddrs'])
    return HttpResponse(res)