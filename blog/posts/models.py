from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Blog(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="blog", verbose_name="Пользователь"
    )
    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"

class Post(models.Model):
    title = models.CharField(verbose_name="Заголовок", blank=False, max_length=100)
    text = models.TextField(
        verbose_name="Текст поста", help_text="Введите текст поста", max_length=140
    )
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posts", verbose_name="Автор"
    )

    class Meta:
        ordering = ("-pub_date",)
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def __str__(self):
        return self.text[:15]


class News(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="news", verbose_name="Пользователь"
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="posts_in_news",
        verbose_name="Пост",
    )
    is_read = models.BooleanField(default=False, verbose_name="Прочитано")

    class Meta:
        verbose_name = "Лента новостей"
        verbose_name_plural = "Ленты новостей"


class Follow(models.Model):
    follower = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="following",
        verbose_name="Подписчик",
    )
    following = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="follower", verbose_name="Автор"
    )

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"
        constraints = [
            models.UniqueConstraint(
                fields=["follower", "following"], name="unique_follower_following"
            )
        ]
