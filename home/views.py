from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Contact, StudentProject
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
import razorpay
from django.views.decorators.csrf import csrf_exempt
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, PasswordChangeForm

# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def mech(request):
    return render(request, 'mech.html')


def civil(request):
    return render(request, 'civil.html')


def cse(request):
    return render(request, 'cse.html')


def it(request):
    return render(request, 'it.html')


def ee(request):
    return render(request, 'ee.html')


def eee(request):
    return render(request, 'eee.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            messages.success(request, f'Account created for {username}!')
            return redirect('collegehome')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, f'Password updated successfully!')
            return redirect('collegeproj')
        else:
            messages.error(request, "Fill the fields properly")
            return redirect('change_password')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'changepassword.html', {'form': form})


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        id = request.POST['student_id']
        content = request.POST['content']
        print(name, email, phone, content)
        if len(name) < 2 or len(email) < 5 or len(phone) < 10 or len(content) < 10:
            messages.error(request, "Please fill contact form correctly")
            return redirect('home')
        else:
            contact = Contact(name=name, email=email,
                              phone=phone, content=content, id=id)
            contact.save()
            messages.success(
                request, "Your has been recieved by us, we will get back to you shortly.")
            return redirect('home')

    return render(request, 'home.html')


@login_required
def addProject(request):
    if request.method == "POST":
        username = request.POST.get('projUsername')
        name = request.POST.get('studentname')
        student_id = request.POST.get('edrpID')
        email = request.POST.get('email')
        phone = request.POST.get('contactNo')
        semester = request.POST.get('semester')
        branch = request.POST.get('branch')
        project_topic = request.POST.get('projTop')
        project_expert = request.POST.get('projExp')
        amount = int(request.POST.get("projCost")) * 100
        client = razorpay.Client(
            auth=("rzp_test_mXXfi6MoDP64rS", "JydA15d2BruBnsJtPAP1iZIs"))
        payment = client.order.create(
            {'amount': amount, 'currency': 'INR', 'payment_capture': '1'})

        if len(phone) != 10:
            messages.error(request, 'Enter a valid phone number.')
            return redirect('addProject')

        if not student_id.isalnum():
            messages.error(
                request, 'Enter a valid student ID (alphanumeric - example - BE2017XXXX).')
            return redirect('addProject')

        if len(name) < 6:
            messages.error(request, 'Enter a valid name.')
            return redirect('addProject')

        if len(project_topic) < 6:
            messages.error(request, 'Enter a valid project topic name.')
            return redirect('addProject')

        # print(name,student_id,email,phone,semester,branch,project_topic,project_expert)
        addProject = StudentProject(username=username, name=name, student_id=student_id, email=email, phone=phone, semester=semester,
                                    branch=branch, project_topic=project_topic, project_expert=project_expert, amount=amount, payment_id=payment['id'])
        addProject.save()
        return render(request, "collegeproj.html", {'payment': payment})
    return render(request, 'collegeproj.html')



def collegeHome(request):
    return render(request, 'collegehome.html')


@login_required
def collegeProj(request):
    return render(request, 'collegeproj.html')

# def handleSignup(request):
#     if request.method == 'POST':
#         fname = request.POST['fname']
#         lname = request.POST['lname']
#         username = request.POST['username']
#         email = request.POST['email']
#         pass1 = request.POST['pass1']
#         pass2 = request.POST['pass2']

#         if len(username)>20:
#             messages.error(request,"User name must be under 15 characters")
#             return redirect('collegehome')

#         if not username.isalnum():
#             messages.error(request,"User name must contain only letters and numbers")
#             return redirect('collegehome')

#         if pass1 != pass2:
#             messages.error(request,"Passwords do not match!")
#             return redirect('collegehome')

#         myuser = User.objects.create_user(username=username,email=email,password=pass1)
#         myuser.first_name = fname
#         myuser.last_name = lname
#         myuser.save()
#         messages.success(request, "Your account has been successfully created.")
#         return redirect('collegehome')

#     else:
#         return HttpResponse("ERROR")


def handleLogin(request):

    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully logged in.")
            return redirect('collegeproj')
        else:
            messages.error(request, "Invalid Credentials, please try again")
            return redirect('collegehome')

    return HttpResponse('ERROR')


def Login(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'Successfully Logged Out')
        return redirect('collegehome')

    return HttpResponse('ERROR')


@csrf_exempt
def success(request):
    if request.method == "POST":
        a = request.POST
        order_id = ""
        for key, val in a.items():
            if key == 'razorpay_order_id':
                order_id = val
                break
            print(order_id)
        user = StudentProject.objects.filter(payment_id=order_id).first()
        user.save()
    messages.success(
        request, "Payment Successfull!. We'll get back to you shortly.")
    return redirect('collegeproj')


@login_required
def stud_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.studentprofile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('stud_profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.studentprofile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'profile.html', context)
