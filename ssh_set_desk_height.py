import paramiko
from os.path import expanduser


def ssh_set_desk_height(height):
    cmd_to_execute = "curl http://localhost:9987/" + str(height)
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(
        "raspberrypi.local",
        username="pi",
        key_filename=expanduser("~") + "/.ssh/id_rsa.pub",
    )
    ssh_stdin, ssh_stdout, ssh_stderr = client.exec_command(cmd_to_execute)
