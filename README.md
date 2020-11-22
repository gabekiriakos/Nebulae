# Gentoo_Handbook <img width="25" height="25" src="/gentoo-logo.png">
<i>A condensed handbook for Gentoo to make installation and management easier</i>

---

<b>Hardware:</b>
* CPU: [AMD Ryzen 3600 @ 4.2Ghz](https://www.amd.com/en/products/cpu/amd-ryzen-5-3600)
* RAM: [G.Skill FlareX 3200Mhz 16GB](https://www.gskill.com/product/165/170/1535961634/F4-3200C14D-16GFX-Overview)
* Disk: [WD SN550 NVMe SSD](https://www.westerndigital.com/products/internal-drives/wd-blue-nvme-ssd)
* GPU: [Gigabyte NVIDIA GTX 1660 SUPER](https://www.gigabyte.com/Graphics-Card/GV-N166SOC-6GD#kf)
* Mobo: [ASUS ROG STRIX B450-I GAMING](https://rog.asus.com/Motherboards/ROG-Strix/ROG-STRIX-B450-I-GAMING-Model/)
* Modules: [Intel Corporation I211 Gigabit Network Connection](https://ark.intel.com/content/www/us/en/ark/products/64404/intel-ethernet-controller-i211-at.html) <br> [Realtek RTL8822BE WiFi/Bluetooth](https://www.realtek.com/en/products/communications-network-ics/item/rtl8822be)

<br>

<b>Overview:</b>
* Distro: [Gentoo](https://www.gentoo.org/)
* Init: [OpenRC](https://wiki.gentoo.org/wiki/Project:OpenRC)
* WM: [i3-gaps](https://github.com/Airblader/i3)
* Status: [py3status](https://github.com/ultrabug/py3status)
* Compositor: [picom](https://github.com/yshui/picom)
* Terminal: [Terminator](https://terminator-gtk3.readthedocs.io/en/latest/)
* Menu: [Rofi](https://github.com/davatorium/rofi)

<br>

<b>Noteable Features:</b>
* System Menu: <i>super+e</i>
* Programs Menu: <i>super+d</i>
* Screenshot (requires Scrot): <i>super+p</i>
* Toggle Window Floating: <i>super+w</i>
* Toggle Workspaces: <i>alt+tab</i>
* Exit Active Window: <i>ctrl+q</i>
* Passthrough Mode (lock all bindings): <i>super+q</i> <br>

Refer to i3 config for all other features and key bindings.

---
<b>Dependencies:</b>

<details>
<summary>
<b>Emerge</b>
</summary>
<i>xorg (all), i3 (gaps, status, lock), py3status, python-pydbus, rofi, dunst, picom, lightdm, git, terminator, networkmanager, network-manager-applet, udisks2, udiskie, ntfs-3g, reflector, nitrogen, gimp, firefox, vlc, libdvdnav, ranger, pcmanfm, noto-fonts, noto-fonts-extra, noto-fonts-cjk, noto-fonts-emoji, ttf-font-awesome, nvidia, nvidia-settings, lib32-nvidia-utils (multilib), steam (multilib), lutris (multilib) wine (multilib), htop, grub-customizer, lxappearance, neofetch, powerline, pulseaudio, pavucontrol, fcitx (all), fcitx-configtool, fcitx-mozc, gtk-engines, gtk-engine-murrine, gnome-themes-extra, baobab, file-roller, bluez, bluez-utils, blueman, papirus-icon-theme, pasystray</i>
</details>

<details>
<summary>
<b>Layman</b>
</summary>
<i>DXVK-bin (via Guru)</i>
</details>

---

<b>Note:</b><br>
A modified version of Louiss Warren's [playerctlbar](https://gist.github.com/louisswarren/d794ff91bdb02a248f5d60d52d1d0086) is being used to display music playback as a module of py3status.

dbus most likely needs to be wrapped in the session to work properly<br> 
(in this case, lightdm -> /etc/lightdm/XSession):

```bash
# Load dbus
if test -z "$DBUS_SESSION_BUS_ADDRESS" ; then
    ## if not found, launch a new one
    eval `dbus-launch --sh-syntax`
fi
```
Gaming applications through Lutris will not load unless [esync limits are set](https://github.com/lutris/docs/blob/master/HowToEsync.md):<br>
> On Linux distributions not using Systemd or distributions using pam-limits.conf (Arch Linux, Fedora, Solus,... ), you (with root privileges or sudo) need to edit /etc/security/limits.conf.
> Change username to your actual username. Once the file is edited, reboot for the changes to take effect, and verify by running `ulimit -Hn` to see the new limit (524288).
> 
> ```c
> username hard nofile 524288
> ```
---

Dotfiles should be added to their respective locations according to the framework of this distribution.  [Refer to the wiki](https://wiki.gentoo.org/wiki/Main_Page) for details concerning each application.<br>

<b>Disclaimer:</b><br>
<i>It should go without saying that I am not responsible for anything YOU did to YOUR system.  This distro is targeted for advanced power users willing to invest in the time and patience to build their own environment.</i>

![screenshot](/screenshot.png)
