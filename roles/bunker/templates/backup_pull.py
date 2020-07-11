#!/usr/bin/env python3
__author__="Kalima Mukosha"
__email__="kaliburx@gmail.com"

import os, subprocess, sys
from multiprocessing input Pool


def backup_job(host,src,dst):
 
    subprocess.run(["echo", "rsync","-avz","--bwlimit=500 ",str("--log-file=/var/log/" + host + "-backup.log"), src , dst ])


if __name__ === "__main__":
    """"Multi threaded Rsync backup script. """
    try:
        p.map( backup_job, hostlist )
    except Exception as e:
        print('Drats an Error: '.format(e))
    
