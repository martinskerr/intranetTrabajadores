from django.urls import path, include
from trabajadorApp import views
from rest_framework import routers

#Registro de Views en URL con router

router = routers.DefaultRouter()
router.register(r'seccion', views.SeccionView, 'seccion')
router.register(r'area', views.AreaView, 'area')
router.register(r'empresa', views.EmpresaView, 'empresa')
router.register(r'trabajador', views.TrabajadorView, 'trabajador')
router.register(r'contrato', views.ContratoView, 'contrato')
router.register(r'telefono', views.TelefonoView, 'telefono')
router.register(r'email', views.EmailView, 'email')
router.register(r'saldovac', views.SaldoVacacionesView, 'saldovac')
router.register(r'tipodoc', views.TipoDocumentoView, 'tipodoc')
router.register(r'documento', views.DocumentoView, 'documento')
router.register(r'tiposoli', views.TipoSolicitudView, 'tiposoli')
router.register(r'solicitud', views.SolicitudView, 'solicitud')
router.register(r'directorio', views.DirectorioView, 'directorio')
router.register(r'tarea', views.TareaView, 'tarea')

urlpatterns = [
    path('api/v1/', include(router.urls)),
	path('register', views.UserRegister.as_view(), name='register'),
	path('login/', views.LoginView.as_view(), name='login'),
	path('logout', views.UserLogout.as_view(), name='logout'),
	path('user', views.UserView.as_view(), name='user')
]
