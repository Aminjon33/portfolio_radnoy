from django.shortcuts import render
from .models import About,Portfolio,BlogPost,Contact
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse
from .bot import send_message
from django.views.generic import View
from django.core.paginator import Paginator
from .models import Post

def index_view(request):
    about_info = About.objects.all()
    portfolios = Portfolio.objects.all()
    return render(request,'index.html', {'about_info': about_info, 'portfolios': portfolios})

def about_view(request):
    about_info = About.objects.all()
    return render(request,'about.html', {'about_info': about_info})

def blog_view(request):
    posts_list = Post.objects.all()  # Barcha postlarni olish
    paginator = Paginator(posts_list, 2)  # Har bir sahifada 2 post

    page_number = request.GET.get('page')  # URL dan sahifa raqamini olish
    page_obj = paginator.get_page(page_number)  # Sahifa obyektini olish
    
    return render(request, "blog.html", {'page_obj': page_obj})


class ContactView(View):
    template_name = "contact.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs): 
        name = request.POST.get('first_name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('description', '')
        contact = Contact(first_name=name,email=email,description=message)
        contact.save()
        
        send_message(f"Ism: {name}\nEmail: {email}\nText:{message}")

        return HttpResponseRedirect(reverse('index-page')) 


def portfolio_details_view(request):
    portfolios = Portfolio.objects.all()
    return render(request,'portfolio-details.html', {'portfolios': portfolios})

def portfolio_view(request):
    portfolios = Portfolio.objects.all()
    return render(request,'portfolio.html', {'portfolios': portfolios})


def single_blog_view(request):
    posts = BlogPost.objects.all()
    return render(request,'single-blog.html', {'posts': posts})

