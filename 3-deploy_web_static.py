#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

Author: Yunus Kedir

Contains:
    Misc
    ====
    fabfile to combine functionalities of archiving and deploying
"""
import datetime
import os
from fabric.api import env, local, put, sudo


env.hosts = ['34.224.2.49', '52.3.240.101']


def do_pack():
    """
    Fab task to create an archive file
    """
    now = datetime.datetime.now()
    now = now.strftime("%Y%m%d%H%M%S")
    local("mkdir -p versions")
    ar_name = "versions/web_static_{}.tgz".format(now)
    result = local("tar -cvzf {} ./web_static".format(ar_name))
    if os.path.exists(ar_name):
        return (ar_name)
    return (None)


def do_deploy(archive_path):
    """
    Fabfile to deploy archive to remote web server
    """
    if not (archive_path and os.path.exists(archive_path)):
        return (False)
    filename = ".".join(archive_path.split("/")[-1].split(".")[0:-1])
    c1 = put(archive_path, "/tmp/{}".format(filename), use_sudo=True).succeeded
    remote_path = "/data/web_static/releases/{}".format(filename)
    c2 = sudo("mkdir -p {}".format(remote_path)).succeeded
    c3 = sudo("tar -xzf /tmp/{} -C {}".format(filename, remote_path)).succeeded
    c4 = sudo("mv {0}/web_static/* {0}".format(remote_path)).succeeded
    c5 = sudo("rm -rf /tmp/{} {}/web_static".format(filename,
                                                    remote_path)).succeeded
    link = "/data/web_static/current"
    c6 = sudo("ln -snf {} {}".format(remote_path, link)).succeeded
    if c1 and c2 and c3 and c4 and c5 and c6:
        return (True)
    return (False)


archive_path = do_pack()


def deploy():
    """
    Calls the above two functions for a full deployment
    """
    if not archive_path:
        return (False)
    return (do_deploy(archive_path))
