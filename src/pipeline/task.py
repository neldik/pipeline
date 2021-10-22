from pipeline import locator
import functools


def _create_function(description):
    function = locator.get(description["name"])

    default_args = description.get("default_args", None)
    if default_args is not None:
        return functools.partial(function, **default_args)
    else:
        return function


def create_task(description):
    function = _create_function(description["function"])

    return function
