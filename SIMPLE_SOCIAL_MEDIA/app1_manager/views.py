from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse 
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .models import Post

def user_login(request):
    
    if request.method == 'GET':
        return render(request, 'index.html')
    
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            request.session['username'] = username
            messages.info(request, 'Successfully logged in...')
            return render(request, 'home.html')

        messages.info(request, ('Incorrect username or password!'))
        return render(request, 'index.html')




def user_logout(request):
    logout(request)
    messages.info(request, ('You have logged out! '))
    return render(request, 'index.html')



def new_post(request):

    if request.method == 'GET':
        return render(request, 'new_post.html')
    
    elif request.method == 'POST':
        
        username = request.session['username']
        user = User.objects.get(username = username)
        title = request.POST['title']
        image = request.FILES['image']
        description = request.POST['description']

        post_instance = Post(user_id = user, title = title, description = description, image = image)
        post_instance.save()

        messages.info(request, ('Post successfully posted!'))
        return redirect('home')

def create_account(request):

    if request.method == 'GET':
        return render(request, 'create_account.html')

    elif request.method == 'POST':
        username = request.POST['username'] 
        email    = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        user = User.objects.filter(username = username)
        print('user is ', str(user))

        if user.first():
            messages.info(request, ('Username already taken!!!'))
            return render(request, 'create_account.html')
        
        if password1 != password2:
            messages.info(request, ('Passwords entered are not same'))
            return render(request, 'create_accoun.html')
        
        user = User(username = username, password = password1, email = email, is_staff = False)
        user.save()

        request.session['username'] = username
        
        messages.info(request, ('Account Created Successfully!'))

        return render(request, 'home.html')


def home(request):

    posts = Post.objects.all().order_by('-date')

    context = {}
    context['posts'] = posts
    
    return render(request, 'home.html', context)
    