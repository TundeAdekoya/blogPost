from django.shortcuts import render, get_object_or_404,redirect
from main.models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def post_list(request):

    object_list = Post.published.all()
    paginator = Paginator(object_list, 3)
    page = request.GET.get('page') 
    
    try:
        posts = paginator.page(page)

    except PageNotAnInteger:
        posts = paginator.page(1)

    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts':posts,
        'page':page,
    }

    return render(request, 'postlist.html', context)

def post_detail(request, year, month, day, post):

    post = get_object_or_404(Post, slug=post, publish__year=year, publish__month=month, publish__day=day)

    return render(request, "postdetail.html", {"post":post})

def post(request):
        if request.method == 'POST':
            if request.POST.get('title') and request.POST.get('body'):
                post = Post()
                post.title = request.POST.get('title')
                post.body = request.POST.get('body')
                post.slug = post.title.lower().replace(' ', '-')
                post.save()

                return redirect('main:post_add')

            else:
                pass
        return render(request , 'post.html')