from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.helloView),
    path("now_date/", views.now_date_view),
    path('goodbye/', views.goodbyeView),
    path('posts/', views.postlistview),
    path('posts/<int:id>/', views.postDetailInfo)
]