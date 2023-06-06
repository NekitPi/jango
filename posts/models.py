from django.db import models


class Post(models.Model):
    CATEGORY = (
        ("n", "News"),
        ("m", "Music"),
        ("s", "Sport")
    )

    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(default=None, blank=True)
    tags = models.ManyToManyField("PostTag", related_name="posts")
    category = models.CharField(max_length=5, choices=CATEGORY, default="l", blank=True)

    date_create = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}. Пост: {self.title}, {self.description}" \
               f", {self.category}, {self.date_create}"

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

class PostTag(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.id} Тэг: {self.title}"

    class Meta:
        verbose_name = "Тэг"
        verbose_name_plural = "Тэги"