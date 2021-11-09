from django.shortcuts import redirect


def is_request_get(view_func):
	def wrapper(request, *args, **kwargs):
		if request.GET:
			return view_func(request, *args, **kwargs)
		else:
			return redirect('core:home')
	return wrapper


def is_request_post(view_func):
	def wrapper(request, *args, **kwargs):
		if request.POST:
			return view_func(request, *args, **kwargs)
		else:
			return redirect('core:home')
	return wrapper