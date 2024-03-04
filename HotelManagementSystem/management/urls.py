from django.urls import path
from .views import RoomTypeView, RoomView, UserView, RoomEditView, GroupView

urlpatterns = [
    path(
        "room-type/",
        RoomTypeView.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
    ),
    # url ko difference anusar diff path rakheko, kina ki to retrieve specific data, or delete specific, we have to send id of specific data
    path(
        "room-type/<int:pk>/",
        RoomTypeView.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}),
    ),
    path("room/", RoomView.as_view()),
    # class based views use garda as_view() method call garnu parcha
    path("room/<int:pk>/", RoomEditView.as_view()),
    path("register/", UserView.as_view({"post": "register"}), name="register"),
    path("login/", UserView.as_view({"post": "login"}), name="login"),
    path("role/", GroupView.as_view({"get": "list"}), name="role-listing"),
]  # in crud create: garna post request
# retrieve garna get,update-put. delete-delete
