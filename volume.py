import subprocess
status = str(subprocess.check_output("amixer | grep 'Front Left: Playback'", shell=True))
result = status.split()[-2]
command = ["notify-send ", "'Current volume: ", str(result), "' ", "-t 500"]
command = "".join(command)
subprocess.run(command, shell=True)
