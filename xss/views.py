from django.shortcuts import render, HttpResponse, redirect
from django.template import loader
from django.http import JsonResponse
import jwt
from xssinjection import settings

# Create your views here.
def home(request):
    payload = {
        'user_id': 1,
        'role': 'user'
    }
    token = jwt.encode(payload, settings.SECRET_JWT_KEY, algorithm='HS256')
    response = render(request=request, template_name='index.html')
    response.set_cookie('jwt', token)
    return response

def xss_attack(request):
    template = loader.get_template("xss.html")
    context = {}
    token = request.COOKIES.get('jwt')
    payload = jwt.decode(token, settings.SECRET_JWT_KEY, algorithms=['HS256'])
    if payload.get('role') == 'admin':
        context['otp_mssg'] = 'b\'06123f20062d1f2a537a1e1837202b223023\''
    if request.method == 'POST':
        context['form_mssg'] = request.POST.get('xss','')
    response = HttpResponse(template.render(context, request))
    return response