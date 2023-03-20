import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'Voice_Blogs.settings')

import django
django.setup()

from django.contrib.auth.models import User
from user.models import UserProfile

user = User.objects.filter(username="Himani")[0]
print(user)
data = UserProfile.objects.filter(user=user)
print(len(data))
print('changing')