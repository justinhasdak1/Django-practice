from django.contrib import admin
from django.urls import path
from . import views  # ভিউস ইমপোর্ট করা হয়েছে

urlpatterns = [
    path('', views.home, name='home'),  # হোম পেজ URL
    path('new/', views.new_record, name='new_record'),  # নতুন ইউজার সংযোজন URL
    path('delete/<int:id>/', views.delete_record, name='delete_record'),  # ইউজার মুছে ফেলার URL
    path('update/<int:id>/', views.update, name='update'),  # ইউজার আপডেট করার URL
]
