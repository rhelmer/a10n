# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from kombu import Exchange, Queue

hg_exchange = Exchange('hg', type='direct')
hg_queues = [Queue('hg', hg_exchange, routing_key='hg')]

scheduler_exchange = Exchange('scheduler', type='direct')
scheduler_queues = [Queue('scheduler', scheduler_exchange,
                          routing_key='scheduler')]

compare_exchange = Exchange('compare', type='direct')
compare_queues = [Queue('compare', compare_exchange,
                        routing_key='compare')]
