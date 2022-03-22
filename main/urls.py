from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('list/', views.post_list, name = 'postlist'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name = 'postdetail'),
    path('post/', views.post, name= 'post_add')
]
