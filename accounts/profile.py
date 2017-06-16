from .models import UserProfile
from .forms import UserProfileForm
import logging


def retrieve(request):
	'''this requires an authenticated user before calling it'''
	try:
		profile = request.user.profile
	except UserProfile.DoesNotExist:
		profile = UserProfile(user=request.user) 
		profile.save()
	return profile
	


def set(request): 
	profile = retrieve(request)
	profile_form = UserProfileForm(request.POST, instance=profile)
	if profile_form.is_valid():
		profile_form.save() 
	


	
















