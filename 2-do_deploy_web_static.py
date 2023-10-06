#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive
from the contents of the web_static folder
"""
import os
from datetime import datetime
from fabric.api import local
from fabric import Connection


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
    
def do_deploy(archive_path):
    if archive_path:
        env.hosts = ['<IP web-01>', '<IP web-02>']
        c = Connection(host=env.hosts, user='<username>', connect_kwargs={'key_filename': '/path/to/ssh/key'})
        remote = '/tmp/{}'.format(os.path.basename(archive_path))
        c.put(archive_path, remote)
        remote_dir = '/data/web_static/releases/{}'.format(os.path.splitext(os.path.basename(archive_path))[0])
        c.run('sudo mkdir -p {}'.format(remote_dir))
        c.run('sudo tar -xzf {} -C {} --strip-components=1'.format(remote, remote_dir))
        c.run('sudo service nginx restart')
    else:
        return False
