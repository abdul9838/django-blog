from django.shortcuts import render ,redirect
from django.contrib.auth import login, logout
from .models import Post
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import PostForm



# def create_post(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('post_list')  # Replace 'post_list' with the URL name of your post listing view
#     else:
#         form = PostForm()

    # return render(request, 'your_template.html', {'form': form})

# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request,'miniblog/home.html',{'posts':posts})
    
def about(request):
    return render(request,'miniblog/about.html')

def contact(request):
    return render(request,'miniblog/contact.html')

def dashboard(request):
    posts = Post.objects.all()
    return render(request,'miniblog/dashboard.html',{'posts':posts})

def signup(request):
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=UserCreationForm()
    return render(request,'miniblog/signup.html',{'form':form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'miniblog/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')


def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = PostForm()
    return render(request,'miniblog/addpost.html', {'form': form})

def edit_post(request, id):
    post=Post.objects.get(id=id)
    if request.method == 'POST':
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = PostForm(instance=post)
    return render(request,'miniblog/editpost.html', {'form': form})


def delete_post(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('dashboard')
