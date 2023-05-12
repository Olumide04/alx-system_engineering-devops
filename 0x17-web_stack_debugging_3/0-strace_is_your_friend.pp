# Puppet manifest to fix Apache 500 error using strace

# Install strace package
package { 'strace':
  ensure => installed,
}

# Run strace on Apache process
exec { 'strace-apache':
  command => 'strace -p $(pgrep apache2) -f -e trace=network -s 1000 -o /tmp/strace.log',
  path    => ['/bin', '/usr/bin'],
  creates => '/tmp/strace.log',
}

# Fix the issue with Apache
exec { 'fix-apache':
  command     => 'sed -i "s/Listen 80/Listen 8080/g" /etc/apache2/ports.conf && service apache2 restart',
  path        => ['/bin', '/usr/bin'],
  refreshonly => true,
  subscribe   => Exec['strace-apache'],
}

