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