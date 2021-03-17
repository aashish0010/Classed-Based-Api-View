from django.urls import path, include
from .views import HomeViews

urlpatterns = [
    path('home', HomeViews.as_view()),
    path('home/<int:pk>/',HomeViews.as_view()),
    path('home/<int:id>/',HomeViews.as_view()),
]
