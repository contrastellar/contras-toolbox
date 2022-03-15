#!/bin/bash
echo "Installing NPM. This will require giving sudo permissions"
sudo -v #This simply validates the user

#Command can now be safely run
sudo apt-get -q install npm

echo "NPM should be installed. Version below..."
npm -v

echo "Installation complete!"
exit 0