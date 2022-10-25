import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Ad, Category


def root(request):
    return JsonResponse({"result": "ok"})


@method_decorator(csrf_exempt, name="dispatch")
class AdListCreateView(View):
    def get(self, request):
        ads = Ad.objects.all()
        response = [
            {"id": ad.pk,
             "name": ad.name,
             "author": ad.author,
             "price": ad.price}
            for ad in ads
        ]
        return JsonResponse(response, safe=False)

    def post(self, request):
        data = json.loads(request.body)
        ad = Ad.objects.create(**data)
        return JsonResponse({
            "id": ad.pk,
            "name": ad.name,
            "author": ad.author,
            "price": ad.price,
            "description": ad.description,
            "address": ad.address,
            "is_published": ad.is_published
        }, safe=False)


@method_decorator(csrf_exempt, name="dispatch")
class CatListCreateView(View):
    def get(self, request):
        categories = Category.objects.all()
        response = [
            {"id": cat.pk,
             "name": cat.name}
            for cat in categories
        ]
        return JsonResponse(response, safe=False)

    def post(self, request):
        data = json.loads(request.body)
        cat = Category.objects.create(**data)
        return JsonResponse({
            "id": cat.pk,
            "name": cat.name
        }, safe=False)


class AdDetailView(DetailView):
    model = Ad

    def get(self, request, *args, **kwargs):
        ad = self.get_object()
        return JsonResponse({
            "id": ad.pk,
            "name": ad.name,
            "author": ad.author,
            "price": ad.price,
            "description": ad.description,
            "address": ad.address,
            "is_published": ad.is_published
        }, safe=False)


class CatDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        cat = self.get_object()
        return JsonResponse({
            "id": cat.pk,
            "name": cat.name,
        }, safe=False)
