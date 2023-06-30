from django.urls import path
from . import views



urlpatterns =[
    path('',views.BookListApiView.as_view(), name='book_list_api_view'),
    path('book-detail/<str:pk>/', views.BookDetailApiView.as_view(), name='book_detail_api_view'),
    path('book-detail/<str:pk>/update', views.BookUpdateApiView.as_view(), name='book_detail_update_api_view'),
    path('book-detail/<str:pk>/delete', views.BookDeleteApiView.as_view(), name='book_detail_delete_api_view'),
]