import pyse.ext as ext
import pkgutil

def load_ext_modules():
    pkg = ext
    for importer, modname, ispkg in pkgutil.iter_modules(pkg.__path__, prefix=pkg.__name__+"."):
        m = importer.find_module(modname).load_module(modname)
