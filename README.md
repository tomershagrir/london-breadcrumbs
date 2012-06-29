## london-breadcrumbs app for London framework

Is a ported version of django-breadcrumbs by chronossc
from https://github.com/chronossc/django-breadcrumbs/

### How to use it:

1. Install it 
2. Add it to INSTALLED_APPS

	INSTALLED_APPS = {
		...
		'breadcrumbs': 'breadcrumbs'
	}
	
3. Make sure that 'london.templates.context_processors.request' is in TEMPLATE_CONTEXT_PROCESSORS

	TEMPLATE_CONTEXT_PROCESSORS = (
		...
		'london.templates.context_processors.request',
		...
	)

4. Add breadcrumbs.middleware.BreadcrumbsMiddleware to your MIDDLEWARE_CLASSES

    MIDDLEWARE_CLASSES = (
    	...
        'breadcrumbs.middleware.BreadcrumbsMiddleware',
        ...
    )

### How to add breadcrumbs:

	# one by one
	request.breadcrumbs( name, url )
	
	# various tuples/lists
	request.breadcrumbs( ( (name1, url1), (name2, url2), (name3, url3), ...,) )
	request.breadcrumbs( [ [name1, url1], [name2, url2], [name3, url3], ...] )
	
	# objects with attributes name and url in list / tuple format:
	request.breadcrumbs( ( obj1, obj2, obj3, obj4, ......) )
	request.breadcrumbs( [ obj1, obj2, obj3, obj4, ......] )
	
### How to use them in templates

	{% for breadcrumb in request.breadcrumbs %}
	<a href="{{ breadcrumb.url }}">{{ breadcrumb.name }}</a>{% if not forloop.last %} >> {% endif %}
	{% endfor %}
	
### Options

	BREADCRUMBS_AUTO_HOME: defaults to False, If True, breadcrumbs add as first Breadcrumb in list ("Home",u"/")
	BREADCRUMBS_HOME_TITLE: defaults to u'Home'
	



