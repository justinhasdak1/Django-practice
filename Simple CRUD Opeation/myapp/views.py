# Django imports
from django.shortcuts import render, redirect, get_object_or_404
from django.db.utils import IntegrityError
from .models import User  # User মডেলটি ইনপোর্ট করা

# Home Page Function
def home(request):
    # সমস্ত ইউজারের তালিকা নিয়ে আসা
    users = User.objects.all()
    # 'index.html' টেমপ্লেটে ইউজারের তালিকা পাঠানো
    return render(request, 'index.html', {'users': users})

# New User Record Function
def new_record(request):
    if request.method == "POST":  # যদি POST পদ্ধতিতে ডেটা আসে
        # ফর্ম থেকে নাম, বয়স, ফোন নম্বর নেয়া
        input_name = request.POST['name']
        input_age = request.POST['age']
        input_phone = request.POST['phone']

        # চেক করা হচ্ছে, ফোন নম্বর আগে থেকে ডেটাবেসে আছে কি না
        if User.objects.filter(phone=input_phone).exists():
            return render(request, 'index.html', {'users': User.objects.all(), 'error': 'এই তথ্যটি আগেই আছে!'})

        try:
            # নতুন ইউজার তৈরি
            users = User(name=input_name, age=input_age, phone=input_phone)
            users.save()  # ইউজার ডেটাবেসে সংরক্ষণ
        except IntegrityError:
            return render(request, 'index.html', {'users': User.objects.all(), 'error': 'এই তথ্যটি আগেই আছে!'})

    return redirect('home')  # সফলভাবে সেভ হলে হোম পেজে রিডাইরেক্ট

# Delete User Function
def delete_record(request, id):
    if request.method == "GET":  # যদি GET পদ্ধতিতে রিকোয়েস্ট আসে
        try:
            user = User.objects.get(id=id)  # ইউজারটি খুঁজে পাওয়া
            user.delete()  # ইউজারটি মুছে ফেলা
        except User.DoesNotExist:
            pass  # যদি ইউজার না থাকে কিছুই করা হবে না
    return redirect('home')  # হোম পেজে ফিরে আসা

# Update User Function
def update(request, id):
    # ইউজারটি পাওয়া যাক, যদি না পাওয়া যায়, 404 দেখানো হবে
    user = get_object_or_404(User, id=id)

    if request.method == "POST":  # যদি POST পদ্ধতিতে ফর্ম সাবমিট করা হয়
        # ইউজারের তথ্য আপডেট করা
        user.name = request.POST['name']
        user.age = request.POST['age']
        user.phone = request.POST['phone']

        # চেক করা হচ্ছে, অন্য কোন ইউজারের ফোন নম্বর এক্সিস্ট করে কি না
        if User.objects.exclude(id=id).filter(phone=user.phone).exists():
            return render(request, 'update.html', {'user': user, 'error': 'এই ফোন নম্বরটি আগেই নিবন্ধিত আছে!'})

        user.save()  # ইউজারের নতুন তথ্য ডেটাবেসে সেভ
        return redirect('home')  # হোম পেজে ফিরে আসা

    # যদি GET পদ্ধতিতে আসা হয়, তাহলে আপডেট ফর্ম প্রদর্শন করা
    return render(request, 'update.html', {'user': user})
