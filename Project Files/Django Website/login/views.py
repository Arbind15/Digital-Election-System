from django.shortcuts import render,redirect
from .models import Voterlist
from django.contrib import messages
from .form import UserLoginForm
from login.form import UserRegisterForm,UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate,logout
from login.doc_gen import pdf
from django.conf import settings
import random
import sqlite3
from django.contrib.auth.models import User


def home(request):
    form=UserLoginForm()
    contex={'form':form}
    return render(request, 'login/home.html', contex)

def detail(request):
    voterlist=Voterlist.objects.order_by('Name')
    contex={'voterlist':voterlist}
    return render(request, 'login/detail.html', contex)

def forget_pass(request):
    voterlist=Voterlist.objects.order_by('Name')
    contex={'voterlist':voterlist}
    return render(request, 'login/forget_pass.html', contex)

def register(request):
    flag=""
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        print(form.is_valid)
        if form.is_valid():
            # voterlist = Voterlist.objects.all()
            # for cid in voterlist:
            #     ctz=form.cleaned_data.get('Citizen_ID_Number')
            #     if cid.Citizen_ID_Number==ctz:
            #         print("Match")
            #         flag="F"
            #         messages.error(request, f'Account with Citizen ID Number  {ctz} already exist!,\n '
            #         f'Make mure you typed it correctly. Or Visit Related Office for more information. ')
            #         form = UserRegisterForm()
            #         contex = {'form': form}
            #         return render(request, 'login/register.html', contex)
            #         break
            # if flag!="F" :
            print("kl")
            model_instance = form.save(commit=False)
            # model_instance.post = self.object
            # model_instance.author = self.request.user
            # model_instance.Date_of_Birth = datetime.datetime.now()
            # model_instance.publish = True
            model_instance.save()
            # form.save()
            username=form.cleaned_data.get('username')
            psw=form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=psw)
            login(request, user)
            print(username,psw)
            return redirect('register2')
    else:
        form = UserCreationForm()
    contex={'form':form}
    return render(request, 'login/register.html', contex)

# @login_required(login_url='login')
def register2(request):
    if request.method=='POST':
        form = UserRegisterForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            print('valid')
            usr=request.POST.get('Citizen_ID_Number',False)
            # for item in Voterlist.objects.all():
            #     if str(item.Citizen_ID_Number) == str(usr):
            #         messages.error(request, f'Account with Citizen ID Number {usr} already exists. Make sure you typed it '
            #         f'correctly or visit related office for further information.')
            #         username=(request.user.username,)
            #         logout(request)
            #         c = sqlite3.connect("D:\Documents\Python\Del_pro\db.sqlite3")
            #         c.execute("DELETE FROM auth_user  WHERE username=(?)", username)
            #         c.commit()
            #         c.close()
            #         form=UserCreationForm()
            #         contex = {'form': form}
            #         return render(request, 'login/register.html', contex)
            model_instance=form.save(commit=False)
            username=request.user
            model_instance.save()
            messages.success(request, f'Account created for {username}!')
            return redirect('home')
        else:
            form = UserRegisterForm()
    else:
        form = UserRegisterForm(initial={"Voter_ID_Number":random.randint(1000000,100000000)})
        form.fields["Voter_ID_Number"].widget.attrs['readonly']=True
    contex={'form':form}
    return render(request, 'login/register2.html', contex)

    contex = {'form': form}
    return render(request, 'login/register2.html', contex)

@login_required
def profile(request):
    media = settings.MEDIA_ROOT
    u_form = UserRegisterForm(instance=request.user)
    c_form = UserCreationForm(instance=request.user)
    usr=request.user
    data = [usr.username,(str(usr.first_name)+' '+str(usr.last_name)),
            usr.email]
    for item in Voterlist.objects.all():
        if str(item.Voter) ==str(usr.username):
            temp=item
            data.append(item.Voter_ID_Number)
            data.append(item.Citizen_ID_Number)
            data.append(item.Phone)
            data.append(item.Address)
            data.append(item.Date_of_Birth)
            data.append(item.Gender)
            data.append(item.Remark)
            data.append(item.Province)
            data.append(item.Photo_Candidate)
            data.append(item.Photo_Citizenship_Front)
            data.append(item.Photo_Citizenship_Rare)
            data.append(item.Vote_Status)
            if item.Remark=="Pending":
                data.append(media+"/pen.png")
            if item.Remark=="Approved":
                data.append(media + "/app.png")
            print(media + "/app.png")
        else:
            print("no")
    print(usr.username)

    if request.method=="POST":
        return pdf(request,data)



    context = {
        'c_form':c_form,
        'u_form': u_form,
        'temp':temp
        }
    return render(request, 'login/profile.html', context)