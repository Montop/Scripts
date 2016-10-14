import subprocess
status = subprocess.check_output("xinput list-props 'SynPS/2 Synaptics TouchPad' | grep 'Device Enabled......:'", shell=True)
result = list(status)
if result[-2] == 48:
    subprocess.Popen("xinput set-prop 'SynPS/2 Synaptics TouchPad' 'Device Enabled' 1", shell=True, stdout=subprocess.PIPE)
else:
    subprocess.Popen("xinput set-prop 'SynPS/2 Synaptics TouchPad' 'Device Enabled' 0", shell=True, stdout=subprocess.PIPE)
