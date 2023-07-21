from django.urls import path
from .views import (NewsList, NewsDetail,
                    NewsCreate, NewsUpdate,
                    NewsDelete, NewsSearch,
                    ArticleCreate, ArticleUpdate,
                    ArticleDelete, CategoriListView, subscrib)
# from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', NewsList.as_view(), name='news_list'),
    path('<int:pk>/', NewsDetail.as_view(), name='news-details'),
    path('create/', NewsCreate.as_view(), name='news_create'),
    path('<int:pk>/edit/', NewsUpdate.as_view(), name='news_edit'),
    path('<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
    path('search/', NewsSearch.as_view(), name='news_search'),
    path('cre/', ArticleCreate.as_view(), name='article_create'),
    path('<int:pk>/edit/', ArticleUpdate.as_view(), name='article_edit'),
    path('<int:pk>/del/', ArticleDelete.as_view(), name='article_delete'),
    path('categories/<int:pk>', CategoriListView.as_view(), name='categori_list'),
    path('categories/<int:pk>/subscribe/', subscrib, name='subscribe'),
    # path('', set_timezone, name='set_timezone'),

]
