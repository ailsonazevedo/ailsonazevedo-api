from rest_framework import urlpatterns
from projects.api.viewsets import ProjectViewSet, ProjectDetailViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r"projects", ProjectViewSet, basename="projects")

urlpatterns = router.urls
