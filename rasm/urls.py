from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rasm.views import (
    ImageKirishViewSet, ImagemMaketViewSet, ImagemOrqafonViewSet, ImagemMatnViewSet,
    HouseViewSet, VideoViewSet, ContactViewSet, Contact2ViewSet, NashiUslugiViewSet, HouseDesignViewSet
)
schema_view = get_schema_view(
    openapi.Info(
        title="Maqola",
        default_version='v1',
        description="Test description",
        terms_of_service="demo.com",
        contact=openapi.Contact(email="jamshidbek@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
router = DefaultRouter()
router.register(r'imagekirish', ImageKirishViewSet)
router.register(r'imagemmaket', ImagemMaketViewSet)
router.register(r'imagemorqafon', ImagemOrqafonViewSet)
router.register(r'imagemmatn', ImagemMatnViewSet)
router.register(r'houses', HouseViewSet)
router.register(r'videos', VideoViewSet)
router.register(r'contacts', ContactViewSet)
router.register(r'contact2s', Contact2ViewSet)
router.register(r'nashiuslugi', NashiUslugiViewSet)
router.register(r'housedesigns', HouseDesignViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),

]

