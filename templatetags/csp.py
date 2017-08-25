import hashlib
from base64 import b64encode

from django import template
from django.utils.crypto import get_random_string


register = template.Library()


@register.simple_tag(name='csp_js_nonce', takes_context=True)
def csp_js_nonce(context=None):
    nonce = get_random_string(16)
    if hasattr(context, 'request'):
        request = context['request']
        if not hasattr(request, 'csp_js_nonces'):
            request.csp_js_nonces = []
        request.csp_js_nonces.append(nonce)
    return nonce


def csp_css_hash(parser, token):
    nodelist = parser.parse(('end_csp_css_hash',))
    parser.delete_first_token()
    return CspCssHash(nodelist)


class CspCssHash(template.Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist

    def render(self, context):
        css = self.nodelist.render(context)
        css_hash = "sha256-{}".format(b64encode(hashlib.sha256(css.encode()).digest()).decode())
        if hasattr(context, 'request'):
            request = context['request']
            if not hasattr(request, 'csp_css_hashes'):
                request.csp_css_hashes = set()
            request.csp_css_hashes.add(css_hash)
        return '<style type="text/css">{}</style>'.format(css)


register.tag('csp_css_hash', csp_css_hash)
