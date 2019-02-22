# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from user_model.models import register_model
from django.shortcuts import render

# Create your views here.
def profile(request):
    request.session.set_expiry(300)
    print 'profile user_id is'
    try:
        the_userid = request.session['user_id']
        print the_userid
        try:
            if the_userid:
                print "hey profile"
                register_mod = register_model.objects.get(id = the_userid)
                print register_mod
                context = {
                    'register_mod' : register_mod
                }                    
                return render(request, 'profilee/profile.html', context)
            else:
                print 'no profile'
                context = {
                    'message': 'Might be there is some error, please try again later' 
                }
                
        except:
            context = {
                    'message': 'Might be there is some error, please try again later' 
                }
    except:
        print 'no the_id'
        context = {
                    'message': 'Please Login your account and if you are a new user than register first and than proceed' 
                }
    return render(request, 'user_model/error.html', context)

    
    