"""This file contains responses to be sent to user"""
from django.http import JsonResponse


def success(content, msg="Success", page=None):
    """This api contains success response"""
    res = {"status": 200, 'message': msg}
    if page is None:
        data = {"response": res, "content": content}
    else:
        data = {"response": res, "content": content, "page": page}
    response = JsonResponse(data, safe=False, status=200)
    return response


def invalid(msg="Invalid Input"):
    """This api contains invalid input response"""
    res = {"status": 400, 'message': msg}
    data = {"response": res}
    response = JsonResponse(data, safe=False, status=400)
    return response


def server_error(msg="Internal Server Error", error=None):
    """This api contains the internal server error response"""
    res = {"status": 500, 'message': msg}
    data = {"response": res, "error": error}
    response = JsonResponse(data, safe=False, status=500)
    return response


def unauthorized(msg="unauthorized"):
    """This api contains response unauthorized user login"""
    res = {"status": 401, 'message': msg}
    data = {"response": res}
    response = JsonResponse(data, safe=False, status=401)
    return response


def expired(msg="Session Expired, Please login again"):
    """This api contains session expired response"""
    res = {"status": 440, 'message': msg}
    data = {"response": res}
    response = JsonResponse(data, safe=False, status=440)
    return response
