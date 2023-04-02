from django.shortcuts import render
import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User, UserDetails


# Create your views here.


@csrf_exempt
def user(request):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        u_data = User(id=body["id"], email=body["email"])
        u_data.save()
        b = UserDetails(user=u_data, name=body["name"])
        b.save()
        return HttpResponse("Successfully Uploaded")


@csrf_exempt
def user_data(request):
    if request.method == "GET":
        user_detail = UserDetails.objects.all().select_related('user')
        result = []
        for u in user_detail:
            email = u.user.email
            name = u.name
            a = {"email": email, "name": name}
            result.append(a)
        return JsonResponse(result, safe=False)
