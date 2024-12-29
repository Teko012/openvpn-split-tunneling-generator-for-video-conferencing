# Generate OpenVPN split tunneling routes for video conferencing
The tool generates OpenVPN configuration commands that can be used with OpenVPN clients such as [Viscosity](https://www.sparklabs.com/support/kb/article/advanced-configuration-commands/#route) to make video conferencing traffic bypass a Full Tunnel OpenVPN connection by making it into a split tunnel.

The output in `openvpn/routes.conf` can be added to a connection's `config.conf` file or copied into the `Advanced` tab under a connection's settings in Viscosity.

With some slight modifications, these routes can also be pushed down from an OpenVPN server to the end users.

## Supported providers
* [Amazon Chime](https://answers.chime.aws/articles/123/hosts-ports-and-protocols-needed-for-amazon-chime.html) / [Slack Huddle](https://slack.com/help/articles/36284146785427-Guide-to-network-and-system-configuration-for-Slack-huddles)
* [Google Meet - Consumer & Google Workspace](https://support.google.com/a/answer/1279090)
* [Skype for Business Online and Microsoft Teams #11](https://learn.microsoft.com/en-us/microsoft-365/enterprise/urls-and-ip-address-ranges) ([API](https://endpoints.office.com/endpoints/worldwide?clientrequestid=b10c5ed1-bad1-445f-b386-b919946339a7))
* [Webex](https://help.webex.com/en-us/article/WBX000028782/Network-Requirements-for-Webex-Services)
* [Zoom Meetings](https://support.zoom.us/hc/en-us/articles/201362683-Zoom-network-firewall-or-proxy-server-settings) ([API](https://assets.zoom.us/docs/ipranges/ZoomMeetings.txt))

## Usage
It requires `Python 3.6` or above. In a new virtual environment, install the required packages:
```
python -m pip install --upgrade pip
pip install -r requirements.txt
```
Then run it with:
```
python generate.py
```
This will generate the routes from  the `providers` folder to `openvpn/routes.conf`.
