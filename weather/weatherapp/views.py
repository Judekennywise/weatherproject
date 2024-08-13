from django.shortcuts import render
from django.conf import settings
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import FavoriteCity, Names
from .forms import ProfileForm, PasswordChangeForm
import requests
from django.shortcuts import get_object_or_404
# Create your views here.
import urllib.request
import json

def index(request):
    weather_data = None
    if request.method == "POST":
        city = request.POST.get('city')

        # Fetch or create the Names object
        

        # Fetch weather data
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={settings.OPENWEATHER_API_KEY}'
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            weather_data = {
                'city': city,
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon'],
            }
        else:
            weather_data = {'error': 'City not found'}

        # Save to favorites if requested and user is authenticated
        

    return render(request, 'index.html', {'weather_data': weather_data})


   




# Signup view
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Signup successful! Please log in.")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

# Login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')  # redirect to the main page after login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Logout view
def logout_view(request):
    logout(request)
    return redirect('index')

@login_required
def dashboard_view(request):
    favorite_cities = FavoriteCity.objects.filter(user=request.user)
    weather_data = []

    for city in favorite_cities:
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city.city_name}&units=metric&appid={settings.OPENWEATHER_API_KEY}'
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            weather_data.append({
                'city': city.city_name,
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon'],
            })

    if request.method == "POST":
        city_name = request.POST.get("city_name")
        if city_name:
            FavoriteCity.objects.create(user=request.user, city_name=city_name)
            return redirect('dashboard')

    return render(request, 'dashboard.html', {'weather_data': weather_data})

@login_required
def profile_view(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user)
    return render(request, 'profile.html', {'form': form})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Keeps the user logged in
            return redirect('profile')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})

@login_required
def delete_account(request):
    if request.method == 'POST':
        request.user.delete()
        return redirect('index')
    return render(request, 'delete_account.html')