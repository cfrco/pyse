#!/usr/bin/python

"""
    An quite easy stream editor based on python.
"""

import argparse

from sys import stdin

def init_arg():
    parser = argparse.ArgumentParser()
    parser.add_argument('script', type=str, nargs='*')
    parser.add_argument('-f', type=str, dest='file', default=None)
    parser.add_argument('-F', action='store_true', dest='function_mode')

    parser.add_argument('--pre', type=str, nargs='+', dest='pre', default='')
    parser.add_argument('--post', type=str, nargs='+', dest='post', default='')
    parser.add_argument('--each', type=str, nargs='+', dest='each', default='')

    return parser

def line_remove_newline(line):
    return line.replace('\r', '').replace('\n', '')

def pyse_run_normal(pre, script, post):
    exec(pre)

    no = 1
    for line in stdin:
        line = line_remove_newline(line)
        exec(script)
        no = no + 1
    
    exec(post)

def pyse_run_function(script):
    # pre()
    # post(no)
    # each(line, no-1)
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
        post(no-1)
    except NameError:
        pass

def main():
    args = init_arg().parse_args()
    
    pre_script = ''
    post_script = ''
    if not args.file is None:
        script = open(args.file).read()
    else:
        pre_script = ' '.join(args.pre)
        post_script = ' '.join(args.post)
        each_script = ' '.join(args.each).strip()

        if not args.script is None:
            script = ' '.join(args.script)

        if each_script != "":
            script = each_script

    if args.function_mode:
        pyse_run_function(script)
    else:
        pyse_run_normal(pre_script, script, post_script)

if __name__ == '__main__':
    main()
