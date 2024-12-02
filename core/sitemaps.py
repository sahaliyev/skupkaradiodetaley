from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'weekly'

    def items(self):
        # List of section names corresponding to their view or ID in the template
        return ['domoy', 'o-nas', 'kataloq', 'kontakt']

    def location(self, item):
        # Use reverse for dynamic URL resolution
        if item == 'index':
            return reverse('index')  # Main page
        return reverse('index') + f'#{item}'  # Section IDs
