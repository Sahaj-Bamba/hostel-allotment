from django import forms
from . import models

class ProfileDetails(forms.ModelForm):
    class Meta:
        model = models.User_details
        fields = [
            'user_reg_no',
            'user_email',
            'user_name',
            'user_gender',
            'user_cpi',
            'user_bio',
            'user_contact',
        ]