from django.shortcuts import render,get_object_or_404, redirect
from ebiznessapp.models import (
     Banner, OurService, Statistic, Category, Portfolio, FAQ, Section, Team, SocialMedia,
     PricingTable, Testimonial, SiteSettings, Message, Site_smedia, BlogCategory, BlogTag, Blog, Comment
)

from django.core.paginator import Paginator


def index(request):
    banners = Banner.objects.all()
    ourservices = OurService.objects.all()
    statistics = Statistic.objects.all()
    categories = Category.objects.all()
    portfolios = Portfolio.objects.all()
    faqs = FAQ.objects.all()
    sections = Section.objects.all()
    teams = Team.objects.all()
    socialmedias = SocialMedia.objects.all()
    pricingtables = PricingTable.objects.all()
    testimonials = Testimonial.objects.all()
    settings = SiteSettings.objects.first()
    messages = Message.objects.all()
    sitesmedias = Site_smedia.objects.all()

    context = {
        "banners" : banners,
        "ourservices" : ourservices,
        "statistics" : statistics,
        "categories" : categories,
        "portfolios" : portfolios,
        "faqs" : faqs,
        "sections" : sections,
        "teams" : teams,
        "socialmedias" : socialmedias,
        "pricingtables" : pricingtables,
        "testimonials" : testimonials,
        "settings" : settings,
        "messages" : messages,
        "sitesmedias" : sitesmedias
    }
    
    for portfolio in portfolios:
        print(portfolio.category.title)
    return render(request, 'index.html', context)

def bloglist(request):
    blogcategories = BlogCategory.objects.all()
    blogtags =  BlogTag.objects.all()
    blogs = Blog.objects.all()
    total_comment = len(Comment.objects.all())
    if blogs.count() < 4:
        recent_posts = Blog.objects.all()
    else:
        recent_posts = Blog.objects.all()[:4]

    search = request.GET.get( "search" )
    if search:
        blogs = Blog.objects.filter(title__icontains=search)

    paginator = Paginator(blogs, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "blogcategories" : blogcategories,
        "blogtags" : blogtags,
        "blogs" : blogs,
        "recent_posts" : recent_posts,
        "total_comment" : total_comment,
        "page_obj" : page_obj
    }


    return render(request,'blog.html', context)

def detail(request, id):
    blog = get_object_or_404(Blog, id = id)
    comments = blog.comments.order_by("-id")
    blogcategories = BlogCategory.objects.all()
    blogtags =  BlogTag.objects.all()
    blogs = Blog.objects.all()
    recent_posts = blogs if blogs.count() < 4 else blogs[:4]

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        web = request.POST.get('website')
        content = request.POST.get('comment')
        idc = request.POST.get("id")
        idc = int(idc) if idc else None
        comment = Comment.objects.get(id=idc) if idc else None

        if name and email and content:
            Comment.objects.create(
                name = name,
                email = email,
                website = web,
                content = content,
                blog = blog,
                parent = comment
            )
        return redirect("blog-detail", id=id)

    context = {
        "blogs" : blogs,
        "blog" : blog,
        "comments" : comments,
        "blogcategories" : blogcategories,
        "blogtags" : blogtags,
        "recent_posts" : recent_posts,
        "countc" : blog.categories.all().count(),
        "countt" : blog.tags.all().count()
        
    }
    return render(request, 'blog-details.html', context) 