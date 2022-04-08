from django.urls import path
from .views import dashboard,Faq
from . import views

app_name = "yukti"

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("faq", Faq, name="Faq"),
]