from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View

from Pro_Bug.models import Bug
from Product.models import Product


class BugView(View):
    def get(self, request, pid):
        product = Product.objects.get(pk=pid)
        bug = Bug.objects.filter(product=product)
        return render(request, 'apply/product/bug/bug.html', {'bug': bug})
