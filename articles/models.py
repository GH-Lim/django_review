from django.db import models


class Article(models.Model):  # 장고의 모델을 상속
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)