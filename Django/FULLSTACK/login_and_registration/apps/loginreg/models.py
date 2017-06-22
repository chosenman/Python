# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.core.exceptions import ValidationError
from django.core.validators import validate_email

# Create your models here.
class UserManager(models.Manager):
    def login(self, email, password):
        e_mail = True
        pw_match = True
        user = ''

        if len(Users.objects.filter(email=email)) == 0:
            e_mail = False
            return answer
        elif Users.objects.get(email=email).password != password:
            pw_match = False
        else:
            user = Users.objects.get(email=email)
            
        answer = (e_mail, pw_match, user)
        return answer

    def register(self, first_name, last_name, email, password, repassword ):
        f_name = True
        l_name = True
        fl_name_alpha = True
        e_mail = True
        pw_length = True
        pw_match = True
        e_mail_uniq = True

        if len(first_name)<2:
            f_name = False
        if len(last_name)<2:
            l_name = False

        # is alphabetical string was imput
        if not str(first_name).isalpha() or not str(last_name).isalpha():
            fl_name_alpha = False

        # email validation
        try:
            validate_email(email)
        except:
            e_mail = False

        # the same emails
        if len(Users.objects.filter(email=email))>0:
            e_mail_uniq = False

        # password match
        if password != repassword:
            pw_match = False
        if len(password)<8:
            pw_length = False

        answer = (
            f_name,         # 0
            l_name,         # 1
            fl_name_alpha,  # 2
            e_mail,          # 3
            pw_length,      # 4
            pw_match,        # 5
            e_mail_uniq     # 6
            )
        return answer

class Users(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    objects = UserManager()
