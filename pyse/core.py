from sys import stdin

def line_remove_newline(line):
    return line.replace('\r', '').replace('\n', '')

def run_normal(pre, script, post):
    exec(pre)

    no = 1
    for line in stdin:
        line = line_remove_newline(line)
        exec(script)
        no = no + 1
    
    exec(post)

def run_function(script):
    # pre()
    # post(no)
    # each(line, no)
    exec(script)
    
    try:
        pre
        pre()
    except NameError:
        pass
        
    no = 1
    for line in stdin:
        line = line_remove_newline(line)
        each(line, no)
        no = no + 1
    
    try:
        post
        post(no)
    except NameError:
        pass

def run_module(mod_name, args):
    import pyse.ext 
    pyse.ext.load_modules()
    if mod_name in pyse.ext.Modules:
        pyse.ext.Modules[mod_name](stdin, args)
