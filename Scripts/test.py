import random, sys, os, django

sys.path.append("""E:\All_Projects\Python\Django\Hostel""")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Hostel.settings")
django.setup()

from accounts.models import User_details
from django.contrib.auth.models import User


def populate(n):
    for i in range(0,n) :
        us = User.objects.create_user(str(20164000+i), password='pass12@0')
        us.save()

        us_det = User_details()
        us_det.user_user = us
        us_det.user_reg_no = 20164000+i
        us_det.user_email = "user_" + str(i) + "@mnnit.ac.in"
        us_det.user_name = "user" + str(i)
        if random.randint(1, 2) % 2 == 1:
            us_det.user_gender = 'M'
        else:
            us_det.user_gender = 'F'
        us_det.user_cpi = random.randint(1, 1000)/100.0
        us_det.contact = 100000000+i
        us_det.authority = 0
        us_det.type = 0
        us_det.year = random.randint(1, 4)
        us_det.save()


def typify():

    mem = User_details.objects.filter(type=0)

    for i in mem:
        r = 0
        if i.user_gender == 'M' :
            r = 0
        else :
            r = 10
        i.type = r + i.year
        i.save()


populate(40)
typify()
