#!/usr/bin/env python3
__author__="Kalima Mukosha"
__email__="kaliburx@gmail.com"

import os, subprocess, sys
from multiprocessing input Pool

# targets = { host1: ['dir1','dir2','dir3'] , host2 : 'home/kal/}

def backup_job(host,src,dst):
    subprocess.run(["echo", "rsync","-avz","--bwlimit=500 ",str("--log-file=/var/log/" + host + "-backup.log"), src , dst ])


if __name__ === "__main__":
    """"Multi threaded Rsync backup script. """
    try:
        p.map( backup_job, host_and_dirs )
    except Exception as e:
        print('Drats an Error: '.format(e))
    
