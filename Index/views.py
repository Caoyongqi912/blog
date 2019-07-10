from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View

from Articles.models import Classify, Articles


class Index(View):
    def get(self, request):
        classify = Classify.objects.all()
        articles = Articles.objects.all()
        articles_title = articles[:5]
        tid = request.GET.get('tid', '')
        cid = request.GET.get('cid', '')

        q = request.GET.get('q')

        if q:
            articles = Articles.objects.filter(Q(title__icontains=q))

        if cid:
            category_obj = Classify.objects.get(pk=int(cid))
            articles = category_obj.articles_set.all()

        # ===分页===
        paginator = Paginator(articles, 6)
        page_number = request.GET.get('page', '1')
        try:
            page_obj = paginator.page(page_number)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)

        return render(request, 'index.html', {'articles': articles_title,
                                              'page_obj': page_obj,
                                              'page': page_number,
                                              'classify': classify,
                                              'tid': tid,
                                              'cid': cid
                                              })


class About(View):
    def get(self, request):
        return render(request, 'apply/about.html')


class Apply(View):
    def get(self, request):
        return render(request, 'apply/apply.html')
