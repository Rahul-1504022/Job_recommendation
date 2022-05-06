import pandas as pd
import json
from recommend import *
from pdftotext import *
from cvrecommendjob import *
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import userprofile,userregistration,usercv
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from .forms import RegisterForm
from django.contrib import messages


# Create your views here.

def registration(request):
    form = RegisterForm()
    

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account was created for ' + user)

            return redirect('userlogin')


    context = {'form':form}
    return render(request,'userregistration.html',context)

def userlogin(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('user_profile')

        else:
            messages.info(request,'username or password is incorrect')
              


    context = {}
    return render(request,'login.html',context)


def userlogout(request):
    logout(request)
    
    return redirect('userlogin')




def user_profile(request):
    userprofiledata = userprofile.objects.all()
    u = []
    for user in userprofiledata:
        if user.username == request.user.username:
            u=user
    print(u)


    return render(request,'userprofile.html',{'data':u})




def userprofileedit(request):
    if request.method =='POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        fullname = request.POST.get('fullname')
        aboutyourself = request.POST.get('aboutyourself')
        gender = request.POST.get('gender')
        degree = request.POST.get('degree')
        subject = request.POST.get('subject')
        presentjobdesignation = request.POST.get('presentjobdesignation')
        pastjobdesignation = request.POST.get('pastjobdesignation')
        ineterest = request.POST.get('ineterest')
        contactno = request.POST.get('contactno')
        permanentaddress = request.POST.get('permanentaddress')
        presentaddress = request.POST.get('presentaddress')

        userprofiledata=userprofile(username=username,email=email,fullname=fullname,aboutyourself=aboutyourself,gender=gender,degree=degree,subject=subject,presentjobdesignation=presentjobdesignation,pastjobdesignation=pastjobdesignation,fieldofinterest=ineterest,contactno=contactno,permanentaddress=permanentaddress,presentaddress=presentaddress)
        userprofiledata.save()        
        return redirect('user_profile')

    return render(request,'userprofileedit.html')



def joblist(request):
    ds = pd.read_csv('job-data.csv')
    job = ds.reset_index().to_json(orient ='records')
    data = []
    data = json.loads(job)
    context = {'d': data}
    
    return render(request,"joblist.html",context)



def recommendedjob(request):
    userprofiledata = userprofile.objects.all()
    u = []
    for user in userprofiledata:
        if user.username == request.user.username:
             u=user


    #data = recommend(user.subject, num=5) 
    #print(data)
    subject = u.subject
    presentjob = u.presentjobdesignation
    previousjob = u.pastjobdesignation
    interest = u.fieldofinterest
    #print(subject)
    data1 = []
    data1 = jobsearch(subject,presentjob,previousjob,interest)
    print(data1)
    data2 = []
    data2 = joborganization(subject,presentjob,previousjob,interest)  
    return render(request, 'recommendjob.html',{'d': zip(data1, data2)})

def user_cv(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        cv = request.FILES['cv']
        uploadcv = usercv(username=username,cv=cv)
        uploadcv.save()
        return redirect('user_profile')



    return render(request,"cvupload.html")


def showcv(request):
    userprofiledata = usercv.objects.all()
    c = []
    for user in userprofiledata:
        if user.username == request.user.username:
            c=user
    print(c)


    return render(request,'usercv.html',{'cvfile':c})


def cv_recommendedjob(request):
    userprofiledata = usercv.objects.all()
    c = []
    for user in userprofiledata:
        if user.username == request.user.username:
            c=user


    user_profile = userprofile.objects.all()
    u = []
    for users in user_profile:
        if users.username == request.user.username:
             u=users

    #cvname = c.cv
    #print(c.username)
    #direc = c.cv
    #print(direc)
    #filename = 'media/'+ direc
    #print(filename)
    subject = u.subject
    presentjob = u.presentjobdesignation
    previousjob = u.pastjobdesignation
    interest = u.fieldofinterest

    keyfeature = cvrecommend('cv/my cv2.pdf')
    #print (keyfeature)
    keyfeature = keyfeature +' ' + subject +' ' + presentjob + ' ' + previousjob +' ' + interest
    print(keyfeature)
    job_name = []
    job_name = cvjobsearch(keyfeature)
    print(job_name)
    job_organization = []
    job_organization = cvjoborganization(keyfeature)
    print(job_organization) 

    return render(request, 'cvrecommend.html',{'job': zip(job_name,job_organization)})