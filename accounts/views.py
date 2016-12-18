from django.shortcuts import render
from account import views as account_views
# Create your views here.

def signup(request):
    if request.method == "POST":
        user = request.user
        request.next = "artists/" #+ user.username
        response = account_views.SignupView.as_view()(request)
        return response
    else:
        response = account_views.SignupView.as_view()(request)
        return response



