
from django.contrib import admin
from django.urls import path, include
from users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register, name="register"),
    path('', include('market_data.urls')),
]
