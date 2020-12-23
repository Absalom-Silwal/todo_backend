from django.urls import path,include
from backend import views

urlpatterns = [
    
   path('',views.Tasklist.as_view()),
   path('detail/<int:pk>',views.TaskDetail.as_view()),
   path('users',views.UserList.as_view()),
   path('users/<int:pk>',views.UserDetail.as_view())
]
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]