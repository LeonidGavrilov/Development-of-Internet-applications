from django.shortcuts import render

# Create your views here.

from django.views.generic.base import View
from .models import Seller


class SellerView(View):
    def get(self, request):
        sellers = Seller.objects.all()
        return render(request, "shop_list.html", {"shop_list": sellers})
