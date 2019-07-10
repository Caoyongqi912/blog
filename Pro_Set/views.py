from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View

from Pro_Set.models import Set
from User.models import User


class SetView(View):
    def get(self, request):
        user = User.objects.all()
        set = Set.objects.all()
        return render(request, 'apply/product/set/set.html', {'user': user, 'set': set})