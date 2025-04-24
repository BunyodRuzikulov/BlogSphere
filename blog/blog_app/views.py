from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Post, Category, Comment, Like, Profile
from .forms import SignUpForm, CommentForm, ProfileForm, ContactForm
from django.contrib.auth.models import User
from django.db.models import Count


def home(request):
    posts = Post.objects.filter(status='published').order_by('-created_at')
    paginator = Paginator(posts, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    featured_post = posts.first()
    return render(request, 'home.html', {
        'posts': page_obj,
        'featured_post': featured_post,
    })
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status='published')
    post.views += 1
    post.save()
    comments = post.comments.filter(active=True, parent=None)
    comment_form = CommentForm()
    related_posts = Post.objects.filter(category=post.category, status='published').exclude(id=post.id)[:3]

    if request.method == 'POST' and request.user.is_authenticated:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            parent_id = request.POST.get('parent_id')
            if parent_id:
                comment.parent = Comment.objects.get(id=parent_id)
            comment.save()
            messages.success(request, 'Kommentingiz yuborildi va moderatsiyadan so‘ng ko‘rsatiladi.')
            return redirect('post_detail', slug=post.slug)

    return render(request, 'post_detail.html', {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
        'related_posts': related_posts,
    })

def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(category=category, status='published')
    sort = request.GET.get('sort', 'newest')

    if sort == 'popular':
        posts = posts.annotate(like_count=Count('likes')).order_by('-like_count')
    elif sort == 'most_viewed':
        posts = posts.order_by('-views')
    else:
        posts = posts.order_by('-created_at')

    paginator = Paginator(posts, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'category.html', {
        'category': category,
        'posts': page_obj,
    })

def profile(request, username):
    user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=user, status='published').order_by('-created_at')
    return render(request, 'profile.html', {
        'profile_user': user,
        'posts': posts,
    })

@login_required
def profile_edit(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profilingiz muvaffaqiyatli yangilandi.')
            return redirect('profile', username=request.user.username)
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'profile_edit.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)  # Profil avtomatik yaratiladi
            login(request, user)
            messages.success(request, 'Ro‘yxatdan o‘tish muvaffaqiyatli!')
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Kirish muvaffaqiyatli!')
            return redirect('home')
        else:
            messages.error(request, 'Noto‘g‘ri foydalanuvchi nomi yoki parol.')
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    messages.success(request, 'Chiqish muvaffaqiyatli!')
    return redirect('home')

@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, status='published')
    like, created = Like.objects.get_or_create(post=post, user=request.user)
    if not created:
        like.delete()
    return redirect('post_detail', slug=post.slug)

def search(request):
    query = request.GET.get('q', '')
    results = Post.objects.filter(
        Q(title__icontains=query) | Q(content__icontains=query) | Q(tags__icontains=query),
        status='published'
    ).order_by('-created_at')
    paginator = Paginator(results, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'search.html', {
        'query': query,
        'results': page_obj,
    })

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Bu yerda email yuborish logikasi qo‘shilishi mumkin
            messages.success(request, 'Xabaringiz yuborildi!')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def archive(request):
    year = request.GET.get('year')
    posts = Post.objects.filter(status='published').order_by('-created_at')
    if year:
        posts = posts.filter(created_at__year=year)
    years = Post.objects.filter(status='published').dates('created_at', 'year', order='DESC')
    paginator = Paginator(posts, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'archive.html', {
        'posts': page_obj,
        'years': [y.year for y in years],
    })