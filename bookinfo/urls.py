from rest_framework.routers import DefaultRouter
from bookinfo.views import BookViewSet

router = DefaultRouter()

router.register(r'book', BookViewSet, basename='book')
wefwf
wefwef