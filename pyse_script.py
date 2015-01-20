#!/usr/bin/python

"""
    An quite easy stream editor based on python.
"""

import argparse
import os
import pyse

def init_arg():
    parser = argparse.ArgumentParser()
    parser.add_argument('script', type=str, nargs='*')
    parser.add_argument('-f', type=str, dest='file', default=None)
    parser.add_argument('-F', action='store_true', dest='function_mode')
    
    parser.add_argument('-m', type=str, dest='module', default=None)
    
    parser.add_argument('--pre', type=str, nargs='+', dest='pre', default='')
    parser.add_argument('--post', type=str, nargs='+', dest='post', default='')
    parser.add_argument('--each', type=str, nargs='+', dest='each', default='')

    return parser

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

    if args.module != None:
        modargs = args.module.split(",")
        pyse.run_module(modargs[0], modargs[1:])
    elif args.function_mode:
        pyse.run_function(script)
    else:
        pyse.run_normal(pre_script, script, post_script)

if __name__ == '__main__':
    main()
