from django.contrib import admin
from django.urls import path
from myapp.views import home, contact_view  # Correct import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('contact/', contact_view, name='contact'),
]
