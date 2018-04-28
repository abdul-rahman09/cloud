
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import User
from django.http import HttpResponse
import cloudinary
from django.utils.datastructures import MultiValueDictKeyError

def login(request):
	   return render(request, "login.html", {})

def authenticate(request):
  try:
    email = request.GET['mail'].lower()
    if '@' in email:
       user = User.objects.get(email = email)
       if(user.password!=request.GET['password']):
        return HttpResponse('Password Incorrect')
    else:
       user=User.objects.get(username=email)
       if(user.password!=request.GET['password']):
        return HttpResponse('Password Incorrect')
  except MultiValueDictKeyError:
       return HttpResponse(' Please Login First')
  except User.DoesNotExist:
    return HttpResponse(' User Not Found')
         
  request.session['name']=user.email

  return render(request, 'bookaroom.html', {'user': user})

def signup(request):
   return render(request, "signup.html", {})

def logout(request):
  try:
    del request.session['member_id']
  except KeyError:
    pass
  return render(request, "signup.html", {})


def add_user(request):

    mail=request.POST['mail'].lower()
    password=request.POST['password']
    name = request.POST['name'].lower()
    username=request.POST['username'].lower()
    photo=request.FILES['fileToUpload']
    cloudinary.uploader.upload(photo, public_id = username)
    obj=User(email=mail,name=name,password=password,username=username,image=photo)
    obj.save()
    return HttpResponse("Saved")




def bookaroom_view(request):
    try:
     if request.session['name']==None:
         return HttpResponse('Login required')
    except KeyError:
          return HttpResponse('Login required')
    return HttpResponse("Booked")





def hotels(request):
   return render(request, "hotels.html", {})


