from django.shortcuts import render
from django.views.generic.base import View
from .models import Cat_eye
import re
from pyecharts.charts import Bar, Pie
from pyecharts import options as opts


#

class Cat(View):

    def __init__(self):
        self.movieName = {}
        self.sumBoxInfo = []
        self.boxRate = []

    def get(self, request):
        cat = Cat_eye.objects.using('spider').all()

        for i in cat:
            self.movieName[i.movieName] = i.sumBoxInfo
            self.sumBoxInfo.append(self._num(i.sumBoxInfo))
            self.boxRate.append(self._float_num(i.boxRate))

        c = (
            Pie()
                .add("",
                     [list(z) for z in zip([name for name in self.movieName][:6], [val for val in self.boxRate][:6])])
                .set_global_opts(title_opts=opts.TitleOpts(title="排片场次"))
                .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
        )
        print(c)
        return render(request, 'apply/cat/cat.html', {'cat': cat, 'pie': c.render_embed()})

    def _num(self, arry):

        arry = re.findall(r'(\d+\.?\d*)([\u4E00-\u9FA5])', arry)[0]
        if arry[1] == '万':
            arry = float(arry[0]) * 10000
        elif arry[1] == '亿':
            arry = float(arry[0]) * 100000000

        return arry

    def _float_num(self, arry):
        arry = float(re.findall(r'(\d+\.?\d*)', arry)[0])
        return arry
