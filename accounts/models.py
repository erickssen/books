from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from checkout.models import BaseOrderInfo


# Create your models here.

class UserProfile(BaseOrderInfo):
	# user = models.ForeignKey(User, unique=True) ----> this way gives error: "no attribute 'profile' "
	user = models.OneToOneField(User, related_name='profile') 

	def __unicode__(self):
		return 'User Profile for:' + self.user.username 






