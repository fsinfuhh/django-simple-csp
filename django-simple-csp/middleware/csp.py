from django.conf import settings


class CSPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        policy = {
            'default-src': ["'self'"],
            'img-src': ["'self'", "data:"],
            'script-src': ["'self'"],
            'style-src': ["'self'"],
        }
        if hasattr(request, 'csp_js_nonces'):
            policy['script-src'] += ["'nonce-{}'".format(nonce) for nonce in request.csp_js_nonces]

        if hasattr(request, 'csp_css_hashes'):
            policy['style-src'] += ["'{}'".format(css_hash) for css_hash in request.csp_css_hashes]

        # Allow inline styles for Django's builtin 403/404/500 pages
        # (which are only shown in DEBUG mode anyway)
        if settings.DEBUG and response.status_code in (403, 404, 500):
            policy['script-src'].append("'unsafe-inline'")
            policy['style-src'].append("'unsafe-inline'")

        if settings.CSP_REPORT_URL:
            policy['report-uri'] = [settings.CSP_REPORT_URL]

        policy_strings = []
        for kind, allowed in policy.items():
            policy_strings.append('{} {}'.format(kind, ' '.join(allowed)))

        if settings.CSP_REPORT_ONLY:
            response['Content-Security-Policy-Report-Only'] = '; '.join(policy_strings)
        else:
            response['Content-Security-Policy'] = '; '.join(policy_strings)

        return response
