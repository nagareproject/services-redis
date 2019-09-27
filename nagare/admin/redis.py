# --
# Copyright (c) 2008-2019 Net-ng.
# All rights reserved.
#
# This software is licensed under the BSD License, as described in
# the file LICENSE.txt, which you should have received as part of
# this distribution.
# --

from nagare.admin import command


class Commands(command.Commands):
    DESC = 'Redis subcommands'


class Clients(command.Command):
    DESC = 'displays general statistiques'

    def run(self, redis_service):
        clients = redis_service.client_list()

        print('{} client{}\n'.format(len(clients), '' if len(clients) < 2 else 's'))

        for client in sorted(clients, key=lambda d: int(d['id'])):
            print('client {}:'.format(client.pop('id')))
            for k, v in sorted(client.items()):
                print('  - {}: {}'.format(k, v))


class Info(command.Command):
    DESC = 'displays general statistiques'

    def run(self, redis_service):
        info = redis_service.info()

        print('Server configuration:')
        for k, v in sorted(info.items()):
            print('  - {}: {}'.format(k, v))


class Config(command.Command):
    DESC = 'displays general statistiques'

    def run(self, redis_service):
        config = redis_service.config_get('repl*')

        print('Server configuration:')
        for k, v in sorted(config.items()):
            print('  - {}: {}'.format(k, v))


class Size(command.Command):
    DESC = 'displays general statistiques'

    def run(self, redis_service):
        size = redis_service.dbsize()

        print('{} keys'.format(size))
