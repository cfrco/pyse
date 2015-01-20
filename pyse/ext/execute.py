from pyse.core import line_remove_newline
from . import pyse_module
import os

@pyse_module("e")
def execute_line(instream, args):
    for line in instream:
        line = line_remove_newline(line)
        print line
        os.system(line)
