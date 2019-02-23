# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from user_model.models import register_model, address
from django.shortcuts import render

# Create your views here.
def profile(request):
    request.session.set_expiry(300)
    print 'profile user_id is'
    try:
        the_userid = request.session['user_id']
        print the_userid
        register_mod = register_model.objects.get(id = the_userid)
        try:
            if the_userid:
                print "hey profile"
                
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

    


def edit_profile_page(request):
    request.session.set_expiry(300)
    print 'profile user_id is'
    try:
        the_userid = request.session['user_id']
        print the_userid
        register_models = register_model.objects.get(id=the_userid)
        if the_userid:
            print 'user-id is'
            #register_model = register_model.objects.get(id=the_userid)
            context={
                "register_models": register_models
            }
            return render(request, 'profilee/edit_profile.html', context)

        else:
            print "heyyyyyyyyyyyyyyyy"
            return render(request, 'user_model/error.html')
    
    except:
        print "hey last"
        return render(request, 'user_model/error.html')



def edit_address(request):
    request.session.set_expiry(300)
    print 'profile user_id is'
    try:
        the_userid = request.session['user_id']
        print the_userid
        user = register_model.objects.get(id=the_userid)
        print user
        add = user.address_set.all()
        if the_userid:
            print the_userid
            print 'address nedeche hai'
            #ad = address.objects.all()
            #print ad
            #address = address.objects.get(user=the_userid)
            print "hey adres"
            print add
            context={
                "add" : add
            }
            return render(request, 'profilee/edit_address.html', context)
        else:
            print "pass1"
    except:
        print "not in try"