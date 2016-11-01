import subprocess
status = subprocess.check_output("xinput list-props 'ELAN Touchscreen Pen' | grep 'Device Enabled......:'", shell=True)
result = list(status)
if result[-2] == 48:
    subprocess.Popen("xinput set-prop 'ELAN Touchscreen Pen' 'Device Enabled' 1", shell=True, stdout=subprocess.PIPE)
else:
    subprocess.Popen("xinput set-prop 'ELAN Touchscreen Pen' 'Device Enabled' 0", shell=True, stdout=subprocess.PIPE)

