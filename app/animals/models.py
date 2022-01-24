from django.db import models


class Animal(models.Model):
    name = models.CharField(verbose_name='이름', max_length=128)
    created = models.DateTimeField(verbose_name='생성일시', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='수정일시', auto_now=True)


class AnimalImage(models.Model):
    seq = models.IntegerField(verbose_name='순서', default=0)
    image = models.ImageField(verbose_name='사진', upload_to='%Y/animals/%m')
    created = models.DateTimeField(verbose_name='생성일시', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='수정일시', auto_now=True)

    animal = models.ForeignKey('animals.Animal', verbose_name='동물', on_delete=models.SET_NULL,
                               related_name='image_set', related_query_name='images', null=True)



