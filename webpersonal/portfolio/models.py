from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.CharField(
        verbose_name="Título",
        max_length=255,
    )
    description = models.TextField(
        verbose_name="Descripción",
    )
    image = models.ImageField(
        verbose_name='Imagen',
        upload_to='projects',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Fecha de creación',
    )
    update_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Fecha de actualización',
    )

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = [
            '-created_at',
        ] 

    def __str__(self):
        return self.title