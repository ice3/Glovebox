"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['Glovebox.py']
DATA_FILES = ['glovebox', 'behaviors', 'libglovebox.so', 'camera.cal', 'data']
OPTIONS = {'argv_emulation': True, 'plist': {'LSArchitecturePriority': ['i386'] }}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)