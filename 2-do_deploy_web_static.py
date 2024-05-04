#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

Author: Yunus Kedir

Contains:
    Misc
    ====
    Fabfile to deploy/send created archive to web servers
"""
import os
from fabric.api import cd, env, put, run


env.hosts = ['34.224.2.49', '52.3.240.101']


def do_deploy(archive_path):
    """
    Fabfile to deploy archive to remote web server
    """
    if not (archive_path and os.path.exists(archive_path)):
        return (False)
    fname = ".".join(archive_path.split("/")[-1].split(".")[0:-1])
    c1 = put(archive_path, "/tmp/{}.tgz".format(fname), use_sudo=True).succeeded
    remote_path = "/data/web_static/releases/{}".format(fname)
    c2 = run("mkdir -p {}".format(remote_path)).succeeded
    c3 = run("tar -xzf /tmp/{} -C {}".format(fname, remote_path)).succeeded
    c4 = run("mv {0}/web_static/* {0}".format(remote_path)).succeeded
    c5 = run("rm -rf /tmp/{} {}/web_static".format(fname,
                                                    remote_path)).succeeded
    link = "/data/web_static/current"
    c6 = run("ln -snf {} {}".format(remote_path, link)).succeeded
    if c1 and c2 and c3 and c4 and c5 and c6:
        return (True)
    return (False)
