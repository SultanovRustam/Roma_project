from django.db import models


class Era(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='eras/')
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class EraPage(models.Model):
    era = models.OneToOneField(Era, on_delete=models.CASCADE)
    content = models.TextField()
    images = models.ManyToManyField('EraImage')
    created_by = models.CharField(max_length=100)

    def __str__(self):
        return f"Страница: {self.era.title}"


class EraImage(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='era_images/')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title