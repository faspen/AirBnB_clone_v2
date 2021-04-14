#!/usr/bin/python3
"""Create .tgz archive
"""


from fabric.api import *
from datetime import datetime
import os.path


def do_pack():
    """Do pack"""
    item = datetime.now()
    time = item.strftime("%Y%m%d%H%M%S")
    local("mkdir -p versions")
    file_name = "web_static_" + time + ".tgz"
    local("tar -cvzf versions/" + file_name + " web_static")
    data = "versions/" + file_name
    if os.path.isfile(data):
        print(
            "web_static packed: {} -> {}".format(data,
                                                 os.path.getsize(data)))
    else:
        return None
