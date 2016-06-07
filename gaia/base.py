# -*- coding: utf-8 -*-

import os


def find_path():
    cwd = os.getcwdu()
    venvpath = os.path.join(cwd, '.py')

    if os.path.exists(venvpath):
        basepath = cwd
    else:
        testpath = os.path.join(os.path.dirname(__file__), '..')
        level = 0
        while level < 6:
            testpath = os.path.join(testpath, '..')
            venvpath = os.path.join(testpath, '.py')
            if os.path.exists(venvpath):
                basepath = testpath
                break
            level += 1
        else:
            basepath = cwd

    return basepath


