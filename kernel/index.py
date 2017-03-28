__author__ = 'pxxgogo'

import json
import urllib

import requests
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from pro2.settings import WEBSITE_URL


def index(request):
    return render(request, "index.html", {})


def log_in_by_github(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/")
    else:
        data = {
            'client_id': "80a5af72e242f84b9b97",
            "redirect_uri": "http://%s/log_in_temp" % WEBSITE_URL,
            "scope": "user,user:email",
            "state": "pxxGOgo_project_2"
        }
        return HttpResponseRedirect("https://github.com/login/oauth/authorize?" + urllib.urlencode(data))


def log_in_temp(request):
    code = request.GET["code"]
    state_ID = request.GET["state"]
    if not state_ID == "pxxGOgo_project_2":
        print("wrong with the state_ID")
        return HttpResponseRedirect("/")
    post_url = "https://github.com/login/oauth/access_token"
    post_header = {"Accept": "application/json"}
    post_data = {"client_id": "80a5af72e242f84b9b97",
                 "client_secret": "08c2357dac8e18b5e58d6e55de0ea60eac0ca4f8",
                 "code": code,
                 "redirect_uri": "http://%s/log_in_temp" % WEBSITE_URL,
                 "state": state_ID}
    authority_response = requests.post(post_url, data=post_data, headers=post_header)
    try:
        access_token = json.loads(authority_response.content)["access_token"]
    except:
        print(authority_response.content)
        return HttpResponseRedirect("/")
    get_user_info_url = "https://api.github.com/user"
    user_info_response = requests.get(get_user_info_url, params={"access_token": access_token})
    # print(access_token)
    user_info = json.loads(user_info_response.content)
    username = user_info["login"]
    password = user_info["id"]
    email = user_info["email"]
    users_list = User.objects.filter(username=username)
    if len(users_list) > 0:
        user = users_list[0]
        user.email = email
        user.save()
        auth.login(request, user)
        return HttpResponseRedirect("/")
    user = User.objects.create_user(username=username, password=password, email=email)
    user.save()
    auth.login(request, user)
    return HttpResponseRedirect("/")


def log_out(request):
    if request.user.is_authenticated():
        auth.logout(request)
        return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect("/")
