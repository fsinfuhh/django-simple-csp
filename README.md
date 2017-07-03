# django-simple-csp

A simple Middleware for adding CSP headers and nonces in Django

## Usage

Requires Django >=1.10

Add it to MIDDLEWARE not MIDDLEWARE_CLASSES
TODO

### CSS

Example use of hashed inline style:

    {% load csp %}
    <style>{% scp_scc_hash %} /* have to be directly together, same as the closing tag, or else the hash is invalid */
        td.style-class {
            background-color: red;
        }
    {% end_scp_scc_hash %}</style>

usage inside of style="..." attributes is not supported by chromium for now.

### Javascript

#### Nonces

TODO: Change to hashes?

TODO: Change Name

Example:

    {% load csp %}
    <script nonce={% csp_nonce %}>
        alert("bla")
    </script>

## Config Values

CSP_REPORT_URL = ""
The URl CSP errors should be reportet to, set to "" if not used, or do not define it.

CSP_REPORT_ONLY = True
Set the header to just report CSP errors do not enforce the CSP. Defaults to True.