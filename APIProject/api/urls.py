

from django.urls import path
from .views import ArticleList
#article_list, article_details

urlpatterns = [
    path('articles/', ArticleList.as_view())
    #path('articles/', article_list),
    #path('articles/<int:pk>/', article_details),
]
