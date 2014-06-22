bashrc-pacman-updates
=====================

Displays how many packages can be updated at the top of the terminal.  Checks for updates once every 12 hours.

Installation is pretty simple add the code blow to the end of `/etc/bash.bashrc` or 
`~/bashrc` make sure it's after ```[[ $- != *i* ]] && return```:
```
echo ""
/path/to/arch-updates.py & 
```

Example output:
```There are 3 updates.  Packages: htop, perl and skype```
