from django.urls import path
from .views import RoomTypeView, RoomView, UserView, RoomEditView

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
    path("room/", RoomView.as_view({"get": "list", "post": "create"})),
    # class based views use garda as_view() method call garnu parcha
    path("room/<int:pk>/", RoomEditView.as_view()),
    path("register/", UserView.as_view({"post": "register"}), name="register"),
]  # in crud create: garna post request
# retrieve garna get,update-put. delete-delete
