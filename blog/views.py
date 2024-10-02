from django.shortcuts import render, get_object_or_404
from .models import BlogPost, Categories


def blog(request):
    category_id = request.GET.get('category')

    if category_id:
        all_posts = BlogPost.objects.filter(
            category_id=category_id).order_by('-date')
    else:
        all_posts = BlogPost.objects.all().order_by('-date')
    latest_posts = all_posts[:3]
    categories = Categories.objects.all()

    return render(request, 'blog/blog.html', {
        'all_posts': all_posts,
        'latest_posts': latest_posts,
        'categories': categories,
        'selected_category': category_id,
    })


def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, post_Slug=slug)
    return render(request, 'blog/blog_detail.html', {'post': post})
