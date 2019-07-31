"""gifticon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import blog.views
import category.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name = 'home'),
    path('blog/<int:blog_id>', blog.views.detail, name = 'detail'),
    path('blog/new/', blog.views.new, name = 'new'),
    path('blog/create/', blog.views.create, name = 'create'),
    path('drink/', category.views.drink, name = 'drink'),
    path('food/', category.views.food, name = 'food'),
    path('fashion/', category.views.fashion, name = 'fashion'),
    path('specialPrice/', category.views.specialPrice, name = 'specialPrice'),
    path('detail/<int:blogDrink_id>', category.views.Drinkdetail, name = 'Drinkdetail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
