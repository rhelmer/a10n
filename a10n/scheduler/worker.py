# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from __future__ import with_statement
import time

from kombu import Connection
from kombu.mixins import ConsumerMixin
from kombu.log import setup_logging

from a10n.queues import compare_queues, scheduler_queues

logger = setup_logging('INFO')
#logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

class Worker(ConsumerMixin):

    def __init__(self, connection, settings):
        self.connection = connection
        self.retries = 0
        self.max_retries = settings.MAX_HG_RETRIES
        self.sentry = None
        if hasattr(settings, 'RAVEN_CONFIG'):
            from raven import Client
            self.sentry = Client(**settings.RAVEN_CONFIG)

    def get_consumers(self, Consumer, channel):
        return [Consumer(queues=scheduler_queues,
                         callbacks=[self.process_pushes,
                                    self.process_repo,
                                    self.push_compare])]

    def process_pushes(self, body, message):
        if body.get('type') != 'scheduler':
            return
        logger.info('got scheduler message %r', body)
        try:
            # TODO tree config
            self.retries = 0
        except KeyboardInterrupt:
            raise
        except Exception:
            self.retries += 1
            logger.error('handlePushes failed: %d' % self.retries,
                         exc_info=True)
            if self.sentry:
                self.sentry.captureException()
            if self.retries > self.max_retries:
                # this problem might be real, let's just die
                # and have a human figure it out
                raise
            time.sleep(self.retries)
            message.requeue()
            return

        try:
            push_compare(body['repository_id'])
        except KeyboardInterrupt:
            raise
        except Exception:
            logger.error('push_compare failed', exc_info=True)
            return

        message.ack()

    def push_compare(self, repository_id):
        connection = Connection(settings.TRANSPORT)
        with producers[connection].acquire(block=True) as producer:
            maybe_declare(compare_exchange, producer.channel)
            # TODO what else does compare need?
            msg = {'type': 'compare',
                   'repository_id': repository_id}
            try:
                producer.publish(msg, exchange=compare_exchange,
                                 routing_key='compare')
            except KeyboardInterrupt:
                raise
            except Exception:
                if self.sentry:
                    self.sentry.captureException()
                raise

def run(args):
    from django.conf import settings

    with Connection(settings.TRANSPORT) as conn:
        try:
            Worker(conn, settings).run()
        except KeyboardInterrupt:
            print('bye bye')
