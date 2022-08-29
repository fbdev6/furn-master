from django.shortcuts import render
from django.views import generic
from django.contrib.auth import get_user_model
from furnapp.models import *
from django.db.models import Q
User = get_user_model()



def home(request):
    
    if 'user' in request.GET:
        search = request.GEt['q']
        full_search = Q(Q(email__icontains=search))
        user = User.objects.filter(full_search)
    else:
        user = User.objects.all()
    users = User.objects.count()
    products = Product.objects.count()
    blog =  Blog.objects.count()
    arravial = Arrival.objects.count()
    context = {
        "user":user,
        "users":users,
        "products":products,
        "blogs":blog,
        "arravials":arravial
    }
    return render(request, 'dashboard/pages/home.html', context)

class Buttons(generic.TemplateView):
   template_name ="dashboard/includes/buttons.html"

def cards(request):
    return render(request, 'dashboard/includes/cards.html')

def animation(request):
    return render(request, 'dashboard/includes/animation.html')

def colors(request):
    return render(request, 'dashboard/includes/colors.html')

def border(request):
    return render(request, 'dashboard/includes/border.html')

def other(request):
    return render(request, 'dashboard/includes/other.html')

def dashboard_login(request):
    return render(request, 'dashboard/registertration/login.html')

def forgot_password(request):
    return render(request, 'dashboard/includes/forgot-password.html')

def register(request):
    return render(request, 'dashboard/registertration/register.html')

def charts(request):
    return render(request, 'dashboard/includes/charts.html')

def tables(request):
    return render(request, 'dashboard/includes/tables.html')

def page_404(request):
    return render(request, 'dashboard/includes/404.html')

def blank(request):
    return render(request, 'dashboard/includes/blank.html')


