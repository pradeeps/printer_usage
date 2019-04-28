from django.urls import path
from .views import home, post_detail

urlpatterns = [
    path('', home, name='home-page'),
    path('detail/<int:id>', post_detail, name='post-detail'),

]
