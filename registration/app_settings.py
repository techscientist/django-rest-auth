from django.conf import settings

from registration.serializers import (
    RegisterSerializer as DefaultRegisterSerializer)
from ..utils import import_callable


serializers = getattr(settings, 'REST_AUTH_REGISTER_SERIALIZERS', {})

RegisterSerializer = import_callable(
    serializers.get('REGISTER_SERIALIZER', DefaultRegisterSerializer))
