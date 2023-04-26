from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify

# Create your models here.
class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name="Nombre", null=False, blank=False)
    estado = models.BooleanField("Estado", default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    image = models.URLField('Portada Cat')
    descripcion = RichTextField(verbose_name="Descripcion", null=True, blank=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        db_table = "categorias"

    def __str__(self):
        """Return string"""
        return str(self.nombre)

class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField(verbose_name="Nombres", max_length=255, null=False, blank=False)
    apellidos = models.CharField(verbose_name="Apellidos", max_length=255, null=False, blank=False)
    facebook = models.URLField(verbose_name="Facebook", null=True, blank=True)
    twitter = models.URLField(verbose_name="Twitter", null=True, blank=True)
    instagram = models.URLField(verbose_name="Instagram", null=True, blank=True)
    email = models.EmailField(verbose_name="Email", null=False, blank=False)
    website = models.URLField(verbose_name="Web", null=True, blank=True)
    estado = models.BooleanField("Estado", default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
        db_table = "autores"

    def __str__(self):
        """Return string"""
        return f"{self.nombres} {self.apellidos}"

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(verbose_name="Titulo", max_length=255, null=False, blank=False)
    slug = models.SlugField("Slug", max_length=100, unique=True)
    description = models.CharField('Description', max_length=255, null=False, blank=False)
    contenido = RichTextField()
    images = models.URLField(verbose_name="Images", null=False, blank=False, max_length=255)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    estado = models.BooleanField("Publicado/No Publicado", default=True)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        db_table = "posts"

    def __str__(self):
        """Return string"""
        return f"{self.titulo}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)

