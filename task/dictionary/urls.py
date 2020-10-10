from django.urls import path

from .views import WordView


app_name = "words"

urlpatterns = [
    path('words/', WordView.as_view()),
    path('words/<int:pk>', WordView.as_view()),
]
