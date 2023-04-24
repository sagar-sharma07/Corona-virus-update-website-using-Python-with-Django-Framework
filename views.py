from django.shortcuts import render,redirect
from myapp import models
from django.core.mail import send_mail
from covid import settings

# Create your views here.

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def prevention(request):
    return render(request,'prevention.html')

def doctors(request):
    return render(request,'doctors.html')

def faq(request):
    return render(request,'faq.html')

def blog(request):
    blgs=models.blog.objects.all()
    print(blgs)
    return render(request,'blog.html',{'blog':blgs})

def contact(request):
    if request.method == 'POST':
        print('form submitted')
        name = request.POST.get('username')
        email = request.POST.get('user_email')
        phone = request.POST.get('phonenumber')
        message = request.POST.get('message')

        c = models.contact()
        c.username = name
        c.email = email
        c.message = message
        c.phone = phone
        c.save()
        res=1
        return render(request,'contact.html',{'response':res})

    return render(request,'contact.html')

def login(request):
    if request.method == 'POST':
        
        email = request.POST.get('user_email')
        password = request.POST.get('user_password')
        print(email)
        print(password)
        if models.registeruser.objects.filter(email=email, password=password).exists():
            user=models.registeruser.objects.get(email=email)
            request.session['userid'] = user.id
            print('Sucessful Login')

            return redirect('myprofile')

        else:
            print('invalid credentials')
            res=1
            return render(request,'login.html',{'response':res})

    return render(request,'login.html')

def situation(request):
    return render(request,'situation.html')

def advice(request):
    return render(request,'advice.html')

def symptoms(request):
    return render(request,'symptoms.html')

def donars(request):
    return render(request,'donars.html')

def fullblog(request,blogid):
    blog=models.blog.objects.get(id=blogid)
    print(blog)
    
    return render(request,'fullblog.html',{'abc':blog})

def register(request):
    if request.method == 'POST':
        print('Form Submitted')
        name = request.POST.get('username')
        email = request.POST.get('user_email')
        password = request.POST.get('user_password')
        confirmpassword = request.POST.get('cpassword')

        if password == confirmpassword :
            print('password matched')
            if models.registeruser.objects.filter(email=email).exists():
                print('Email id already exists')
                res=2
                return render(request,'register.html',{'response':res})

            else:
                print('email id does not exists')
                u = models.registeruser()
                u.name=name
                u.email=email
                u.password=password
                u.save()

                return redirect('login')

        else:
            res=1
            print('Password does not match')
            return render(request,'register.html',{'response':res})

        #r = models.registeruser()
        #r.name = name
        #r.email = email
        #r.password = password
        #r.save()

    return render(request,'register.html')

def forgetpassword(request):
    if request.method == 'POST':
        email=request.POST.get('user_email')
        print(email)
        if models.registeruser.objects.filter(email=email).exists():
            print('EMail exists')
            user=models.registeruser.objects.get(email=email)
            ####send mail

            subject='Your Forgotten Password'
            message='Your Password is: '+user.password
            email_from=settings.EMAIL_HOST_USER
            email_to=[email,]

            send_mail(subject, message,email_from,email_to)

        else:
            print('EMail does not exists')
            res=1
            return render(request,'forgetpassword.html',{'res':res})


    return render(request,'forgetpassword.html')

def myprofile(request):
    user = models.registeruser.objects.get(id = request.session.get('userid'))
    print(user)
    return render(request,'myprofile.html',{'myprofile':user})

def logout(request):
    del request.session['userid']
    return redirect('login')

def changepassword(request):

     user = models.registeruser.objects.get(id = request.session.get('userid') ) 
     print(user)

     if request.method == 'POST':
        print('Form Submitted')
        oldpassword = request.POST.get('user_password')
        newpassowrd = request.POST.get('npassword')
        confirmpassword = request.POST.get('cpassword')

        if newpassowrd == confirmpassword:
            print('Password matched')
            if oldpassword == user.password:
                print('old password matches')
                user.password = newpassowrd
                user.save()
                res=3
                print('Password changed successfully')            
                return render(request,'changepassword.html',{'response':res})



            else:
                res=2
                print('old password does not matched')            
                return render(request,'changepassword.html',{'response':res})

            


        else:
            res=1
            print('password does not matched')            
            return render(request,'changepassword.html',{'response':res})

     return render(request,'changepassword.html')