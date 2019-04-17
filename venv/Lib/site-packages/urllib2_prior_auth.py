from base64 import standard_b64encode
try:
    from urllib.request import HTTPBasicAuthHandler
except ImportError:
    from urllib2 import HTTPBasicAuthHandler


class HTTPBasicPriorAuthHandler(HTTPBasicAuthHandler):
    handler_order = 400

    def http_request(self, req):
        if not req.has_header('Authorization'):
            if hasattr(req, 'get_host'):
                host = req.get_host()
            else:
                host = req.host
            user, passwd = self.passwd.find_user_password(None, host)
            credentials = '{0}:{1}'.format(user, passwd).encode()
            auth_str = standard_b64encode(credentials).decode()
            req.add_unredirected_header('Authorization',
                                        'Basic {}'.format(auth_str.strip()))
        return req

    https_request = http_request
