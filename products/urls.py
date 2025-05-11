from django.urls import path, include
from products import views

urlpatterns = [
    # path("", views, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("signin/", views.signin, name="log"),
    path('contact/', views.contact_view, name='contact'),
    
]