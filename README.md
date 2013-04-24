curry.py 
========

Curried callables in Python!

### What?

Curried functions accept arguments one-by-one, instead of all in a single call. Some more functional languages provide more facilities for curried functions, but they have been missing in Python. If you've ever used `functools.partial`, it's similar, but more potent. 

### How?

The `curried` function (also usable as a decorator) curries a function over the number of arguments it requires (which do not specify defaults). Optional arguments can be passed at any point in curried application as keywords.

	>>> @curried
	... def add(x, y, z=0):
	...     return x + y + z

	>>> add(4)(5)
	9
	>>> add(4, z=3)(5)
	12

Curried functions that accept a variable number of arguments (i.e. `*args`) need to be terminated by an empty call

	>>> @curried
	... def add_all(*nums):
	...     return reduce(lambda x,y: x+y, nums)

	>>> add_all(1)(2)(3)(4)()
	10

Best of all, curried functions that don't accept variable positional arguments (`*args`) can be treated **exactly** as if they were normal functions! 

Even with functions decorated with `@curried`, you need not treat them differently than if they were defined as normal functions, unless you *want* them to curry arguments. No need to worry about surprising or confusing colleagues!

	>>> add(10, 20)
	30
	>>> add(10, 20, 30)
	60
	>>> add(10, 20, 30, 40)
	Traceback (most recent call last):
	  File "<input>", line 1, in <module>
	  File "curry.py", line 32, in curried_func
	    return accum_curry(args, kwargs)
	  File "curry.py", line 26, in accum_curry
	    return func(*accum_args, **accum_kwargs)
	TypeError: add() takes at most 3 arguments (4 given)

### Installation

Currently not uploaded to pypi, or even much of a package. The module's a single file with only two functions, so if you want to play around with it, drop it in as-is, and let me know what you think [@ryanartecona](http://twitter.com/ryanartecona)!