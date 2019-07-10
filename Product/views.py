from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.generic.base import View

from Product.models import Product


class ProductView(View):
    def get(self, request):
        if request.user.is_authenticated:

            product = Product.objects.all()
            return render(request, 'apply/product/product.html', {'pro': product})
        else:
            next = request.GET.get('next', '')
            return render(request, 'user/login.html', {'next': next})





class Del_pro(View):
    def get(self, request):
        pid = request.GET.get('pid', '')
        if request.user.is_superuser:
            Product.objects.get(pk=pid).delete()
            return redirect(reverse('product:pro_detail'))
        else:
            return JsonResponse({'status': 'fail'})





class Detail(View):
    def get(self,request,pid):
        product = Product.objects.get(pk=pid)
        return render(request,'apply/product/product_detail.html',{'product':product})

