from django.urls import include, path
from rest_framework_nested import routers
# from bible_app.views import BookViewSet, ChapterViewSet, VerseViewSet
from bible_app import views

router = routers.SimpleRouter()
router.register(r'books', views.BookViewSet, basename='book')

urlpatterns = [
    path('', include(router.urls)),
    path('books/<str:book_name>/<int:chapter_number>/', views.ChapterViewSet.as_view({'get': 'retrieve'})),
]