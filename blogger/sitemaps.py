from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from blog.models import Category, Article

class CategorySitemap(Sitemap):
    def items(self):
        return Category.objects.all()

class ArticleSitemap(Sitemap):
    def items(self):
        return Article.objects.all()

    def lastmod(self, obj):
        return obj.created_at

class StaticViewSitemap(Sitemap):
    def items(self):
        return ['privacy_policy', 'cookies_policy', 'disclaimer']

    def location(self, item):
        return reverse(item)