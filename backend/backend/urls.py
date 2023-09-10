from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers

from api import views

router = routers.DefaultRouter()
router.register('tasks', views.TaskView, 'task')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

schema_view = get_schema_view(
    info=openapi.Info(
        title='Kyttygram API',
        default_version='v1',
        description='Documentation for Kittygram API',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)

urlpatterns += [
    path(
        route='api/redoc/',
        view=schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'
    ),
]
