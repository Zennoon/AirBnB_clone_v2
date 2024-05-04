#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

Author: Yunus Kedir

Contains
    Misc
    ====
    Fab file to generate a .tgz archive from contents of web_static folder
"""
import datetime
from fabric.api import env, local


def do_pack():
    """
    Fab task to create an archive file
    """
    now = datetime.datetime.now()
    now = now.strftime("%Y%m%d%H%M%S")
    local("mkdir -p versions")
    ar_name = "versions/web_static_{}.tgz".format(now)
    result = local("tar -cvzf {} ./web_static".format(ar_name))
    if result.succeeded:
        return (ar_name)
    return (None)
