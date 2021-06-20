from django.views.generic import ListView, DetailView

# Create your views here.

from . models import Article
class ArticleListView(ListView):
    model = Article
    template_name = 'home.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = "detail.html"
    comtext_object_name = 'batman'
