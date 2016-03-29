from __future__ import print_function
import sys


def _eprint(*args, **kwargs):
    kwargs['file'] = sys.stderr
    print(*args, **kwargs)


def output_demo(args, module):
    _eprint('Args:')
    _eprint(repr(args))
    _eprint()
    _eprint('Module:')
    _eprint(repr(module))
    sys.exit(0)
output_demo.pdoc_output_plugin = 'demo'
