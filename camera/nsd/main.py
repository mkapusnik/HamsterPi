from zeroconf import IPVersion, ServiceInfo, Zeroconf
import os

hostFile = open("/hostname", "r")
server = hostFile.readline().strip()

port = int(os.environ.get('PORT', 8555))
name = os.getenv('NAME', server.title())
desc = {'deviceName': name}
type = '_nanny._tcp.local.'

info = ServiceInfo(
    type,
    name+"."+type,
    port=port,
    properties=desc,
    server=server+".local.",
)

zeroconf = Zeroconf(ip_version=IPVersion.V4Only)
print("Registration of a service {} on {}:{}, press Ctrl-C to exit...".format(name, server, port))
zeroconf.register_service(info)
try:
    input("Press enter to exit...\n\n")
finally:
    print("Unregistering...")
    zeroconf.unregister_service(info)
    zeroconf.close()