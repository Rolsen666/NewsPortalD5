from django.urls import path
from .views import PostNewsList, Post_Filter, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, \
   ProfileUpdateView



urlpatterns = [
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.
   path('', PostNewsList.as_view()),
   path('search/', Post_Filter.as_view()),
   path('<int:pk>', PostDetailView.as_view(), name='news_detail'),
   path('add/', PostCreateView.as_view(), name='add'),
   path('edit/<int:pk>', PostUpdateView.as_view(), name='edit'),
   path('delete/<int:pk>', PostDeleteView.as_view(), name='delete'),
   path('accounts/login', ProfileUpdateView.as_view(),
        name='profile_update'),
]
