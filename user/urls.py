from django.urls import path

from user import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('new/', views.CreateUserView.as_view(), name='user_new'),
    path('update/<int:pk>', views.UpdateUserView.as_view(), name='user_update'),
    path('delete/<int:pk>', views.DeleteUserView.as_view(), name='user_delete'),
]