#!/usr/bin/python3
"""Fabric script
"""


from fabric.api import *
import os.path
from datetime import datetime

env.hosts = ['34.75.252.237', '107.20.130.157']


def do_pack():
    """Do pack"""
    item = datetime.now()
    time = item.strftime("%Y%m%d%H%M%S")
    local("mkdir -p versions")
    file_name = "web_static_" + time + ".tgz"
    local("tar -cvzf versions/" + file_name + " web_static")
    data = "versions/" + file_name
    if os.path.exists(data):
        print(
            "web_static packed: {} -> {}".format(data, os.path.getsize(data)))
    else:
        return None


def do_deploy(archive_path):
    """Do deploy"""
    if os.path.exists(archive_path) is False:
        return False
    try:
        new_path = archive_path.split('/')
        the_path = new_path[1].split('.')
        put(archive_path, "/tmp")
        run("mkdir -p /data/web_static/releases/{}".format(the_path[0]))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}".format(
            new_path[1], the_path[0]))
        run("rm /tmp/{}".format(new_path[1]))
        run("mv /data/web_static/releases/{}/web_static/*\
            /data/web_static/releases/{}".format(
            the_path[0], the_path[0]))
        run("rm -rf /data/web_static/releases/{}/web_static".format(
            the_path[0]))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/\
            /data/web_static/current".format(
            the_path[0]))
        print("New version deployed!")
        return True
    except:
        return False
