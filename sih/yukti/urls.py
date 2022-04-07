from django.urls import path
from .views import dashboard,Signup,Faq

app_name = "yukti"

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("signup", Signup, name="Signup"),
    path("faq", Faq, name="Faq"),
]