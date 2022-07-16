from zeroconf import IPVersion, ServiceInfo, Zeroconf
import os

port = os.getenv('PORT', 8555)
name = os.getenv('NAME', 'Default Nanny')
desc = {'deviceName': name}
type = '_nanny._tcp.local.'

info = ServiceInfo(
    type,
    name+"."+type,
    port=port,
    properties=desc,
    server="hamster.local.",
)

zeroconf = Zeroconf(ip_version=IPVersion.V4Only)
print("Registration of a service on port {}, press Ctrl-C to exit...".format(port))
zeroconf.register_service(info)
try:
    input("Press enter to exit...\n\n")
finally:
    print("Unregistering...")
    zeroconf.unregister_service(info)
    zeroconf.close()