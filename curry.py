from functools import wraps
from inspect import getargspec


def curry_n(n, func=None):
	"""curry_n(n, func) returns a new function which takes any arguments,
	returning callables that take any arguments until n argumentss 
	have been applied. Accumulates kwargs until func is evaluated.

	>>> curried_max = curry_n(4, max)
	>>> curried_max(2)(3, 5)(4)
	5
	>>> @curry_n(2)
	... def add(x, y):
	...     return x + y

	>>> add3 = add(3)
	>>> add3(4)
	7
	"""
	def curry_func(func):
		def accum_curry(args, kwargs, accum_args=(), accum_kwargs={}):
			accum_args = accum_args + args
			accum_kwargs.update(kwargs)

			if not (args or kwargs) or len(accum_args) >= n:
				return func(*accum_args, **accum_kwargs)
			else:
				return wraps(func)(lambda *a, **kw: accum_curry(a, kw, accum_args, accum_kwargs))

		@wraps(func)
		def curried_func(*args, **kwargs):
			return accum_curry(args, kwargs)

		return curried_func

	return curry_func(func) if func else curry_func


def curried(func):
	"""Curries a function over the number of arguments it requires
	(which do not specify defaults). Optional arguments can be 
	passed at any point in curried application as keywords.

	>>> @curried
	... def add(x, y, z=0):
	...     return x + y + z

	>>> add(4)(5)
	9
	>>> add(4, z=3)(5)
	12

	Curried functions that accept a variable number of arguments 
	(i.e. `*args`) need to be terminated by an empty call

	>>> @curried
	... def add_all(*nums):
	...     return reduce(lambda x,y: x+y, nums)

	>>> add_all(1)(2)(3)(4)()
	10
	"""
	argspec = getargspec(func)
	num_defaults = len(argspec.defaults) if argspec.defaults else 0
	num_required = len(argspec.args) - num_defaults
	num_curried = float('inf') if argspec.varargs else num_required

	return curry_n(num_curried)(func)


if __name__=="__main__":
	import doctest
	doctest.testmod()