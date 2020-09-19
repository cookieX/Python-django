from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views as view

urlpatterns = [
    path("register/", view.UserSignUpView.as_view()),
    path("list/", view.UserList.as_view()),
    path("edit/me/", view.ManageUserView.as_view()),
    path("change/password/", view.UpdatePassword.as_view()),
    path("<slug:username>/", view.UserProfileView.as_view(), name="user-profile"),
    path("<slug:username>/follow/", view.FollowUserView.as_view(), name="follow-user"),
    path(
        "<slug:username>/get-followers/",
        view.GetFollowersView.as_view(),
        name="get-followers",
    ),
    path(
        "<slug:username>/get-following/",
        view.GetFollowingView.as_view(),
        name="get-following",
    ),
]
