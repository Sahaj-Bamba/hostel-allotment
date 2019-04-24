from django.db import models
from django.contrib.auth.models import User


# class user_requests(models.Model):
#     user_from = models.ForeignKey(User, default=None, related_name="user_from", on_delete=models.CASCADE)
#     user_to = models.ForeignKey(User, default=None, related_name="user_to", on_delete=models.CASCADE)
#
# class priority(models.Model):
#     user = models.ForeignKey(User, default=None, related_name="_user", on_delete=models.CASCADE)
#     proff = models.ForeignKey(User, default=None, related_name="_proff", on_delete=models.CASCADE)
#     user_priority = models.DecimalField(verbose_name="priority", max_digits=4 , decimal_places=0,blank=False)

class User_details(models.Model):

    GENDER_CHOICES =(
        ('F', 'Female'),
        ('M', 'Male')
    )

    user_reg_no = models.DecimalField(verbose_name="reg_no", max_digits=8, decimal_places=0, unique=True, blank=False)
    user_email = models.EmailField(verbose_name="email", max_length=100, unique=True, blank=False)
    user_name = models.CharField(verbose_name="name", max_length=100, blank=False)
    user_gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    user_cpi = models.DecimalField(verbose_name="cpi", max_digits=4, decimal_places=2, blank=False)
    user_contact = models.CharField(verbose_name="contact", blank=False, max_length=15)
    authority = models.IntegerField(verbose_name="authority", default=0)
    type = models.IntegerField(verbose_name="type", default=0)
    year = models.IntegerField(verbose_name="year", default=0)
    user_user = models.OneToOneField(User, default=None, on_delete=models.CASCADE)

    # resume =

    # user_email = models.CharField(verbose_name="email", max_length=100, default=1)
    # user_category = models.CharField(verbose_name="category", max_length=100, default=1)
    # user_password = models.CharField(verbose_name="password", max_length=100, default=1)
    # user_first_name = models.CharField(verbose_name="first_name", max_length=100, default=1)
    # user_last_name = models.CharField(verbose_name="last_name", max_length=100, default=1)
    # user_id = models.IntegerField(verbose_name="user_id", default=1)

    def __str__(self):
        return self.user_name


class Team_details(models.Model):

    # team_id= models.IntegerField(verbose_name="team_id",default=1)
    # team_leader_name=models.CharField(verbose_name="team_leader",max_length=100,default=1)

    team_name = models.CharField(verbose_name="team_name", unique=True, max_length=100)
    team_leader = models.OneToOneField(User, related_name="leader", default=None, on_delete=models.CASCADE)
    team_member_1 = models.ForeignKey(User, default=None, related_name="member1", on_delete=models.SET_NULL, null=True)
    team_member_2 = models.ForeignKey(User, default=None, related_name="member2", on_delete=models.SET_NULL, null=True)
    team_member_3 = models.ForeignKey(User, default=None, related_name="member3", on_delete=models.SET_NULL, null=True)
    team_cpi = models.DecimalField(verbose_name="cpi", max_digits=4, decimal_places=2, blank=False)
#
#
#     def __str__(self):
#         return self.team_name
