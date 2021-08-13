from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.utils import timezone
from .models import Post


class AppViewIdx(TemplateView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["app"] = "Index"
        return context


class AppViewPage01(TemplateView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["app"] = "Page01"
        return context

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'app_test/post_list.html', {'posts': posts})




