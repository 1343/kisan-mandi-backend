import json

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from common import responses, views
from product.models import Product, ProductType
from user.models import User


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
        return delete(request, prod_id)
    return responses.invalid("Invalid method type")


@csrf_exempt
def post(request):
    try:
        if request.method == "POST":
            data = json.loads(request.body.decode('utf-8'))
            # errors = views.validate(data, {"name": "NNULL|TYPEstr", "description": "NNULL|TYPEstr",
            #                                "product_type": "NNULL|TYPEstr",
            #                                "latitude": "NNULL", "longitude": "NNULL",
            #                                "location": "NNULL|TYPEstr", "image": "NNULL|TYPEstr",
            #                                "user_id": "NNULL|TYPEint", "price": "NNULL"})
            # if errors:
            #     return responses.invalid(errors)
            User.objects.get(id=data["user_id"])
            product_type = data["product_type"]
            product = ProductType.objects.filter(id=product_type)
            if not product:
                return responses.invalid("Invalid Product Type")
            product_name = product[0].name
            try:
                latitude = data["latitude"]
            except KeyError:
                latitude = 0.000
            try:
                longitude = data["longitude"]
            except KeyError:
                longitude = 0.000
            try:
                location = data["location"]
            except KeyError:
                location = ""
            try:
                image = data["image"]
            except KeyError:
                image = ""
            prod = Product.objects.create(name=data["name"], description=data["description"],
                                          product_type=product[0],
                                          longitude=longitude, latitude=latitude,
                                          location=location,
                                          image=image, user_id=data["user_id"],
                                          price=data["price"])
            return responses.success({
                "id": prod.id,
                "name": prod.name,
                "description": prod.description,
                "product_type": product_name,
                "longitude": prod.longitude,
                "latitude": prod.latitude,
                "location": prod.location,
                "image": prod.image,
                "price": prod.price,
                "user_id": prod.user_id,
                "status": prod.status
            })
        return responses.invalid("Invalid method type")
    except User.DoesNotExist:
        return responses.invalid("Invalid user id")


def get(request, prod_id=None):
    if request.method == "GET":
        if prod_id is not None and not prod_id == "":
            product = Product.objects.filter(id=prod_id).all()
        else:
            created_by = request.GET.get("created_by", None)
            if created_by is None or created_by == "":
                product = Product.objects.select_related('product_type').all()
            else:
                product = Product.objects.select_related('product_type').filter(user_id=created_by).all()
        result = []
        for prod in product:
            user = User.objects.get(id=prod.user_id)
            result.append({
                "id": prod.id,
                "name": prod.name,
                "description": prod.description,
                "product_type": prod.product_type.name,
                "longitude": prod.longitude,
                "latitude": prod.latitude,
                "location": prod.location,
                "image": prod.image,
                "price": prod.price,
                "user_id": prod.user_id,
                "user_name": user.name,
                "status": prod.status
            })
        return responses.success(result)
    return responses.invalid("Invalid method type")


@csrf_exempt
def patch(request, prod_id=None):
    if request.method == "PATCH":
        data = json.loads(request.body.decode('utf-8'))
        if prod_id is None and not prod_id == " ":
            return responses.invalid("Please provide id")
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


def get_product_type(request):
    if request.method == "GET":
        prod_type = ProductType.objects.all()
        result = []
        for pt in prod_type:
            result.append({
                "id": pt.id,
                "name": pt.name
            })
        return responses.success(result)
    return responses.invalid("Invalid method type")


@csrf_exempt
def add_product_type(request):
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        prod_type = ProductType.objects.create(name=data["name"])
        return responses.success({"id": prod_type.id})
    return responses.invalid("Invalid method type")
