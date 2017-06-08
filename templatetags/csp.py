from django import template
from django.utils.crypto import get_random_string


register = template.Library()


@register.simple_tag(name='csp_nonce', takes_context=True)
def csp_nonce(context=None):
    nonce = get_random_string(16)
    if hasattr(context, 'request'):
        request = context['request']
        if not hasattr(request, 'csp_nonces'):
            request.csp_nonces = []
        request.csp_nonces.append(nonce)
    return nonce
