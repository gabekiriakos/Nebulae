# Management

Although the following commands are often used, check the [cheat sheet](https://wiki.gentoo.org/wiki/Gentoo_Cheat_Sheet) for details.

Update repositories (typically once a day): <br>
`emerge-webrsync`

Flag changes have been made with intent to update only several packages: <br>
`emerge --ask --update --changed-use --quiet --deep @world`

New flags have been added locally or globally with intent to update the entire system: <br>
`emerge --ask --update --newuse --quiet --deep @world`

Add package from @world: <br>
`emerge --ask <package>`

Remove package from @world: <br>
`emerge --ask --deselect <package>`

Remove unused packages from system (should be run after system updates): <br>
`emerge --ask --depclean`

Make changes to /etc/portage/package.use and /etc/security/limits.conf when prompted: <br>
`etc-update`

List available overlay repos: <br>
`layman -L`

Add overlay repo: <br>
`layman -a <name>`

Remove overlay repo: <br>
`layman -d <name>`

Update repos: <br>
`layman -S`
