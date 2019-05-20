# elicense
Tool to find installed packages in Gentoo with non-accepted license(s).

## Usage
Just call `elicense` program and review output:
```
~ # elicense
# The following package(s) are using licenses which aren't covered by
# ACCEPT_LICENSE="-* @FREE" setting nor have entries in the package.license file:
sys-block/hpacucli hp-proliant-essentials
sys-block/storcli Avago LSI
sys-kernel/linux-firmware linux-fw-redistributable no-source-code
media-fonts/corefonts MSttfEULA
sys-firmware/intel-microcode intel-ucode
```
The output can be used to populate `/etc/portage/package.license` file:

```
~ # elicense >> /etc/portage/package.license
```

If there isn't any package currently installed with unaccepted license(s), output will be
```
~ # elicense
# Licenses for all installed packages are already accepted!
```
