from django.urls import path
from . import views

urlpatterns = [
    path("questionnaire/", views.questionnaire, name="questionnaire"),
    path("", views.stats, name="stats"),
]
