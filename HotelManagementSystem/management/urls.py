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
    ),  # class based views use garda as_view() method call garnu parcha
]  # in crud create garna post request
# retrieve garna get,update-put. delete-delete
