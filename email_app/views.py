from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import  *
from .models import *
from email_pro.settings import EMAIL_HOST_USER
from django.contrib.auth.models import User
from django.contrib import messages
import uuid
from django.conf import settings








#as_p : it will render django forms as paragraph


def email_send(request):
    a=ContactusForm()
    if request.method=='POST':
        sub=ContactusForm(request.POST)
        if sub.is_valid():
            nm=sub.cleaned_data['Name'] #nandan
            em=sub.cleaned_data['Email'] #anshya@gmail.com
            ms=sub.cleaned_data['Message'] #hai

            send_mail(str(nm)+"||"+"TCS",ms,EMAIL_HOST_USER,[em])
            return render(request,'success.html')
    return render(request,'email.html',{'form':a})


# nandan || tcs

def register(request):
    a=regform()
    if request.method=='POST':
        b=regform(request.POST)
        if b.is_valid():
            us=b.cleaned_data["username"]
            em=b.cleaned_data["email"]
            ps=b.cleaned_data["password"]
            cp=b.cleaned_data["cpass"]
            if ps==cp:
                c=regmodel(username=us,email=em,password=ps)
                c.save()
                send_mail("Account created",str(us)+" is registered as new user",EMAIL_HOST_USER,[em])
                return render(request,'success.html')
        else:
            return HttpResponse("error")
    return render(request,'reg.html',{'form':a})











def contactus_view(request): #request='contactus.html'
    sub = ContactusForm()
    if request.method == 'POST':
        sub = ContactusForm(request.POST)
        if sub.is_valid():
            email = sub.cleaned_data['Email']
            name=sub.cleaned_data['Name']
            message = sub.cleaned_data['Message']

            send_mail(str(name)+' || '+str(email),message, EMAIL_HOST_USER, [email],
                      fail_silently = False)
            #send_mail(subject, message, from_email,recipient, fail_silently=False)

            return render(request, 'contactussuccess.html')

    return render(request, 'contactus.html', {'form':sub})


















def login(request):
        if request.method == 'POST':
            username = request.POST.get('username') #shan
            password = request.POST.get('password') #123
            user_obj = User.objects.filter(username=username).first()
            #user_obj=shan
            if user_obj is None: #if user doesn't exist
                messages.success(request, 'user not found')
                return redirect(login) #login
            profile_obj = profile.objects.filter(user=user_obj).first()
            if not profile_obj.is_verified: #if not profile is false
                messages.success(request, 'profile not verified check your mail')
                return redirect(login)
            user = authenticate(username=username, password=password)
            #user=valid
            # If the given credentials are valid, return a User object.
            if user is None:
                messages.success(request, 'wrong password or username')
                return redirect(login)
            return HttpResponse("success")
        return render(request,'login.html')
# request :register.html
def regis(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')#anshya@gmail.com
        password=request.POST.get('password')
        if User.objects.filter(username=username).first(): #username
            # #it will get first object from filter query.
            messages.success(request,'username already taken')
            #
            return redirect(regis)
        if User.objects.filter(email=email).first(): #email
            messages.success(request,'email already exist')
            return redirect(regis)
        user_obj=User(username=username ,email=email)
        user_obj.set_password(password)
        user_obj.save()
        # import uuid
        auth_token=str(uuid.uuid4()) #vd3fr65237e689236re67dgy334r76
        # new model is created
        profile_obj=profile.objects.create(user=user_obj,auth_token=auth_token) #123456
        profile_obj.save()
        # user defined
        send_mail_regis(email,auth_token) #mail sending function
        return render(request,'success.html')
    return render(request,'register.html')


def token_page(request):
    return render(request,'token.html')


def success(request):
    return render(request,'success.html')
#url





def send_mail_regis(email,auth_token):
    subject="your account has been verified"
    message=f'paste the link to verify your account http://127.0.0.1:8000/appname/verify/{auth_token}'
    email_from=EMAIL_HOST_USER #from
    recipient=[email] #to
    send_mail(subject,message,email_from,recipient)

# anshya
# token:123
#true


def verify(request,auth_token): #123
    profile_obj=profile.objects.filter(auth_token=auth_token).first()
    if profile_obj:
        if profile_obj.is_verified: #if profile object is false
            messages.success(request,'your account is already verified')
            return redirect(login) #login page
        profile_obj.is_verified=True
        profile_obj.save()
        messages.success(request,'your account has been verified')
        return redirect(login) #login function (login)
    else:
        messages.success(request,"user not found")
        return redirect(login)






def error(request):
    return render(request,'errorpage.html')






