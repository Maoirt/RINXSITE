from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    #path('about-us', views.about, name='about'),
    path('education', views.education, name='education'),
    # path('schedule', views.schedule, name='schedule'),
    path('teachers', views.teachers, name='teachers'),
    path('contact', views.contact, name='contact'),
    path('aboutRINX', views.aboutRINX, name='aboutRINX'),
    path('physics', views.physics, name='physics'),
    path('mathematics', views.mathematics, name='mathematics'),
    path('computer ', views.computer, name='computer'),
    path('contactKB', views.contactKB, name='contactKB'),
    path('gallery ', views.gallery, name='gallery'),
    path('register', views.register, name='register'),

]
