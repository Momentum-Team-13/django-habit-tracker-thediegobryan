"""habit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from habits import views as habit_views

urlpatterns = [
    path("", habit_views.homepage, name='homepage'),
    path("habits/", habit_views.list_habits, name='list_habits'),
    path("habits/new_habit", habit_views.new_habit, name='new_habit'),
    path("habits/status", habit_views.status, name='status'),
    path("habit/<int:pk>/<year>/<month>/<day>", habit_views.status_detail, name='status_detail'),
    path("habit/<int:pk>", habit_views.habit_detail, name='habit_detail'),
    path('accounts/', include('registration.backends.simple.urls')),
    path('admin/', admin.site.urls),
]
