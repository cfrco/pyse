
Modules = dict()

def pyse_module(name):
    def decorator(function):
        Modules[name] = function

        return function

    return decorator

import pkgutil

def load_modules():
    for importer, modname, ispkg in pkgutil.iter_modules(__path__, __name__+"."):
        m = importer.find_module(modname).load_module(modname)
