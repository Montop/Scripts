import subprocess
status = subprocess.check_output("xinput list-props 15 | grep 'Device Enabled (137):'", shell=True)
if status == b'\tDevice Enabled (137):\t0\n':
    subprocess.Popen("xinput set-prop 15 'Device Enabled' 1", shell=True, stdout=subprocess.PIPE)
else:
    subprocess.Popen("xinput set-prop 15 'Device Enabled' 0", shell=True, stdout=subprocess.PIPE)
