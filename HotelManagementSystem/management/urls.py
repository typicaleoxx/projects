from django.urls import path
from .views import RoomTypeView

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
    ),  # class based views use garda as_view() method call garnu parcha
]  # in crud create garna post request
# retrieve garna get,update-put. delete-delete
