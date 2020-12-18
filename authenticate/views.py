from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView

# import forms.py file
from . forms import *
from . models import *


from django.contrib import messages
import json
import requests


class LoginView(View):
    form_class = LoginForm
    template_name = 'authenticate/login.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})


class HomePage(View):
    template_name = 'authenticate/index.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})


class UploadDetails(View):
    form_class = PersonForm
    template_name = 'authenticate/upload_details.html'

    def get(self, request, *args, **kwargs):
        if request.COOKIES.get('token') == "initialized":
            messages.success(request, ("Please login to submit your information."))
            return render(request, "authenticate/index.html", {})
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            if 'cv_file' in request.FILES:
                user.cv_file = request.FILES['cv_file']
            user.save()

            # uploading user information 3.2.1 and getting response
            response_json = upload_user_detail(user, request)
            # uploading cv as binary file (3.3.1)
            upload_cv_using_api(response_json, user, request)

        else:
            messages.success(request, ("Please enter valid information"))
            return render(request, 'authenticate/upload_details.html', {'form':self.form_class, 'errors':form.errors} )

        messages.success(request, ('Successfully Uploaded your details.'))
        return redirect('index')


def upload_user_detail(user, request):
    update_time = user.on_spot_update_time.timestamp()*1000
    creation_time = user.on_spot_creation_time.timestamp()*1000
    token = request.COOKIES.get('token')
    token = "Token " + str(token)
    # print("token ", token)

    data = {
        "tsync_id":int(user.tsync_id),
        "name":user.name,
        "email":user.email,
        "phone":user.phone_number,
        "full_address":user.full_address,
        "name_of_university":user.name_of_university,
        "graduation_year":user.graduation_year,
        "cgpa":user.cgpa,
        "experience_in_months":user.experience_in_months,
        "current_work_place_name":user.current_work_place_name,
        "applying_in":user.applying_in,
        "expected_salary":user.expected_salary,
        "field_buzz_reference":user.field_buzz_reference,
        "github_project_url":user.github_project_url,
        "cv_file": {
            "tsync_id":int(user.cv_file_tsync_id),
        },
        "on_spot_update_time":int(update_time),
        "on_spot_creation_time":int(creation_time),
    }
    data = json.dumps(data)
    # print("data ", data)
    url = "https://recruitment.fisdev.com/api/v1/recruiting-entities/"
    header = {"Content-type": "APPLICATION/JSON",
                "Authorization": token}

    response_json = requests.post(url, data=data, headers=header).json()
    # print (response_json)
    return response_json


def upload_cv_using_api(response_json, user, request):
    cv_file_id = response_json["cv_file"]["id"]
    file_upload_url = "https://recruitment.fisdev.com/api/file-object/" + str(cv_file_id) + "/"

    token = request.COOKIES.get('token')
    token = "Token " + str(token)

    cv_header = { "Authorization": token,}
    cv_file_path = user.cv_file.path
    # print("cv_file_path", cv_file_path)

    file = {'file': open(cv_file_path, 'rb')}
    # print("file ",file)

    cv_response_decoded_json = requests.put(url=file_upload_url, files=file, headers=cv_header)
    cv_response_json = cv_response_decoded_json.json()
    # print("cv response", cv_response_json)
