from django.db import models  # Django মডেল ইমপোর্ট করা হয়েছে

# User টেবিল তৈরি করা
class User(models.Model):
    name = models.CharField(max_length=50)  # ইউজারের নাম (সর্বোচ্চ ৫০ অক্ষর)
    age = models.IntegerField()  # ইউজারের বয়স
    phone = models.CharField(max_length=15, unique=True)  # ফোন নম্বর (ইউনিক)
