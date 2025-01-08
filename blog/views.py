from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Article, Category


# Create your views here.


# def home(request, page=1):
#     articles_list = Article.objects.published()
#     paginator = Paginator(articles_list, 3)
#     articles = paginator.get_page(page)
#     context = {
#         "articles": articles,
#     }
#     return render(request, "blog/home.html", context)

class ArticleList(ListView):
    queryset = Article.objects.published()
    paginate_by = 3


# def article_detail(request, slug):

#     context = {
#         "article": get_object_or_404(Article.objects.published(), slug=slug, status='p')
#     }
#     return render(request, "blog/detail.html", context)

class ArticleDetail(DetailView):
    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Article.objects.published(), slug=slug, status='p')


# def category(request, slug, page=1):
#     category = get_object_or_404(Category, slug=slug, status=True)
#     article_list = category.articles.published()
#     paginator = Paginator(article_list, 2)
#     articles = paginator.get_page(page)
#     context = {
#         "category": category,
#         "articles": articles,
#     }
#     return render(request, "blog/category.html", context)


class CategoryList(ListView):
    paginate_by = 2
    template_name = "blog/category_list.html"

    def get_queryset(self):
        global category
        slug = self.kwargs.get('slug')
        category = get_object_or_404(Category.objects.active(), slug=slug)
        return category.articles.published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = category
        return context
