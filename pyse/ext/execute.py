from pyse.core import line_remove_newline
from . import pyse_module
import os

@pyse_module("e")
def execute_line(instream, args):

    # Echo
    echo = False
    if "echo" in set(args):
        echo = True
    
    for line in instream:
        line = line_remove_newline(line)
        if echo:
            print line
        os.system(line)
