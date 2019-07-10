from .models import QuanJi
from django.shortcuts import render
from django.views.generic import View


class QuanJi_movie(View):
    def get(self, request):
        quanji = QuanJi.objects.using('spider').all()
        return render(request, 'apply/quanji/quanji.html', {'quanji': quanji})
