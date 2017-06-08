from django.conf import settings


class CSPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        policy = {
            'default-src': ["'self'"],
            'img-src': ["'self'", "data:"],
            'script-src': ["'self'"]
        }
        if hasattr(request, 'csp_nonces'):
            policy['script-src'] += ["'nonce-{}'".format(nonce) for nonce in request.csp_nonces]

        # Allow inline styles for Django's builtin 403/404/500 pages
        # (which are only shown in DEBUG mode anyway)
        if settings.DEBUG and response.status_code in (403, 404, 500):
            policy['script-src'].append("'unsafe-inline'")
            policy['style-src'] = ["'self'", "'unsafe-inline'"]

        if settings.get('CSP_REPORT_URL', ""):
            policy['report-uri'] = [settings["CSP_REPORT_URL"]]

        policy_strings = []
        for kind, allowed in policy.items():
            policy_strings.append('{} {}'.format(kind, ' '.join(allowed)))

        if settings.get('CSP_REPORT_ONLY', True):
            response['Content-Security-Policy-Report-Only'] = '; '.join(policy_strings)
        else:
            response['Content-Security-Policy'] = '; '.join(policy_strings)

        return response
