# this will unlink the default wsl2 resolv.conf
sudo unlink /etc/resolv.conf 

# This config will prevent wsl2 from overwritting the resolve.conf file everytime
# you start wsl2
cat <<EOF | sudo tee -a /etc/wsl.conf
[network]
generateResolvConf = false
EOF

# all NS's will be listed here
cat <<EOF | sudo tee -a /etc/resolv.conf
nameserver <NS>
nameserver 8.8.8.8
nameserver 8.8.4.4
search <Search Engine>
EOF

# Make the new /etc/resolve.conf immutable
sudo chattr +i /etc/resolv.conf
