from rest_framework.routers import DefaultRouter
from .views import ProgramaViewSet, EstudianteViewSet

router = DefaultRouter()
router.register('programas', ProgramaViewSet)
router.register('estudiantes', EstudianteViewSet, basename='estudiante')

urlpatterns = router.urls
