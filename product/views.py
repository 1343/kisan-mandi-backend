import json

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from common import responses
from product.models import Product


@csrf_exempt
def route(request, prod_id=None):
    """This api acts as a router to call other api"""
    if request.method == 'POST':
        return post(request)
    if request.method == 'GET':
        return get(request)
    if request.method == 'PATCH':
        return patch(request, prod_id)
    if request.method == 'DELETE':
        return delete(prod_id)
    return responses.invalid("Invalid method type")


@csrf_exempt
def post(request):
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        prod = Product.objects.create(name=data["name"], description=data["description"],
                                      product_type=data["product_type"],
                                      longitude=data["longitude"], latitude=data["latitude"], location=data["location"],
                                      image=data["image"], user_id=data["user_id"])
        return responses.success({
            "id": prod.id,
            "name": prod.name,
            "description": prod.description,
            "product_type": prod.product_type,
            "longitude": prod.longitude,
            "latitude": prod.latitude,
            "location": prod.location,
            "image": prod.image,
            "user_id": prod.user_id,
            "status": prod.status
        })
    return responses.invalid("Invalid method type")


def get(request, prod_id=None):
    if request.method == "GET":
        if prod_id is not None and not prod_id == "":
            product = Product.objects.filter(id=prod_id).all()
        else:
            product = Product.objects.all()
        result = []
        for prod in product:
            result.append({
                "id": prod.id,
                "name": prod.name,
                "description": prod.description,
                "product_type": prod.product_type,
                "longitude": prod.longitude,
                "latitude": prod.latitude,
                "location": prod.location,
                "image": prod.image,
                "user_id": prod.user_id,
                "status": prod.status
            })
        return responses.success(result)
    return responses.invalid("Invalid method type")


@csrf_exempt
def patch(request, prod_id=None):
    if request.method == "PATCH":
        data = json.loads(request.body.decode('utf-8'))
        prod = Product.objects.filter(id=prod_id)
        if not prod:
            return responses.invalid("Invalid product id")
        for key in data.keys():
            if key == "status":
                Product.objects.filter(id=prod_id).update(status=data["status"])
        return responses.success("")
    return responses.invalid("Invalid method type")


def delete(request, prod_id=None):
    if request.method == "DELETE":
        Product.objects.filter(id=prod_id).delete()
        return responses.success("")
    return responses.invalid("Invalid method type")
