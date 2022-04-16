from django.urls import path
from .views import RegisterView, LoginView, UserView, Logout
from .views import TicketViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register('tickets', TicketViewSet)


urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout', Logout.as_view()),
]


