#!/bin/bash
echo "This just installs the Digital Ocean monitoring agent"

/usr/bin/curl -sSL https://repos.insights.digitalocean.com/install.sh | sudo bash

echo "Script complete!"
exit 0