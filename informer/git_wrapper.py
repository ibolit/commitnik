import logging
import shlex
import subprocess


def git(*args):
    command = 'git ' + ' '.join(args)
    kwargs = {
         'stdout': subprocess.PIPE,
         'stderr': subprocess.PIPE
    }
    proc = subprocess.Popen(shlex.split(command), **kwargs)
    (stdout_str, stderr_str) = proc.communicate()
    if stderr_str:
        logging.error(stderr_str)
    return stdout_str.decode().strip()
