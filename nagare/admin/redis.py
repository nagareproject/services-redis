# --
# Copyright (c) 2008-2022 Net-ng.
# All rights reserved.
#
# This software is licensed under the BSD License, as described in
# the file LICENSE.txt, which you should have received as part of
# this distribution.
# --

from nagare.admin import command


class Commands(command.Commands):
    DESC = 'Redis subcommands'


def display_config(config, label):
    if config and label:
        print(label + ':')

    for k, v in sorted(config.items()):
        print('  - {}: {}'.format(k, v))


class Clients(command.Command):
    DESC = 'displays informations on the clients connected to the Redis server'

    def set_arguments(self, parser):
        parser.add_argument(
            '-t', '--type',
            choices=('normal', 'master', 'replica', 'pubsub'),
            default=None
        )

        super(Clients, self).set_arguments(parser)

    def run(self, redis_service, type):
        clients = redis_service.client_list(type)

        print('{} client{}\n'.format(len(clients), '' if len(clients) < 2 else 's'))

        for client in sorted(clients, key=lambda d: int(d['id'])):
            display_config(client, 'client {}'.format(client.pop('id')))


class Info(command.Command):
    DESC = 'displays server statistics'

    def set_arguments(self, parser):
        parser.add_argument(
            '-t', '--type',
            choices=('all', 'server', 'clients', 'memory', 'persistence', 'stats', 'replication', 'cpu', 'commandstats', 'cluster', 'keyspace'),
            default='default'
        )

        super(Info, self).set_arguments(parser)

    def run(self, redis_service, type):
        display_config(redis_service.info(type), 'Server statistics')


class Config(command.Command):
    DESC = 'displays server configurations'

    def set_arguments(self, parser):
        parser.add_argument('-t', '--type', default='*', help='config pattern')

        super(Config, self).set_arguments(parser)

    def run(self, redis_service, type):
        display_config(redis_service.config_get(type), 'Server configuration')


class Size(command.Command):
    DESC = 'displays cache size'

    def run(self, redis_service):
        size = redis_service.dbsize()

        print('{} keys'.format(size))


class Flush(command.Command):
    DESC = 'delete all the keys in cache'

    def run(self, redis_service):
        return 0 if redis_service.flushall() else 1
