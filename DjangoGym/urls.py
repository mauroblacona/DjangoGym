from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import ObtainAuthToken
from SmartGym import views

from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'empleados', views.EmpleadoViewSet)
router.register(r'socios', views.SocioViewSet)
router.register(r'sucursales', views.SucursalViewSet)
router.register(r'actividades', views.ActividadViewSet)
router.register(r'profesionales', views.ProfesionalViewSet)
router.register(r'autoridades', views.AutoridadViewSet)
router.register(r'posiblesclientes', views.PosibleClienteViewSet)
router.register(r'consultorios', views.ConsultorioViewSet)
router.register(r'proveedores', views.ProveedorViewSet)
router.register(r'asistenciasocios', views.AsistenciaSocioViewSet)
router.register(r'asistenciaempleados', views.AsistenciaEmpleadoViewSet)
router.register(r'insumos', views.InsumoViewSet)
router.register(r'ejercicios', views.EjercicioViewSet)
router.register(r'rutinas', views.RutinaViewSet)
router.register(r'turnos', views.TurnoViewSet)
router.register(r'cajas', views.CajaViewSet)
router.register(r'recordatorios', views.RecordatorioViewSet)
router.register(r'cuotas', views.CuotaViewSet)
router.register(r'liquidaciones', views.LiquidacionViewSet)
router.register(r'horarios', views.HorarioViewSet)
router.register(r'usuarios', views.UserViewSet)


urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', ObtainAuthToken.as_view()),
    path('estadisticas/', views.estadisticas, name='estadisticas'),
]

admin.site.site_header = 'SmartGym'
admin.site.index_title = 'SmartGym'
admin.site.site_title = 'Panel Administrativo'
admin.site.site_url = "http://localhost:4200/principal/"


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
