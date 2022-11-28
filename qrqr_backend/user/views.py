from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import redirect,render
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import cSignupForm
from django.contrib.auth import authenticate, login

# from user.forms import ProfileForm

# Create your views here.
def signup(request):
    print('회원가입호출')
    if request.method == 'POST':
        signupForm = cSignupForm(request.POST)
        if signupForm.is_valid():
            signupForm.save()
            username = signupForm.cleaned_data.get('username')
            raw_password = signupForm.cleaned_data.get('password1')
            # user = authenticate(username=username, password=raw_password)
            # login(request, user)
            print('회원가입성공')
            return redirect('user/login.html')
    else:
        signupForm = cSignupForm()
    return render(request,'user/signUp.html',{'signupForm':signupForm})


def login(request):
    print('로그인호출')
    if request.method == 'POST':
        loginForm = AuthenticationForm(request,request.POST)
        if loginForm.is_valid():
            auth_login(request,loginForm.get_user())
            return redirect('/list/')
        else:
            return render(request, "main.html")
    else:
        loginForm = AuthenticationForm()
    return render(request,'user/login.html',{'loginForm':loginForm})
def logout(request):
    print('로그아웃성공')
    auth_logout(request)
    return redirect('/list/')

@login_required(login_url='login') #사용자 프로필 수정이므로 로그인여부확인
def edit_user_profile(request):
    if request.method == "POST":
        file_Form = ProfileForm(request.POST)
        if file_Form.is_valid():
            profile_file = file_Form.save(commit=False)
            if request.FILES:  # 파일 업로드 여부 체크
                profile_file.imgfile = request.FILES['imgfile']  # 들어온 파일들중에 이름이 imgsrc인 녀석을 대입시켜준다
                # 원래는 이미지 확인하는 소스를 만들어야 하지만 테스트 이므로 그냥 한다.
            profile_file.writer = request.user
            profile_file.save()
            return redirect('/list/')
    return redirect('/list/')


#임시로 만든 메인페이지
def mainFunc(request):
    return render(request, 'main.html')