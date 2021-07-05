from django import http
from django.utils.http import urlquote
from django import urls
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin

# gregbrown.co.nz/code/append-or-remove-slash/
class AppendOrRemoveSlashMiddleware(MiddlewareMixin):
    def process_request(self, request):
        urlconf = getattr(request, 'urlconf', None)
        if not self.is_valid_path(request.path_info, urlconf):
            if request.path_info.endswith('/'):
                new_path = request.path_info[:-1]
            else:
                new_path = request.path_info + '/'

            if self.is_valid_path(new_path, urlconf):
                return http.HttpResponsePermanentRedirect(
                    self.generate_url(request, new_path))

    def process_response(self, request, response):
        if response.status_code == 404:
            if not request.path_info.endswith('/') and settings.APPEND_SLASH:
                new_path = request.path_info + '/'
            elif request.path_info.endswith('/') and not settings.APPEND_SLASH:
                new_path = request.path_info[:-1]
            else:
                new_path = None

            if new_path:
                urlconf = getattr(request, 'urlconf', None)
                if self.is_valid_path(new_path, urlconf):
                    return http.HttpResponsePermanentRedirect(
                        self.generate_url(request, new_path))
        return response

    def generate_url(self, request, path):
            if request.get_host():
                new_url = "%s://%s%s" % (request.is_secure() and 'https' or 'http',
                                        request.get_host(),
                                        urlquote(path))
            else:
                new_url = urlquote(path)
            if request.GET:
                new_url += '?' + request.META['QUERY_STRING']
            return new_url

    def is_valid_path(self, path, urlconf=None):
        try:
            urls.resolve(path, urlconf)
            return True
        except urls.Resolver404:
            return False
