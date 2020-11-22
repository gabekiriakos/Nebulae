# Management

Although the following commands are often used, check the [cheat sheet](https://wiki.gentoo.org/wiki/Gentoo_Cheat_Sheet) for details.

```bash
(updates repositories - typically once a day)
emerge-webrsync

(if flag changes have been made with intent to update only several packages)
emerge --ask --update --changed-use --quiet @world

(if new flags have been added locally or globally with intent to update the entire system)
emerge --ask --update --newuse --quiet @world

(add package from @world)
emerge --ask <package>

(remove package from @world)
emerge --ask --deselect <package>

(remove unused packages from system - this should be run after system updates)
emerge --ask --depclean

(make changes to /etc/portage/package.use and /etc/security/limits.conf when prompted)
etc-update

(list available overlay repos)
layman -L

(add repo)
layman -a <name>

(remove repo)
layman -d <name>

(update repos)
layman -S

```
