from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns=[
    path('',HomeListView.as_view(),name='home'),
    path('filter/<int:id>/',ProductListView.as_view(),name='product'),
    path('<int:id>/',ProductDetailView.as_view(),name='detail'),   
    path('register/',RegisterPage,name='register'),
    path('accounts/login/',LoginPage,name='login'),
    path('logout/',LogoutPage,name='logout'),
    path('change/<int:id>/',ChangeProducts.as_view(),name='change_products'),
    path('add/',Addproducts,name='add_products'),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset_password/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('shop/<int:id>/',UserProfile.as_view(),name='users'),
    path('save/<int:id>/',Saves,name='saves'),
    path('mysaves/',SavePage.as_view(),name='savepage'),
    path('searchproduct/',HomeSearch,name='homesearch'),
    path('contact-us/',ContactUs.as_view(),name='contact-us'),
    path('about_us/',AboutUs.as_view(),name='about-us'),

]