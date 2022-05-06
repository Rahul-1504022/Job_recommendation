from django.conf.urls.static import static
from django.conf import settings
from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.registration,name='registration'),
    path('userlogin',views.userlogin,name='userlogin'),\
    path('userlogout',views.userlogout,name='userlogout'),
    path('user_profile',views.user_profile,name='user_profile'),
    path('userprofileedit',views.userprofileedit,name='userprofileedit'),
    path('joblist',views.joblist,name='joblist'),
    path('recommendedjob',views.recommendedjob,name='recommendedjob'),
    path('user_cv',views.user_cv,name='user_cv'),
    path('showcv',views.showcv,name='showcv'),
    path('cv_recommendedjob',views.cv_recommendedjob,name='cv_recommendedjob'),
    path('home',include('index.urls')),


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)