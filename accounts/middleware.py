import jwt
from django.shortcuts import redirect
from django.conf import settings

class JWTMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        exempt = ['/login/', '/logout/']
        if request.path not in exempt:
            token = request.COOKIES.get('jwt')
            if not token:
                return redirect('login')
            try:
                payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
                request.user_payload = payload
            except jwt.ExpiredSignatureError:
                return redirect('login')
            except jwt.InvalidTokenError:
                return redirect('login')
        return self.get_response(request)