from django.urls import path

from users.views import Users, UsersId


urlpatterns = [
    path("", Users().as_view()),
    path("<int:id>/", UsersId().as_view()),
]
