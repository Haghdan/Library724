from django.urls import path
from . import views


app_name = 'Book'
urlpatterns = [
	path('', views.all_Books, name='all_Books'),
	path('<int:id>/<str:name>/', views.book_detail, name='book_detail'),
]