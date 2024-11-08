"""ananyaproject1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
# ananyaproject1/urls.py

# ananyaproject1/urls.py

# ananyaproject1/urls.py

from django.contrib import admin
from django.urls import path
from ananyaapp1 import views  # Import the views from your app

urlpatterns = [  # Root URL mapped to home view
    path('add/', views.add_numbers, name='add_numbers'),  # /add/ URL mapped to add_numbers view
    path('sub/',views.sub_numbers,name='sub_numbers'),
    path('admin/', admin.site.urls),  # Admin URL path (default)
]



