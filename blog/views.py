from django.shortcuts import render
from blog.models import Post, Comment
from blog.forms import CommentForm

def blog_index(request):
    template = 'blog_index.html'
    posts = Post.objects.all().order_by('-created_on')
    context = {
        'posts': posts,
    }
    return render(request, template, context)

def blog_category(request, category):
    template = 'blog_category.html'
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        'category': category,
        'posts': posts,
    }
    return render(request, template, context)

def blog_detail(request, post_id):
    template = 'blog_detail.html'
    post = Post.objects.get(pk=post_id)

    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()

    comments = Comment.objects.filter(post=post)
    context = {
        'post': post,
        'comments': comments,
        'form': form,
    }
    return render(request, template, context)