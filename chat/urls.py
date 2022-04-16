from django.urls import path
from .views import RegisterView, LoginView, UserView, Logout
from .views import TicketViewSet, CategoryViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register('tickets', TicketViewSet)
router.register('category', CategoryViewSet)


urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout', Logout.as_view()),
]


