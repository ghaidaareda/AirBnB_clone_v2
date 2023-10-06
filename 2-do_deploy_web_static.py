#!/usr/bin/python3
"""
Fabric script that
extarct archive to severs
"""

import os
from fabric.api import run, env, put


def do_deploy(archive_path):
    if not os.path.exists(archive_path):
        print(f"Archive file not found: {archive_path}")
        return False

    archive_name = os.path.basename(archive_path)
    archive_no_ext = os.path.splitext(archive_name)[0]
    remote_path = "/tmp/{}".format(archive_name)

    try:
        put(archive_path, remote_path)
        run("mkdir -p /data/web_static/releases/{}/".format(archive_no_ext),
            key_filename=~/.ssh/school)
        run("tar -xzf {} -C /data/web_static/releases/{}/"
            .format(remote_path, archive_no_ext))
        run("rm {}".format(remote_path))
        run("mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/".format(archive_no_ext,
                                                   archive_no_ext))
        run("rm -rf /data/web_static/releases/{}/web_static"
            .format(archive_no_ext))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ "
            "/data/web_static/current".format(archive_no_ext))
        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False
