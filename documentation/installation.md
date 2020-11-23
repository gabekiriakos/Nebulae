# Installation

[Home](https://github.com/gabekiriakos/Nebulae) | [Installation](documentation/installation.md) | [Kernel](documentation/kernel.md) | [Management](documentation/management.md)

The following is a condensed version of the [AMD64 Handbook](https://wiki.gentoo.org/wiki/Handbook:AMD64) for installing Gentoo.<br>
It is highly recommended to observe it throughout this process for details specific to your own build since this is personalized.

```bash
ping -4 google.com

lsblk

parted -a optimal /dev/nvme0n1
(parted) mklabel gpt
(parted) print
(parted) rm # (to remove partitions)
(parted) unit mib
(parted) mkpart primary 1 130
(parted) name 1 boot
(parted) mkpart primary 130 -1
(parted) name 2 system
(parted) set 1 boot on
(parted) print
(parted) quit

mkfs.fat -F32 /dev/nvme0n1p1
mkfs.ext4 /dev/nvme0n1p2

mount /dev/nvme0n1p2 /mnt/gentoo
df (to confirm)

Stage 3 tarball:
cd /mnt/gentoo
links https://www.gentoo.org/downloads/
(download latest)

tar xpvf stage3-*.tar.xz --xattrs-include='*.*' --numeric-owner

nano -w /mnt/gentoo/etc/portage/make.conf

(For Ryzen 3600)
CHOST="x86_64-pc-linux-gnu"
CFLAGS="-O2 -march=znver2 -pipe"
CXXFLAGS="${CFLAGS}"
MAKEOPTS="-j12"

mirrorselect -i -o >> /mnt/gentoo/etc/portage/make.conf
(select with spacebar)

mkdir --parents /mnt/gentoo/etc/portage/repos.conf

cp /mnt/gentoo/usr/share/portage/config/repos.conf /mnt/gentoo/etc/portage/repos.conf/gentoo.conf

cp --dereference /etc/resolv.conf /mnt/gentoo/etc/

mount --types proc /proc /mnt/gentoo/proc
mount --rbind /sys /mnt/gentoo/sys
mount --make-rslave /mnt/gentoo/sys
mount --rbind /dev /mnt/gentoo/dev
mount --make-rslave /mnt/gentoo/dev

chroot /mnt/gentoo /bin/bash
source /etc/profile
export PS1="(chroot) ${PS1}"

—-

mount /dev/nvme0n1p1 /boot

emerge-webrsync

eselect profile list (select same as stage 3)
eselect profile set # (unless already done)

emerge --ask --verbose --update --deep --newuse —quiet @world

*(determine current USE flags set by default profile)
emerge --info | grep ^USE
less /var/db/repos/gentoo/profiles/use.desc

**(establish additional USE flags fine-tuning)
nano -w /etc/portage/make.conf

ls /usr/share/zoneinfo
echo "Asia/Tokyo" > /etc/timezone

emerge --config sys-libs/timezone-data

nano -w /etc/locale.gen
(add en_US.UTF-8 UTF-8)

locale-gen
eselect locale list
eselect locale set #

env-update && source /etc/profile && export PS1="(chroot) ${PS1}"

—-

Kernel:
https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Kernel

(Make sure make.conf has ACCEPT_LICENSE=“*”)
emerge --ask sys-kernel/linux-firmware

emerge --ask sys-kernel/gentoo-sources
ls -l /usr/src/linux (confirm symbolic link)

emerge --ask sys-apps/pciutils
lspci (to get system information for kernel build)

NOTE: Check "kernel" guide for which options to enable or use /usr/src/linux/.config

cd /usr/src/linux
make menuconfig

(post-config)
make -j12 && make modules_install
make install

emerge --ask sys-kernel/genkernel

genkernel --install --kernel-config=/usr/src/linux/.config initramfs

ls /boot/initramfs* (to confirm)

emerge --depclean

blkid
nano -w /etc/fstab

/dev/nvme0n1p1   /boot     vfat    defaults,noatime     0 2
/dev/nvme0n1p2   /         ext4    noatime              0 1

nano /etc/hostname (name the pc)

nano /etc/hosts
127.0.0.1     localhost
::1           localhost
127.0.1.1     (hostname).localdomain (hostname)

(update with new USE flags)
NOTE: Several packages will require accept permissions or locally required USE flags.
Check the "management" guide for more information if unsure.
emerge --update --newuse --deep --quiet @world

emerge —ask app-editors/vim

emerge --ask net-misc/networkmanager
rc-update add NetworkManager default

emerge --ask app-admin/sudo
visudo (uncomment wheel group)

passwd (set root password)

useradd -m (new_user)
passwd (user)
usermod -aG wheel,audio,video,storage,power,optical,lp (user)
groups (user)

emerge --ask app-admin/sysklogd
rc-update add sysklogd default

emerge --ask --verbose sys-boot/grub:2

echo 'GRUB_PLATFORMS="efi-64"' >> /etc/portage/make.conf

grub-install --target=x86_64-efi --efi-directory=/boot

grub-mkconfig -o /boot/grub/grub.cfg

exit
reboot

rm /stage3-*.tar.*
```
