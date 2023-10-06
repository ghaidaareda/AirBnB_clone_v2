#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive
from the contents of the web_static folder
"""
import os
from datetime import datetime
from fabric.api import local


def do_pack():
    """
    makeing archive
    """
    try:
        if not os.path.exists("versions"):
            os.makedirs("versions")
        now = datetime.utcnow().strftime("%Y%m%d%H%M%S")
        arc_name = f"web_static_{now}.tgz"
        arc_cmd = f"tar -cvzf versions/{arc_name} web_static"
        local(arc_cmd)
        return f"versions/{arc_name} web_static"
    except Exception:
        return None
