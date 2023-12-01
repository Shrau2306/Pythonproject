from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, UserProfileViewSet, FileViewSet, FolderViewSet

router = DefaultRouter()
router.register('companies', CompanyViewSet)
router.register('user-profiles', UserProfileViewSet)
router.register('files', FileViewSet)
router.register('folders', FolderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]