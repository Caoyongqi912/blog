from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View

from Pro_App.models import AppCase, AppCaseStep
from Product.models import Product


class AppCaseView(View):
    def get(self, request, pid):
        product = Product.objects.get(pk=pid)
        appcase = AppCase.objects.filter(product=product)
        return render(request, 'apply/product/app/appcase.html', {'appcase': appcase})


class AppCaseStepView(View):
    def get(self, request,aid):
        appcase = AppCase.objects.get(pk=aid)
        appcasestep = AppCaseStep.objects.filter(appcase=appcase)
        return render(request, 'apply/product/app/appcasestep.html', {'appcasestep': appcasestep})
