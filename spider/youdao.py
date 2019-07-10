from datetime import datetime
import hashlib
import json
import random
import re
import time
import urllib.request
import urllib.parse
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View
from .spider_setting import Base_spider

class You(View):
    def get(self, request):
        return render(request, 'apply/spider/youdao_spider.html')


class YouDao(View):

    def post(self, request):
        d = request.POST.get('msg_input')



        now = datetime.now()
        now = now.timestamp()
        print(now)
        a = re.match(r'(\d+)\.(\d+)', str(now))
        b = a.group(1) + a.group(2)
        f = b[:13]  # 时间戳前13位

        c = "rY0D^0'nM0}g5Mm1z%1G4"
        u = 'fanyideskweb'

        creatmd5 = u + d + f + c

        # 生成md5
        md5 = hashlib.md5()
        md5.update(creatmd5.encode('utf-8'))
        sign = md5.hexdigest()

        url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&sessionFrom='

        data = {}
        data['i'] = d
        data['from'] = 'AUTO'
        data['to'] = 'AUTO'
        data['smartresult'] = 'dict'
        data['client'] = 'fanyideskweb'
        data['salt'] = f
        data['sign'] = sign
        data['doctype'] = 'json'
        data['version'] = '2.1'
        data['keyfrom'] = 'fanyi.web'
        data['action'] = 'FY_BY_CLICKBUTTION'
        data['typoResult'] = 'true'

        data = urllib.parse.urlencode(data).encode('utf-8')

        req = urllib.request.Request(url=url, data=data, method='POST', headers=Base_spider().ua())
        response = urllib.request.urlopen(req)
        translateResult = response.read().decode('utf-8')
        res = json.loads(translateResult)
        if res.get('errorCode') != 0:
            data = {'status': 'err'}
            return JsonResponse(data)

        res_for_english = res['translateResult'][0][0]['tgt']
        res_for_chinese = res['translateResult'][0][0]['src']

        data = {
            'output_for_C': res_for_chinese,
            'output_for_e': res_for_english,

        }
        return JsonResponse(data)
