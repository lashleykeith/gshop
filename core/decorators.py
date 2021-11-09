from django.shortcuts import redirect

def is_request_get(url):
	def redirected(view_func):
		def wrapper(request, *args, **kwargs):
			if not request.GET:
				return redirect(url)
			return view_func(request, *args, **kwargs)
		return wrapper
	return redirected


def is_request_post(url):
	def redirected(view_func):
		def wrapper(request, *args, **kwargs):
			if not request.POST:
				return redirect(url)
			return view_func(request, *args, **kwargs)
		return wrapper
	return redirected



def is_admin(view_func):
	def wrapper(request, *args, **kwargs):
		if request.user.is_superuser:
			return view_func(request, *args, **kwargs)
		else:
			return redirect('accounts:login')
	return wrapper


def is_teacher(view_func):
	def wrapper(request, *args, **kwargs):
		if request.user.is_staff and not request.user.is_superuser:
			return view_func(request, *args, **kwargs)
		else:
			return redirect('accounts:login')
	return wrapper


def is_student(view_func):
	def wrapper(request, *args, **kwargs):
		if not request.user.is_superuser and not request.user.is_staff:
			return view_func(request, *args, **kwargs)
		else:
			return redirect('accounts:login')
	return wrapper