#!/bin/bash
echo "Installing the fish shell. This will require giving sudo permissions"
sudo -v

#Command can now be safely run
sudo apt-get -q install fish

echo "Fish should be installed. Version below..."
fish -v

echo "Adding fish to the trusted shells file!"
tee -a $(which fish)

echo "Installation complete! Please set your default shell."
exit 0