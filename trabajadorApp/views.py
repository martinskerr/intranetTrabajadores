from django.contrib.auth import get_user_model, login, logout
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import *
from rest_framework import permissions, status
from django.core import validators
from .validations import custom_validation, validate_email, validate_password
from .models import *
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated


class UserRegister(APIView):
	permission_classes = (permissions.AllowAny,)
	def post(self, request):
		clean_data = custom_validation(request.data)
		serializer = UserRegisterSerializer(data=clean_data)
		if serializer.is_valid(raise_exception=True):
			user = serializer.create(clean_data)
			if user:
				return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(status=status.HTTP_400_BAD_REQUEST)


class UserLogin(APIView):
	permission_classes = (permissions.AllowAny,)
	authentication_classes = (SessionAuthentication,)
	##
	def post(self, request):
		data = request.data
		assert validate_email(data)
		assert validate_password(data)
		serializer = UserLoginSerializer(data=data)
		if serializer.is_valid(raise_exception=True):
			user = serializer.check_user(data)
			login(request, user)
			return Response(serializer.data, status=status.HTTP_200_OK)


class UserLogout(APIView):
	permission_classes = (permissions.AllowAny,)
	authentication_classes = ()
	def post(self, request):
		logout(request)
		return Response(status=status.HTTP_200_OK)


class UserView(APIView):
	permission_classes = (permissions.IsAuthenticated,)
	authentication_classes = (SessionAuthentication,)
	##
	def get(self, request):
		serializer = UserSerializer(request.user)
		return Response({'user': serializer.data}, status=status.HTTP_200_OK)
	
class SeccionView(viewsets.ModelViewSet):
	serializer_class = SeccionSerializer
	queryset = Seccion.objects.all()	

class AreaView(viewsets.ModelViewSet):
	serializer_class = AreaSerializer
	queryset = Area.objects.all()

class EmpresaView(viewsets.ModelViewSet):
	serializer_class = EmpresaSerializer
	queryset = Empresa.objects.all()
	
class TrabajadorView(viewsets.ModelViewSet):
	serializer_class = TrabajadorSerializer
	queryset = Trabajador.objects.all()

class ContratoView(viewsets.ModelViewSet):
	serializer_class = ContratoSerializer
	queryset = Contrato.objects.all()

class TelefonoView(viewsets.ModelViewSet):
	serializer_class = TelefonoSerializer
	queryset = Telefono.objects.all()

class EmailView(viewsets.ModelViewSet):
	serializer_class = EmailSerializer
	queryset = Email.objects.all()

class SaldoVacacionesView(viewsets.ModelViewSet):
	serializer_class = SaldoVacacionesSerializer
	queryset = SaldoVacaciones.objects.all	

class TipoDocumentoView(viewsets.ModelViewSet):
	serializer_class = TipoDocumentoSerializer
	queryset = TipoDocumento.objects.all()

class DocumentoView(viewsets.ModelViewSet):
	serializer_class = DocumentoSerializer
	queryset = Documento.objects.all()

class TipoSolicitudView(viewsets.ModelViewSet):
	serializer_class = TipoSolicitudSerializer
	queryset = TipoSolicitud.objects.all()

class SolicitudView(viewsets.ModelViewSet):
	serializer_class = SolicitudSerializer
	queryset = Solicitud.objects.all()
	
class DirectorioView(viewsets.ModelViewSet):
	serializer_class = DirectorioSerializer
	queryset = Directorio.objects.all()

class TareaView(viewsets.ModelViewSet):
	serializer_class = TareaSerializer
	queryset = Tarea.objects.all()				


class SubirDocumentoView(APIView):
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [IsAuthenticated]  # asegurar que solo admins autenticados pueden subir documentos

    def post(self, request, format=None):
        serializer = DocumentoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()  # Guarda el documento con las relaciones especificadas
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)	