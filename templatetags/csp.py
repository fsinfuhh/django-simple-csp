import hashlib
from base64 import b64encode

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


@register.simple_tag(name='csp_css_hash', takes_context=True)
def csp_scc_hash(context, *args):
    css = ''.join(args).encode('utf-8')
    css_hash = "sha256-{}".format(b64encode(hashlib.sha256(css).digest()).decode('utf-8'))
    if hasattr(context, 'request'):
        request = context['request']
        if not hasattr(request, 'csp_css_hashes'):
            request.csp_css_hashes = []
        if css_hash not in request.csp_css_hashes:
            request.csp_css_hashes.append(css_hash)
    return css
