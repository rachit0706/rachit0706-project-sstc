from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('about/', views.about,name='about'),
    path('contact/', views.contact,name='contact'),
    path('college/', views.collegeHome,name='collegehome'),
    path('collegeproj/', views.collegeProj,name='collegeproj'),
    # path('signup/', views.handleSignup,name='signup'),
    # path('login/', views.handleLogin,name='login'),
    # path('logout/', views.handleLogout,name='logout'),
    path('mech/', views.mech,name='mech'),
    path('civil/', views.civil,name='civil'),
    path('cse/', views.cse,name='cse'),
    path('it/', views.it,name='it'),
    path('ee/', views.ee,name='ee'),
    path('eee/', views.eee,name='eee'),
    path('addProject/', views.addProject,name='addProject'),
    path('success/', views.success,name='success'),
   
]