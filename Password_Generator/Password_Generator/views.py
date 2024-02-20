from django.shortcuts import render
import string
import random

def homepage(request):
    return render(request,"index.html")

def password_generator(request):
    pwdlen = int(request.POST.get('pwdlength'))
    pwd = ""
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    characters = letters+digits+special
    while(len(pwd) < pwdlen):
        pwd += random.choice(characters)

    
    data = {'result':pwd}

    return render(request,"password.html",data)
