# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from User.models import User
from Rooms.models import Room
# Create your models here.
class Comment(models.Model):
	Desc = models.CharField(max_length=200)
	userid = models.ForeignKey(User,on_delete=models.CASCADE)
	roomid=models.ForeignKey(Room,on_delete=models.CASCADE)


	def __str__(self):
		return  str(self.id) +'     ' + self.Desc 