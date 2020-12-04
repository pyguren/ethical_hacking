from subprocess import Popen, PIPE

for ip in range(1,254):
    ipAddress = "192.168.1." + str(ip)

    # Windows
    subp = Popen(['ping', '-n', '1', ipAddress], stdout=PIPE, stdin=PIPE, stderr=PIPE)
    stdout, stderr = subp.communicate(input=None)
    if "TTL" in str(stdout):
        print("IP %s is up" % (ipAddress))

    #Linux
    #subp = Popen(['/bin/ping','-c 1', ipAddress], stdout=PIPE, stdin=PIPE, stderr=PIPE)
    #stdout, stderr = subp.communicate(input=None)
    #if "bytes from " in str(stdout):
    #    print("IP %s is up" % (ipAddress))