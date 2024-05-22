from . import views
from django.urls import path,include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("user_list", views.UserListView)


urlpatterns = [
    path('', include(router.urls)),
    path("register/", views.UserRegistrationView.as_view(), name="register"),
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("logout/", views.UserLogoutView.as_view(), name="logout"),
    path('active/<uid64>/<token>/', views.activate, name='activate'),
]
