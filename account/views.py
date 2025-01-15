from blog.models import Article
from django.views.generic import (ListView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView,
                                  )
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import (FieldsMixin, FormVaildMixin,
                     AuthorAccessMixin, SuperUserAccessMixin)
# Create your views here.


class ArticleList(LoginRequiredMixin, ListView):
    queryset = Article.objects.all()
    template_name = "registration/home.html"

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Article.objects.all()
        else:
            return Article.objects.filter(author=self.request.user)


class ArticleCreate(LoginRequiredMixin, FormVaildMixin, FieldsMixin, CreateView):
    model = Article
    fields = ['author', 'title', 'slug', 'description', 'thumbnail',
              'category', 'publish', 'status']
    template_name = "registration/article-create-update.html"


class ArticleUpdate(AuthorAccessMixin, FormVaildMixin, FieldsMixin, UpdateView):
    model = Article
    fields = ['author', 'title', 'slug', 'description', 'thumbnail',
              'category', 'publish', 'status']
    template_name = "registration/article-create-update.html"


class ArticleDelete(SuperUserAccessMixin, DeleteView):
    model = Article
    success_url = reverse_lazy("account:home")
    template_name = "registration/article_confirm_delete.html"


# How to Build an E-commerce Website with Django and Python freeCodeCamp
