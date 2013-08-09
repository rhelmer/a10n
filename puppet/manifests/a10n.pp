# Version:  $Id$

class webapp::a10n {

    file {
        '/etc/supervisord.conf':
            source => '/vagrant/puppet/files/supervisord.conf',
            notify => Service[supervisor];
    }

    service {
        'supervisor':
            ensure => running,
            require => Package['supervisor'];
    }

    user {
      'a10n':
        ensure => present,
        system => true;
    }

    package {
        [
         'httpd',
         'rabbitmq-server',
         'mysql-server',
         'mysql-devel',
         'python-virtualenv',
         'supervisor',
        ]:
        ensure => latest;
    }
}
