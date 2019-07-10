from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View

from Pro_Api.models import ApiTest, ApiTestStep, Apis
from Product.models import Product


class Pro_Detail(View):
    def get(self, request, pid):
        if pid:
            product = Product.objects.get(pk=pid)
            apitest = ApiTest.objects.filter(product=product)

            return render(request, 'apply/product/api/api.html', {'api': apitest})


class Method(View):
    def get(self, request, aid):
        if aid:
            apitest = ApiTest.objects.get(pk=aid)
            method = ApiTestStep.objects.filter(api_test=apitest)
            return render(request, 'apply/product/api/api_method.html', {'method': method})



class ApisView(View):
    def get(self,request):
        usernaem = request.user.username
        apis = Apis.objects,all()
        return render(request,'apply/product/api/apis.html',{'username':usernaem,'apis':apis})