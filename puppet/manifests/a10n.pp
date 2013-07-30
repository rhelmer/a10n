# Version:  $Id$

class webapp::a10n {

    include epel

    file {
        '/etc/httpd/conf.d/welcome.conf':
            ensure => absent,
            notify => Service[httpd];
    }

    service {
        'httpd':
            ensure => running,
            require => Package['httpd'];
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
         'python-virtualenv',
        ]:
        ensure => latest;
    }
}