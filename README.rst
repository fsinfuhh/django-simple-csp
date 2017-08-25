django-simple-csp
=================

A simple Middleware for adding CSP headers and nonces in Django

Usage
=====

Requires Django >=1.10

Add it to MIDDLEWARE not MIDDLEWARE_CLASSES
TODO: discribe in more detail


CSS
---

TODO: remove hash from the name of tag?

Example use of hashed inline style::

    {% load csp %}
    {% csp_css_hash %}
        td.style-class {
            background-color: red;
        }
    {% end_csp_css_hash %}

usage inside of style="..." attributes is not supported by chromium for now.

Javascript
----------

Nonces
~~~~~~

TODO: Change to hashes?

Example::

    {% load csp %}
    <script nonce={% csp_js_nonce %}>
        alert("bla")
    </script>


Config Values
-------------

CSP_REPORT_URL = ""
The URl CSP errors should be reportet to, set to "" if not used, or do not define it.

CSP_REPORT_ONLY = True
Set the header to just report CSP errors do not enforce the CSP. Defaults to True.
