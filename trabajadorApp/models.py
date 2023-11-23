from django.db import models

# Create your models here.

class Empleador(models.Model):
    nombre_empleador = models.CharField(max_length=55, null=False, blank=False)

class Seccion(models.Model):
    nombre_seccion = models.CharField(max_length=55, null=False, blank=False)
    def __str__(self):
        return self.nombre_seccion

class Area(models.Model):
    nombre_area = models.CharField(max_length=55, null=False, blank=False)
    def __str__(self):
        return self.nombre_area

class Empresa(models.Model):
    nombre_empresa = models.CharField(max_length=55, null=False, blank=False)
    def __str__(self):
        return self.nombre_empresa
    
class Trabajador(models.Model):
    nombre_trabajador = models.CharField(max_length=80, null=False, blank=False)
    rut_trabajador = models.CharField(max_length=15, null=False, blank=False, unique=True)
    fechaingreso_trabajador = models.DateField(null=False, blank=False)
    estado_trabajador = models.BooleanField()
    fk_seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE, null=False, blank=False)
    fk_area = models.ForeignKey(Area, on_delete=models.CASCADE, null=False, blank=False)
    fk_empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, null=False, blank=False)
    supervisor = models.ForeignKey('self', on_delete=models.CASCADE)                

class Contrato(models.Model):
    fk_trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE, null=False, blank=False)
    tipo_contrato = models.CharField(max_length=55, null=False, blank=False)
    def __str__(self):
        return self.tipo_contrato

class Telefono(models.Model):
    fk_trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE, null=False, blank=False)
    num_telefono = models.IntegerField(null=False, blank=False)
    def __str__(self):
        return self.num_telefono

class Email(models.Model):
    fk_trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE, null=False, blank=False)
    nombre_email = models.CharField(max_length=30, null=False, blank=False)
    def __str__(self):
        return self.nombre_email

class SaldoVacaciones(models.Model):
    fk_trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE, null=False, blank=False)
    saldo_vacaciones = models.FloatField(null=False, blank=False)
    fechainicio_sueldo = models.DateField(null=False, blank=False)
    fechafin_sueldo = models.DateField(null=False, blank=False)
    def __str__(self):
        return self.saldo_vacaciones


class TipoDocumento(models.Model):
    nombre_tipodocumento = models.CharField(max_length=15, null=False, blank=False)
    def __str__(self):
        return self.nombre_tipodocumento
    
class Documento(models.Model):
    fk_empleador = models.ForeignKey(Empleador, on_delete=models.CASCADE, null=False, blank=False)
    fk_trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE, null=False, blank=False)
    fk_tipodocumento = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE, null=False, blank=False)
    ruta_documento = models.FileField(null=False, blank=False)
    fechasolicitud_documento = models.DateField(null=False, blank=False)

class TipoSolicitud(models.Model):
    nombre_tiposolicitud = models.CharField(max_length=15, null=False, blank=False)

class Solicitud(models.Model):
    fk_tiposolicitud = models.ForeignKey(TipoSolicitud, on_delete=models.CASCADE, null=False, blank=False)
    fk_trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE, null=False, blank=False)
    fecha_solicitud = models.DateField(null=False, blank=False)
    estado_solicitud = models.CharField(max_length=15, null=False, blank=False)

class Directorio(models.Model):
    fk_seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE, null=False, blank=False)
    fk_area = models.ForeignKey(Area, on_delete=models.CASCADE, null=False, blank=False)
    nombre_directorio = models.CharField(max_length=55, null=False, blank=False)

class Tarea(models.Model):
    fk_empleador = models.ForeignKey(Empleador, on_delete=models.CASCADE, null=False, blank=False)
    fk_trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE, null=False, blank=False)
    nombre_tarea = models.CharField(max_length=55, null=False, blank=False)
    fecha_tarea = models.DateField(null=False, blank=False)