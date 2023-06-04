# vim: ft=python ts=4 sw=4 tw=999 expandtab fileencoding=utf-8
# ----------------------------------------------------------------------------
# File : run.py
# Author : yc0325lee
# Created : 2022-03-05 17:48:20 by lee2103
# Modified : 2022-03-05 17:48:20 by lee2103
# Description : 
# ----------------------------------------------------------------------------
import sys

# (1)
if False:
    import game.sound.echo
    game.sound.echo.test()

# (2)
if False:
    from game.sound import echo
    echo.test()

# (3)
if False:
    from game.sound.echo import test
    test()

# (4)
if False:
    from game.sound import *
    wav.test()

# (5)
if True:
    from game.graphic import * # graphic/__init__.py -> __all__
    render.test()
