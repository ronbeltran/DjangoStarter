
from django.conf import settings

def context_variables(request):
    return {
        'settings': settings,
    }   

