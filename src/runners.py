import shlex
import subprocess

from .models import Job, InputTask


class PythonRunner:
    def run(self, job: Job, task: InputTask):
        cmd = shlex.split(f"pdm run python {job.path}")
        p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        resp, _ = p.communicate(input=task.data.encode())
        return resp.decode()

