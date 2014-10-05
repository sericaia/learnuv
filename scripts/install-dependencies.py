#!/usr/bin/env python

from subprocess import call
import os

script_dir = os.path.dirname(__file__)
root_dir   = os.path.join(os.path.abspath(script_dir), '..')
deps_dir   = os.path.join(root_dir, 'deps')
libuv_dir  = os.path.join(deps_dir, 'libuv')
build_dir  = os.path.join(root_dir, 'build')
gyp_dir    = os.path.join(build_dir, 'gyp')

def mkdirp(dir):
    try:
        os.mkdir(dir)
    except OSError:
        pass

def run(cmd):
    print '\033[0;32mlearnuv\033[0m executing: ' + cmd
    os.system(cmd)

# libuv
mkdirp(deps_dir)
## todo: This may not work with older git versions (http://stackoverflow.com/questions/20280726/how-to-git-clone-a-specific-tag)
run('git clone --depth 1 --branch v1.0.0-rc1 https://github.com/joyent/libuv.git ' + libuv_dir)

# gyp
mkdirp(build_dir)
run('git clone https://git.chromium.org/external/gyp.git ' + gyp_dir)
