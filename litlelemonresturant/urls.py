from django.urls import path
from .views import PostListView,PostDetailView,BookMeal
from .views import home ,about


urlpatterns = [
    path('',home,name="home"),
    path('about/',about,name="about"),
    path('menu/',PostListView.as_view(),name="menu"),
    path('menu_item/<int:pk>/',PostDetailView.as_view(),name="menu_item"),
    path('Book/', BookMeal.as_view(),name="Book" ),
   
]
