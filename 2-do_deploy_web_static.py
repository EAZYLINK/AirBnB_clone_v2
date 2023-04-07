#!/usr/bin/env python3
"""
Fabric script to distribute an archive to web servers
"""

import os
from fabric.api import env, run, put

env.user = 'ubuntu'
env.hosts = ["100.25.193.56", "18.210.19.239"]

def do_deploy(archive_path):
    # Check if archive_path exists
    if not os.path.exists(archive_path):
        print("File does not exist!")
        return False

    # Extract archive filename without extension
    filename = os.path.basename(archive_path)
    filename_no_ext = os.path.splitext(filename)[0]

    # Upload archive to /tmp/ directory on web server
    put(archive_path, "/tmp/")

    # Create directory to uncompress archive
    run("sudo mkdir -p /data/web_static/releases/{}/".format(filename_no_ext))

    # Uncompress archive to directory
    run("sudo tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(filename, filename_no_ext))

    # Remove archive from web server
    run("sudo rm /tmp/{}".format(filename))

    # Delete symbolic link /data/web_static/current
    run("sudo rm -rf /data/web_static/current")

    # Create new symbolic link to new version of code
    run("sudo ln -s /data/web_static/releases/{}/ /data/web_static/current".format(filename_no_ext))

    # Return True if all operations were successful
    return True
