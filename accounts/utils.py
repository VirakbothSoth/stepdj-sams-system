import jwt
from datetime import datetime, timedelta, timezone
from django.conf import settings

def generate_token(user):
    now = datetime.now(timezone.utc)
    payload = {
        'user_id': user.id,
        'username': user.username,
        'token_type': 'access',
        'exp': now + timedelta(hours=24),
        'iat': now,
    }
    return jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

def decode_token(token):
    return jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])