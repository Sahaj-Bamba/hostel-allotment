from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from accounts.models import User_details

def home(request):
    return render(request, 'base/home.html', {})


def not_found(request):
    update(request)
    return render(request, 'base/not_found.html', {})


def update(request):
    try:
        if request.user.is_authenticated:
            pass
            temp = User_details.objects.get(user_user=request.user)
            request.session['gamer_type'] = temp.type
            request.session['gamer_authority'] = temp.authority
        else :
            request.session['gamer_type'] = 0
            request.session['gamer_authority'] = 0
    except ObjectDoesNotExist:
        request.session['gamer_type'] = 0
        request.session['gamer_authority'] = 0
