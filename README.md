# Nebulae <img width="25" height="25" src="/gentoo-logo.png">

[Home](https://github.com/gabekiriakos/Nebulae) | [Installation](documentation/installation.md) | [Kernel](documentation/kernel.md) | [Management](documentation/management.md)

<b>Disclaimer:</b><br>
<i>It should go without saying that I am not responsible for anything YOU did to YOUR system. <br>
Gentoo is targeted for <ins>advanced</ins> power users willing to invest in the time and patience to build their own environment.</i>

---

<b>Environment:</b>
* Distro: [Gentoo](https://www.gentoo.org/) <img align="right" width="60%" height="60%" src="/screenshot.png">
* Init: [OpenRC](https://wiki.gentoo.org/wiki/Project:OpenRC)
* WM: [i3-gaps](https://github.com/Airblader/i3)
* Status: [py3status](https://github.com/ultrabug/py3status)
* Compositor: [picom](https://github.com/yshui/picom)
* Terminal: [Terminator](https://terminator-gtk3.readthedocs.io/en/latest/)
* Menu: [Rofi](https://github.com/davatorium/rofi)
* Icons: [Papirus](https://github.com/PapirusDevelopmentTeam/papirus-icon-theme)
* Fonts: 
   * [Noto Sans](https://packages.gentoo.org/packages/media-fonts/noto)
   * [Monaco](.fonts/monaco.ttf) (terminal)
   * [Awesome](https://packages.gentoo.org/packages/media-fonts/fontawesome) (glyphs)

<br>

<b>Features:</b>
* System Menu: <i>super+e</i>
* Programs Menu: <i>super+d</i>
* Screenshot (requires Scrot): <i>super+p</i>
* Toggle Window Floating: <i>super+w</i>
* Toggle Workspaces: <i>alt+tab</i>
* Exit Active Window: <i>ctrl+q</i>
* Passthrough Mode (lock all bindings): <i>super+q</i> <br>

Refer to the [i3 config](.config/i3/config) for all other features and key bindings.

Dotfiles should be added to their respective locations according to the framework of this distribution. <br>
[Refer to the wiki](https://wiki.gentoo.org/wiki/Main_Page) for details concerning each application.

---
<b>Dependencies:</b>

<details>
<summary>
<b>Emerge</b>
</summary>
<i>
sys-kernel/linux-firmware, 
app-portage/genlop, 
app-portage/layman, 
media-libs/jpeg, 
net-misc/networkmanager, 
gnome-extra/nm-applet, 
sys-auth/elogind, 
app-admin/sudo, 
app-editors/vim, 
app-vim/airline, 
app-vim/nerdtree, 
dev-vcs/git, 
app-misc/ranger, 
app-misc/neofetch, 
x11-base/xorg-x11, 
x11-drivers/nvidia-drivers, 
virtual/wine, 
games-util/lutris (requires dxvk-bin),  
x11-wm/i3-gaps, 
x11-misc/i3status, 
x11-misc/py3status, 
x11-misc/i3lock, 
x11-misc/picom, 
x11-misc/pcmanfm, 
x11-misc/rofi, 
x11-terms/terminator, 
x11-misc/lightdm, 
x11-misc/nitrogen, 
x11-misc/dunst, 
sys-fs/udiskie, 
sys-fs/ncdu, 
sys-fs/ntfs3g, 
sys-process/htop, 
media-fonts/noto, 
media-fonts/noto-cjk, 
media-fonts/noto-emoji, 
media-fonts/fontawesome, 
media-sound/alsa-utils, 
media-sound/pulseaudio, 
media-sound/pavucontrol, 
media-sound/pasystray, 
www-client/links, 
www-client/firefox, 
media-video/vlc, 
media-libs/libdvdnav, 
x11-themes/papirus-icon-theme, 
lxde-base/lxappearance, 
app-i18n/fcitx, 
app-i18n/fcitx-configtool, 
app-i18n/fcitx-anthy
</i>
</details>

<details>
<summary>
<b>Layman</b>
</summary>
<i>app-emulation/dxvk-bin (layman -a guru)</i>
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

Additionally, DXVK [must be configured](https://wiki.gentoo.org/wiki/DXVK) for 32-bit driver support.
