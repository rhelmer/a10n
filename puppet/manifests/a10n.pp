# Version:  $Id$

class webapp::a10n {

    file {
        '/etc/supervisord.conf':
            source => '/vagrant/puppet/files/supervisord.conf',
            notify => Service[supervisord];

        '/home/vagrant/.hgrc':
            source => '/vagrant/puppet/files/dot.hgrc';

        '/src/l10n/a10n/a10n/settings/local.py':
            source => '/vagrant/puppet/files/local.py';
    }

    service {
        'supervisord':
            ensure => running,
            require => Package['supervisor'];

        'rabbitmq-server':
            ensure => running,
            require => Package['rabbitmq-server'];
    }

    user {
      'a10n':
        ensure => present,
        system => true;
    }

    package {
        [
         'rabbitmq-server',
         'mysql-server',
         'mysql-devel',
         'python-virtualenv',
         'supervisor',
         # the following are for elmo
         'libxslt-devel',
         'libxml2-devel',
        ]:
        ensure => latest;
    }
}
