from django.db import models


class Autor(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()
    birthday = models.DateField()
    fullname = models.CharField(max_length=200, blank=True)

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.fullname = f'{self.firstname} {self.lastname}'
        return super().save(self)


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    views_count = models.IntegerField(default=0)
    publicate = models.BooleanField(default=False)

    def __str__(self):
        return str(self.title)


class Comment(models.Model):
    author = models.ForeignKey(Autor, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateField()
    edit_date = models.DateField()
