bashrc-pacman-updates
=====================

Displays how many packages can be updated at the top of the terminal.  Checks for updates once every 12 hours.

Installation is pretty simple add this to `/etc/bashrc` or `~/bashrc`:
```
echo ""
/path/to/arch-updates.py & 
```

Example output:
```There are 3 updates.  Packages: htop, perl and skype```
