from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [

	path('', views.IndexView.as_view(), name='index'),

	path('signup/', views.UserFormView.as_view(), name='signup'),

	path('<int:pk>/', views.DetailsView.as_view(), name='details'),
]