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

        'mysqld':
            ensure => running,
            require => Package['mysql-server'];
    }

    user {
      'a10n':
        ensure => present,
        system => true;
    }

    yumrepo {
        'EPEL':
            baseurl => 'http://download.fedoraproject.org/pub/epel/6/$basearch',
            descr => 'EPEL',
            enabled => 1,
            gpgcheck => 0;
    }
    package {
        [
         'python-virtualenv',
         'supervisor',
         'rabbitmq-server',
        ]:
        ensure => latest,
        require => Yumrepo['EPEL'];
    }
    package {
        [
         'mysql-server',
         'mercurial',
         # the following are for elmo
         'libxslt-devel',
         'libxml2-devel',
         'mysql-devel',
        ]:
        ensure => latest;
    }
}
