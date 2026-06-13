from django.urls import path
from .views import hello
from  .views import RegisterView,UserDetailView,UserUpdateView,ChangePasswordView,EmailResetView,ForgotPasswordView,LogoutView,AdminDeleteUserView

urlpatterns = [
    path("", hello, name="hello"),
    path("register/", RegisterView.as_view(), name="register"),
    path("user/", UserDetailView.as_view(), name="user"),
    path("user/update/", UserUpdateView.as_view(), name="user_update"),
    path("user/change-password/", ChangePasswordView.as_view(), name="change_password"),
    path("user/email-reset/", EmailResetView.as_view(), name="email_reset"),
    path("user/forgot-password/", ForgotPasswordView.as_view(), name="forgot_password"),
    path("user/logout/", LogoutView.as_view(), name="logout"),
    path("admin/delete-user/<str:user_cin>/", AdminDeleteUserView.as_view(), name="delete_user")
]