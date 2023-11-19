from django.urls import path, include
from demo import views
# from demo.views import Another
from rest_framework import routers
from .views import BookViewSet

router = routers.DefaultRouter()
router.register('books', BookViewSet)
urlpatterns = [
    path('', include(router.urls))
    # path('first', views.first)  # reference to view first
    # path('another', Another.as_view()) # treat this class as as_view
]
