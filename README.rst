django-simple-csp
=================

A simple Middleware for adding CSP headers and nonces in Django

Usage
=====

Requires Django >=1.10

Add it to the INSTALLED_APPS settings variable::

    INSTALLED_APPS = [
        ...
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        ...
        'django-simple-csp'
        ...
    ]


Add it to MIDDLEWARE (not MIDDLEWARE_CLASSES)::

    MIDDLEWARE = [
        ...
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        ...
        'django-simple-csp.middleware.csp.CSPMiddleware',
        ...
    ]



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
