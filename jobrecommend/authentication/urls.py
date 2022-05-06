from django.urls import path
from . import views

urlpatterns = [
    path('forgot-password/', views.forgotpassword,name='forgotpassword'),
    path('logout/',views.userlogout,name='logout')
    
]