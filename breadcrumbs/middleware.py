# -*- coding: utf-8 -*-
from .breadcrumbs import Breadcrumbs

class BreadcrumbsMiddleware(object):

    def process_request(self,request):
        request.breadcrumbs = Breadcrumbs()
        request.breadcrumbs._clean(request.site['name'].title() if getattr(request, 'site', None) else 'Home')
        return None