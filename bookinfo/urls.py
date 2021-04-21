from rest_framework.routers import DefaultRouter
from bookinfo.views import BookViewSet

router = DefaultRouter()

router.register(r'book', BookViewSet, basename='book')




class Student:
    def __init__(self, name):
        self.Name = name

s1 = Student(name='abc')