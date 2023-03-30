from ipaddress import ip_network
from ipcalc import Network
from pathlib import Path

# Relative path for input folder and output file
INPUT_FOLDER_PATH = './providers/'
OUTPUT_FILE = './openvpn/routes.conf'

# Output parameters
OPENVPN_COMMAND = "route"
OPENVPN_GATEWAY = "net_gateway"
OPENVPN_METRIC = "default"


def get_provider_cidrs(folder_path):
    cidrs = ""
    files = folder_path.glob('**/*.txt')
    for file_path in files:
        cidrs += Path(file_path).read_text()
    return cidrs


def generate_routes(cidr_list):
    routes = ""
    for cidr in cidr_list:
        ip = Network(cidr)
        network = str(ip.network())
        netmask = str(ip.netmask())
        route = f"{OPENVPN_COMMAND} {network} {netmask} {OPENVPN_GATEWAY} {OPENVPN_METRIC}\n"
        routes += route
    return routes


def main():
    folder_path = Path(__file__).parent / INPUT_FOLDER_PATH
    cidrs = get_provider_cidrs(folder_path)
    cidr_list = sorted(cidrs.splitlines(), key=lambda x: ip_network(x))
    routes = generate_routes(cidr_list)

    with open(OUTPUT_FILE, "w") as f:
        print(routes, file=f)

    print("Routes successfully generated")


if __name__ == "__main__":
    main()
