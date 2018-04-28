# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from User.models import User
# Create your models here.
class Room(models.Model):
	photo = models.ImageField(upload_to='Pictures')
	Price=models.CharField(max_length=20)
	isbooked=models.BooleanField(default=False)
	userid = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)




	def __str__(self):
		return  str(self.id) +'     ' + '       '+ self.Price