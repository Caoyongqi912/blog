from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View

from Pro_Web.models import WebCase, WebCaseStep
from Product.models import Product


class WebCaseView(View):
    def get(self, request, pid):
        product = Product.objects.get(pk=pid)
        web_case = WebCase.objects.filter(product=product)
        return render(request, 'apply/product/web/web_case.html', {'web_case': web_case})


class WebCaseStepView(View):
    def get(self, request, web_id):
        web_case = WebCase.objects.get(pk=web_id)
        web_step = WebCaseStep.objects.filter(web_case=web_case)
        return render(request, 'apply/product/web/web_case_step.html', {'web_step': web_step})
