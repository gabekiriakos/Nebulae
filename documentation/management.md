# Management

[Home](https://github.com/gabekiriakos/Nebulae) | [Installation](../documentation/installation.md) | [Kernel](../documentation/kernel.md) | [Management](../documentation/management.md)

### USE Flags

USE flags can be determined globally or locally.  They are designed to make each package as minimal as possible, effectively removing any potential bloat in the process.  This also helps make compiling much faster.  More on this [here](https://wiki.gentoo.org/wiki/USE_flag).

The most important thing to understand is the [precedence of USE flags](https://wiki.gentoo.org/wiki/Handbook:AMD64/Working/USE#Precedence).  Your default profile already has USE flags predetermined and take on the lowest precendence, while changes at the time of installing a package at the command line take on the highest precendence.  Global USE flags are established in your [`make.conf`](../etc/portage/make.conf), while local ones are set in the [`/etc/portage/package.use`](../etc/portage/package.use) directory by package name.  

### Accept Keywords

When installing a package, you will often encounter a prompt like the following:

```bash
root #emerge --ask media-sound/sfc

These are the packages that would be merged, in order:

Calculating dependencies... done!
[ebuild  N    #] media-sound/sfc-0.018-r1 

The following mask changes are necessary to proceed:
 (see "package.unmask" in the portage(5) man page for more details)
# required by media-sound/sfc (argument)
# /var/db/portage/profiles/package.mask:
# Jonas Stein <jstein@gentoo.org> (24 Jun 2019)
# Source is broken. Upstream is dead since 2011.
# Removal after 2019-08-01. (bug #688552)
=media-sound/sfc-0.018-r1

NOTE: The --autounmask-keep-masks option will prevent emerge
      from creating package.unmask or ** keyword changes.

Would you like to add these changes to your config files? [Yes/No] 
```

Although the Gentoo wiki [covers it](https://wiki.gentoo.org/wiki/Knowledge_Base:Unmasking_a_package), I personally find the easiest way to deal with this is to say `Yes`, run `etc-update`, select the newly updated config (typically option #1), and create an example file (typically option #5).  Then, you should rename this new file to the name of the package you intend to install by running `mv /etc/portage/package.use/<example_file> /etc/portage/package.use/<new_name>`.  Another alternative is to use a single file (`/etc/portage/package.use/<single_file>`) for all changes instead of separate ones.  Once either of these steps has been done correctly, you should be able to install the package on the next attempt.

Your default profile selected at the time of installation has some package restrictions by default.  If the package you want to install throws an "accept" error, [`package.accept_keywords`](../etc/portage/package.accept_keywords) needs to be updated.

### Disk Management

By design, disk space gets accumulated with the installation of many packages.  They are cached but can be removed safely using `eclean` (part of the [app-portage/gentoolkit](https://packages.gentoo.org/packages/app-portage/gentoolkit) package).  Not all of the distfiles or packages located in `/var/cache/distfiles/` and `/var/cache/binpkgs/` respectively, will get removed using `eclean`, so it is up to you to decide whether to remove them or not.  It should be noted that although it doesn't hurt to do so, removing these files requires re-downloading them if any problems occur at some point.

### Common Commands

The following commands are often used (check the [cheat sheet](https://wiki.gentoo.org/wiki/Gentoo_Cheat_Sheet) for details):

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

Clean distfiles: <br>
`eclean-dist -dp` (remove `p` if sure)

Clean packages: <br>
`eclean-pkg -dp` (remove `p` if sure)

### Aliases

Since many commands are quite verbose, it is best practice to establish [aliases](https://www.tecmint.com/create-alias-in-linux/) that make Gentoo easier to manage.
The following is taken from my [.bashrc](../.bashrc) that I commonly use to `update` and `clean` the system:

```bash
alias \
	update='sudo emerge-webrsync; 
		sudo layman -S; 
		sudo emerge -uND @world' \
	clean='sudo emerge --depclean; 
	       sudo eclean-dist -d; 
	       sudo eclean-pkg -d; 
	       echo "Before:" `sudo du -sh ~/.cache/`;
	       rm -rf ~/.cache/*;
	       echo "After:" `sudo du -sh ~/.cache/`' \
```
