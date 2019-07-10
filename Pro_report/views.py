from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View

from Pro_Api.models import ApiTest, Apis
from Product.models import Product


class Report(View):
    def get(self, request):
        apis_list = Apis.objects.all()
        apis_count = Apis.objects.all().count()
        apis_pass_count = len(Apis.objects.filter(api_status=True))
        apis_fail_count = apis_count - apis_pass_count
        content = {
            'apis_list': apis_list,
            'apis_count': apis_count,
            'apis_pass_count': apis_pass_count,
            'apis_fail_count': apis_fail_count

        }
        return render(request, 'apply/product/report/report.html', content)


class ApiReprot(View):
    def get(self, request, pid):
        api_list = ApiTest.objects.get(pk=pid)
        api_count = ApiTest.objects.get(pk=pid).count()
        print('api_count', api_count)
        api_pass_count = ApiTest.objects.filter(api_test_res=True).count()
        api_fail_count = api_count - api_pass_count
        data = {
            'api_list': api_list,
            'api_count': api_count,
            'api_pass_count': api_pass_count,
            'api_fail_count': api_fail_count,
        }
        return render(request, 'apply/product/api/api_report.html', data)
