from django.db import models

class Categories(models.Model):
  category_name = models.CharField(max_length=30)

  def __str__(self):
    return self.category_name


class News(models.Model):
  news_title = models.CharField(max_length=60)
  news_context = models.CharField(blank=True)
  created_ed = models.DateTimeField(auto_now_add=True)
  updated_ed = models.DateTimeField(auto_now=True)
  category = models.ForeignKey(Categories, on_delete=models.CASCADE)
  photo = models.ImageField(upload_to='photos/%Y/%m/%d')
  views = models.IntegerField(default=0)

  def __str__(self):
    return self.news_title
