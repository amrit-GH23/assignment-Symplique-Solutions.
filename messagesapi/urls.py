# urls.py (in the same app or your project urls)
from django.urls import path
from .views import save_message

urlpatterns = [
    path('save-message/', save_message),
]
