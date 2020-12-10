from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name="название")
    picture = models.ImageField(upload_to="media/", verbose_name="аватар")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "исполнитель"
        verbose_name_plural = "исполнители"


class Albums(models.Model):
    name = models.CharField(max_length=100, verbose_name="название")
    data = models.DateTimeField(verbose_name="дата издания")
    picture = models.ImageField(upload_to="media/", verbose_name="обложка")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="исполнитель", default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "альбом"
        verbose_name_plural = "альбомы"


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="название")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"


class Music(models.Model):
    position = models.CharField(max_length=3, verbose_name="position_in_album", default=1)
    name = models.CharField(max_length=100, verbose_name="название")
    music = models.FileField(upload_to="media/", verbose_name="песня")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="исполнитель", default=1)
    album = models.ForeignKey(Albums, on_delete=models.CASCADE, verbose_name="альбом", default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="категория", default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "трек"
        verbose_name_plural = "треки"
