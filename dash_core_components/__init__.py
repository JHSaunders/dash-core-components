"""This package provides the core React component suite for Dash."""

from __future__ import print_function as _

import os as _os
import sys as _sys
import dash as _dash
import json

from .version import __version__

# Module imports trigger a dash.development import, need to check this first
if not hasattr(_dash, 'development'):
    print("Dash was not successfully imported. Make sure you don't have a file "
          "named \n'dash.py' in your current directory.", file=_sys.stderr)
    _sys.exit(1)

# Must update to dash>=0.23.1 to use this version of dash-core-components
if not hasattr(_dash.development.base_component, '_explicitize_args'):
    print("Please update the `dash` module to >= 0.23.1 to use this "
          "version of dash_core_components.\n"
          "You are using version {:s}".format(_dash.version.__version__),
          file=_sys.stderr)
    _sys.exit(1)


from ._imports_ import *
from ._imports_ import __all__


_current_path = _os.path.dirname(_os.path.abspath(__file__))

_this_module = _sys.modules[__name__]

_basepath = _os.path.dirname(__file__)
_filepath = _os.path.abspath(_os.path.join(_basepath, 'package.json'))
with open(_filepath) as f:
    package = json.load(f)

js_package_name = package['name']
py_package_name = __name__
js_version = package['version']

_js_dist = [
    {
        'external_url': 'https://cdn.plot.ly/plotly-1.42.2.min.js',
        'relative_package_path': 'plotly-1.42.2.min.js',
        'namespace': 'dash_core_components'
    },
    {
        'relative_package_path': '{}.min.js'.format(py_package_name),
        'dev_package_path': '{}.dev.js'.format(py_package_name),
        'external_url': (
            'https://unpkg.com/{}@{}/{}/{}.min.js'
        ).format(js_package_name, js_version, py_package_name, py_package_name),
        'namespace': py_package_name
    },
    {
        'relative_package_path': '{}.min.js.map'.format(py_package_name),
        'dev_package_path': '{}.dev.js.map'.format(py_package_name),
        'external_url': (
            'https://unpkg.com/{}@{}/{}/{}.min.js.map'
        ).format(js_package_name, js_version, py_package_name, py_package_name),
        'namespace': py_package_name,
        'dynamic': True
    }
]

for _component in __all__:
    setattr(locals()[_component], '_js_dist', _js_dist)
