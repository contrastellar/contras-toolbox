# this will unlink the default wsl2 resolv.conf
sudo unlink /etc/resolv.conf 

# This config will prevent wsl2 from overwritting the resolve.conf file everytime
# you start wsl2
cat <<EOF | sudo tee -a /etc/wsl.conf
[network]
generateResolvConf = false
EOF

# all NS's will be listed here
# the entries for nameserver and search get added to this cat command
# this will likely be edited with output from either/or of the .ps1 scripts that are in this repo
cat <<EOF | sudo tee -a /etc/resolv.conf
nameserver <IPs go here>
nameserver 8.8.8.8
nameserver 8.8.4.4
search <searches goes here>
EOF

# Make the new /etc/resolve.conf immutable
sudo chattr +i /etc/resolv.conf
