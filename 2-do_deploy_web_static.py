#!/usr/bin/python3
"""
Fabric script that
extarct archive to severs
"""

import os
from fabric.api  import run, put, env


def do_deploy(archive_path):
    """
    extract the archive to server
    """
    if archive_path:
        env.hosts = ['100.26.50.163', '107.22.142.93']
        remote = '/tmp/{}'.format(os.path.basename(archive_path))
        put(archive_path, '/tmp/')
        no_ext = os.path.splitext(os.path.basename(archive_path))[0]
        remote_dir = '/data/web_static/releases/{}'.format(no_ext)
        run('sudo mkdir -p {}'.format(remote_dir))
        run('sudo tar -xzf {} -C {}'.format(remote, remote_dir))
        run('sudo service nginx restart')
    else:
        return False
