from django.contrib import admin
from django.urls import path, include
from .views import PostList , PostDetail

urlpatterns = [
    path('<int:pk>/', PostDetail.as_view(), name="detailcreate"),
    path('', PostList.as_view(), name="listcreate"),

]
