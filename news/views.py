# Create your views here.
from django.views.generic import TemplateView, DetailView
from news.models import News, Category


# Create your views here.

class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['trending'] = News.objects.all().order_by('-pub_date')[:3]
        context['rightcontent'] = News.objects.all().order_by('-pub_date')[3:5]
        categories = Category.objects.all()[:5]
        context['categories'] = []
        context['news'] = {}
        for category in categories:
            news = News.objects.filter(category=category).order_by('-pub_date')[:5]
            if len(news) > 0:
                context['categories'].append(category)
                context['news'][category.id] = news
        context['most_recent_detail'] = News.objects.first()
        context['most_recent_single'] = News.objects.all().order_by('-pub_date')[8:10]

            # context['news'][category]= News.objects.filter(category=category).order.by('pub_date')[:5]
        return context


class CategoryPageView(TemplateView):
    template_name = 'category.html'


class AboutUsPageView(TemplateView):
    template_name = 'about.html'


class ContactPageView(TemplateView):
    template_name = 'contact.html'


class LatestNewsPageView(TemplateView):
    template_name = 'latest_news.html'


# Create your views here.
class DetailPageView(TemplateView):
    template_name = 'detailnews.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        news= News.objects.get(pk=self.kwargs["pk"])
        context["detail"] = news
        return context
