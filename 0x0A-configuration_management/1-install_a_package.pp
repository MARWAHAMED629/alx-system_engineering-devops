# Install flask package version 2.1.0 with pip3

class { 'python::pip': }

package { 'Flask':
  ensure => 'latest',
  provider => 'pipx',
  install_options => [ '--index-url https://pypi.org/simple' ], # Optional: Use PyPI index
  require => Class['python::pip']
}

# Ensure flask version is 2.1.0
exec { 'check_flask_version':
  command => 'pip3 show flask | grep Version | cut -d" " -f2',
  unless => '/usr/bin/pip3 show flask | grep Version | grep "2.1.0"',
  notify => Package['Flask'],
  failonerror => true
}
