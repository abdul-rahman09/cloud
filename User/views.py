
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import User
from Rooms.models import Room
from Comment.models import Comment
from django.shortcuts import redirect
from django.http import HttpResponse
import cloudinary
from django.utils.datastructures import MultiValueDictKeyError
from urllib.request import urlopen

import simplejson

def update(request):
    return render(request, "profile.html", {})


def login(request):
	 return render(request, "login.html", {})

def updateprof(request):
  try:
    if request.session['name']==None:
      return HttpResponse('Login required')
  except KeyError:
      return HttpResponse('Login required')

  name=request.POST['name']
  photo=request.FILES['photo']
  password=request.POST['password']
  obj=request.session['name']
  user=User.objects.get(email=obj)
   
  User.objects.select_for_update().filter(id=user.id).update(name=name,password=password,image=photo)
  cloudinary.uploader.upload(photo, public_id = user.username)
  return HttpResponse("updated")





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




def bookaroom_view(request,roomid):
    try:
     if request.session['name']==None:
         return HttpResponse('Login required')
    except KeyError:
          return HttpResponse('Login required')


    obj=request.session['name']
    id1=User.objects.get(email=obj)
    Room.objects.select_for_update().filter(id=roomid).update(userid = id1.id)
#    obj1=Room.objects.get(id=roomid)
#    obj1.update(userid=id1.id)
    #MyModel.objects.filter(pk=some_value).update(field1='some value')


    return HttpResponse("Booked by   "  + str(id1.id))



def getProfilePicUrl(user_id):
  api_query = urlopen('https://graph.facebook.com/'+user_id)
  dict1 = simplejson.loads(api_query.read())
  return dict1['picture']


def fb(request):
  id1=request.GET['res']
  pic_url = getProfilePicUrl(id1)
  pic = urllib.urlopen(pic_url) # retrieve the picture
  cloudinary.uploader.upload(photo, public_id = 'facebook')
  



  return HttpResponse("Fb SAved")




def hotels(request):
  obj=Room.objects.all();
  obj1=User.objects.filter(room=1)
  obj2=Comment.objects.filter(roomid=1)
  arr=[]
  for i in obj:
    arr.append(i)

  for i in obj1:
    arr.append(i)

  for i in obj2:
    arr.append(i)

  return render(request, 'hotels.html', {'obj': obj})
  


  return HttpResponse(arr)
  return render(request, "hotels.html", {})


