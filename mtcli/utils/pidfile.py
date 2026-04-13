import os
import sys
import signal


class PidFile:

    def __init__(self, path: str):
        self.path = path

    def create(self):

        if os.path.exists(self.path):

            with open(self.path) as f:
                pid = int(f.read().strip())

            if self._pid_running(pid):
                print(f"Monitor já está rodando (PID {pid})")
                sys.exit(1)

        with open(self.path, "w") as f:
            f.write(str(os.getpid()))

    def remove(self):
        if os.path.exists(self.path):
            os.remove(self.path)

    def _pid_running(self, pid: int):

        try:
            os.kill(pid, 0)
            return True
        except OSError:
            return False
