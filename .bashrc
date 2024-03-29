# /etc/skel/.bashrc
#
# This file is sourced by all *interactive* bash shells on startup,
# including some apparently interactive shells such as scp and rcp
# that can't tolerate any output.  So make sure this doesn't display
# anything or bad things will happen !


# Test for an interactive shell.  There is no need to set anything
# past this point for scp and rcp, and it's important to refrain from
# outputting anything in those cases.
if [[ $- != *i* ]] ; then
	# Shell is non-interactive.  Be done now!
	return
fi

# Put your fun stuff here.

BLUE="\[$(tput setaf 4)\]"
MAGENTA="\[$(tput setaf 5)\]"
RESET="\[$(tput sgr0)\]"

PS1="${BLUE}[\w]${MAGENTA}: ${RESET}"

# Useful aliases
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
