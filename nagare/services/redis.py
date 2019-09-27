# --
# Copyright (c) 2008-2019 Net-ng.
# All rights reserved.
#
# This software is licensed under the BSD License, as described in
# the file LICENSE.txt, which you should have received as part of
# this distribution.
# --

from __future__ import absolute_import

import redis
from nagare.services import plugin


class Redis(plugin.Plugin, redis.Redis):
    """Sessions manager for sessions kept in an external redis server
    """
    LOAD_PRIORITY = 75
    CONFIG_SPEC = {
        'host': 'string(default="127.0.0.1")', 'port': 'integer(default=6379)',
        'db': 'integer(default=0)', 'password': 'string(default=None)',
        'socket_timeout': 'integer(default=None)', 'socket_connect_timeout': 'integer(default=None)',
        'unix_socket_path': 'string(default=None)',
        'encoding': 'string(default="utf-8")', 'encoding_errors': 'string(default="strict")',
        'decode_responses': 'boolean(default=False)',
        'retry_on_timeout': 'boolean(default=False)',
        'ssl': 'boolean(default=False)',
        'ssl_keyfile': 'string(default=None)', 'ssl_certfile': 'string(default=None)',
        'ssl_cert_reqs': 'string(default="required")', 'ssl_ca_certs': 'string(default=None)',
        'max_connections': 'integer(default=None)', 'single_connection_client': 'boolean(default=False)',
        'health_check_interval': 'integer(default=0)'
    }

    def __init__(self, name, dist, **config):
        """Initialization

        In:
          - ``host`` -- address of the memcache server
          - ``port`` -- port of the memcache server
        """
        plugin.Plugin.__init__(self, name, dist)
        redis.Redis.__init__(self, **config)
