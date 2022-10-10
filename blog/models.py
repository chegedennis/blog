from tabnanny import verbose
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return '%s' % self.slug  
    
    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    category = models.ForeignKey(Category, related_name='articles', on_delete=models.CASCADE)
    body = RichTextUploadingField(blank=True, null=True)
    image = models.ImageField(upload_to='uploads')
    created_at = models.DateTimeField(auto_now_add=True)
    # active = models.BooleanField(default=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '%s' % (self.slug)

class Comment(models.Model):
    author = models.CharField(max_length=100)
    email = models.EmailField()
    article = models.ForeignKey(Article, related_name='comments',on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # manually deactivate inappropriate comments from admin site
    active = models.BooleanField(default=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        return f"Comment by: {self.author}"

    


