# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from django.contrib import messages
from .models import Users

# Create your views here.
def index(request):

    return render(request,'loginreg/index.html')

def loginreg(request):

    if request.method == "POST":
        if request.POST['action'] == 'reg':
            fname = request.POST['fname']
            lname = request.POST['lname']
            email = request.POST['email']
            password = request.POST['password']
            repassword = request.POST['repassword']

            answer = Users.objects.register(fname, lname, email, password, repassword)
            print answer

            if not answer[0] or not answer[1]:
                messages.add_message(request, messages.ERROR, 'Please enter string at least 3 characters in Name and Lastname fields')
            elif not answer[2]:
                messages.add_message(request, messages.ERROR, 'Use only alphabet characters')
            elif not answer[3]:
                messages.add_message(request, messages.ERROR, 'Email is not valid')
            elif not answer[4]:
                messages.add_message(request, messages.ERROR, 'Password is too short')
            elif not answer[5]:
                messages.add_message(request, messages.ERROR, "Passwords don't match")
            elif not answer[6]:
                messages.add_message(request, messages.ERROR, "We already have this email in data base")
            else:
                # if everything is good
                Users.objects.create(fname=fname,lname=lname,email=email,password=password)
                request.session['name'] = fname
                messages.add_message(request, messages.SUCCESS, "Successfully registered!")
                return render(request,'loginreg/loginreg.html')

            return redirect('/')

        elif request.POST['action'] == 'login':
            email = request.POST['email']
            password = request.POST['password']

            answer = Users.objects.login(email, password)

            if not answer[0]:
                messages.add_message(request, messages.ERROR, "We don't have such user with that email")
                return redirect('/')
            elif not answer[1]:
                messages.add_message(request, messages.ERROR, "The password you entered don't match this email")
                return redirect('/')
            elif  answer[2] != '':
                messages.add_message(request, messages.SUCCESS, "Successfully logined!")
                request.session['name'] = answer[2].lname
                return render(request,'loginreg/loginreg.html')
    else:
        return redirect('/')
