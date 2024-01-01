#!/usr/bin/env puppet
# using puppet to make changes to our config file

file { '/etc/ssh/ssh_config':
	ensure => present.
content =>"
	#SSH client configuration
	host *
	IdentityFile ~/.ssh/school
	PasswordAuthentication no
	",
}
