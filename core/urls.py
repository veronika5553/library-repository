from django.urls import path, include
from core.views import BookViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("books", BookViewSet)

urlpatterns = [
    path("", include(router.urls))
]
app = "core"
