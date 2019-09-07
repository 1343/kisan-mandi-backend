import json

from django.contrib.gis.geos import Point
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from common import responses, views
from user.models import User


@csrf_exempt
def login(request):
    data = json.loads(request.body.decode('utf-8'))
    errors = views.validate(data, {"phone": "NNULL|TYPEstr"})
    if errors:
        return responses.invalid(errors)
    user = User.objects.filter(phone=data["phone"])
    if user:
        user = User.objects.get(phone=data["phone"])
        is_profile_complete = True
    else:
        user = User.objects.create(phone=data["phone"])
        is_profile_complete = False
    content = {
        "user_id": user.id,
        "name": user.name,
        "is_profile_complete": is_profile_complete
    }
    return responses.success(content)


@csrf_exempt
def update_user(request, user_id):
    if request.method == "PUT":
        data = json.loads(request.body.decode('utf-8'))
        errors = views.validate(data, {"name": "NNULL|TYPEstr", "user_type": "NNULL|TYPEstr",
                                       "latitude": "NNULL", "longitude": "NNULL"})
        if errors:
            return responses.invalid(errors)
        user = User.objects.filter(id=user_id).all()
        if not user:
            return responses.invalid("Invalid user id")
        User.objects.filter(id=user_id).update(name=data["name"], user_type=data["user_type"],
                                               latitude=data["latitude"], longitude=data["longitude"])
        return responses.success({
            "id": user[0].id,
            "name": data["name"],
            "user_type": data["user_type"],
            "latitude": data["latitude"],
            "longitude": data["longitude"],
            "phone": user[0].phone
        })
    return responses.invalid("Invalid method type")


def response_object(users, user_id=None):
    result = []
    for usr in users:
        result.append({
            "id": usr.id,
            "name": usr.name,
            "phone": usr.phone,
            "user_type": usr.user_type,
            "latitude": usr.latitude,
            "longitude": usr.longitude
        })
    # if user_id is None or user_id == "":
    return result
    # else:
    #     return result[0]


def get_user(request, user_id=None):
    if request.method == "GET":
        if user_id is not None and not user_id == "":
            user = User.objects.filter(id=user_id).all()
        else:
            user = User.objects.all()
        return responses.success(response_object(user, user_id))
    return responses.invalid("Invalid method type")


def get_merchants(request):
    if request.method == "GET":
        user = User.objects.filter(user_type="merchant").all()
        return responses.success(response_object(user))
    return responses.invalid("Invalid method type")
