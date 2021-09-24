import importlib


def _get_module(module_name):
    return importlib.import_module(module_name)


def _get_object(module, path_in_module):
    obj = module
    for path in path_in_module:
        obj = getattr(obj, path)
    return obj

def _get_object_from_path(path: str):
    subpaths = path.split(".")

    module = _get_module(subpaths[0])
    return _get_object(module, subpaths[1:])


def get(path: str):
    obj = _get_object_from_path(path)
    if not callable(obj):
        raise ImportError("Object at path not callable")
    return obj