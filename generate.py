from ipaddress import ip_network
from ipcalc import Network
from pathlib import Path

# Relative folder path
input_folder_path = './providers/'
output_file = './openvpn/routes.conf'

# Output values
openvpn_command = "route"
openvpn_gateway = "net_gateway"
openvpn_metric = "default"

folder_path = Path(__file__).parent / input_folder_path
files = folder_path.glob('**/*.txt')

cidrs: str = ""
routes: str = ""

for file_path in files:
    cidrs += Path(file_path).read_text()

cidr_list = sorted(cidrs.splitlines(), key=lambda x: ip_network(x))

for cidr in iter(cidr_list):
    ip = Network(cidr)
    network = str(ip.network())
    netmask = str(ip.netmask())

    routes += " ".join([openvpn_command, network, netmask, openvpn_gateway, openvpn_metric]) + "\n"

with open(output_file, "w") as f:
    print(routes, file=f)

print("Routes successfully generated")
