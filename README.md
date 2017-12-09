Raspberry Pi Xmas Tree
======================

Herein lies a repo containing some really poor attempts at using Ansible and
Python to control a Raspberry Pi Zero W with PiHut's [3D Xmas Tree](https://thepihut.com/products/3d-xmas-tree-for-raspberry-pi) kit attached.

By trade I normally do stuff with Chef and Ruby, so please don't expect anything
here to be ideomatic Ansible or Python. That said, comments and PRs are welcome.

Notes
-----

The Ansible playbook expects a Raspberry Pi with the hostname `xmastree` to
already exist on your network. The easiest way to make this happen is to
configure `wpa-supplicant.conf` on the microSD card, then SSH in and use
`raspi-config` to update the hostname. You'll also want to copy across your SSH
key at that point.

The internet is awash with guides on doing headless wifi setup on a Raspberry Pi
Zero W, so Google should sort you out there.
