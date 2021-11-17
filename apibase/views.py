from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
import cx_Oracle
from apibase.forms.user_mgmt import SignUpForm


@api_view(['post'])
def signup(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        # fullname = form.cleaned_data['fullname']
        # username = form.cleaned_data['username']
        # password = form.cleaned_data['password']
        # confirm_password = form.cleaned_data['confirm_password']
        # email = form.cleaned_data['email']

        #call sp here
        # connection = cx_Oracle.connect('db_user', 'db_password', 'connection_srting')
        # cursor = connection.cursor()
        # result = cursor.execute("call sp here")

        return JsonResponse({'status': 'success', 'error_code':200, 'message': form.cleaned_data}, safe=False)
    else:
        return JsonResponse({'status': 'failed', 'error_code': 400, 'message': form.errors}, safe=False)