from django.urls import path
from .views import home, info

app_name = "lanapp"

urlpatterns = [
    path('', home),
    path('<slug:slug>/', info, name="info"),
]
