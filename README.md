# django-simple-csp

A simple Middleware for adding CSP headers and nonces in Django

## Usage

TODO

## Config Values

CSP_REPORT_URL = ""
The URl CSP errors should be reportet to, set to "" if not used, or do not define it.

CSP_REPORT_ONLY = True
Set the header to just report CSP errors do not enforce the CSP. Defaults to True.