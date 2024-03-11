from django.urls import path
from .views import UserList, UserDetail,UserDetailByPhone

urlpatterns = [
    path('UsersUN/', UserList.as_view()),
    path('UsersUN/<int:pk>', UserDetail.as_view()),
    path('UsersUN/byphone/<slug:phone>',UserDetailByPhone.as_view())
]