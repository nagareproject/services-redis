# Encoding: utf-8

# --
# Copyright (c) 2008-2021 Net-ng.
# All rights reserved.
#
# This software is licensed under the BSD License, as described in
# the file LICENSE.txt, which you should have received as part of
# this distribution.
# --

from os import path

from setuptools import setup, find_packages


here = path.normpath(path.dirname(__file__))

with open(path.join(here, 'README.rst')) as long_description:
    LONG_DESCRIPTION = long_description.read()

setup(
    name='nagare-services-redis',
    author='Net-ng',
    author_email='alain.poirier@net-ng.com',
    description='Redis service',
    long_description=LONG_DESCRIPTION,
    license='BSD',
    keywords='',
    url='https://github.com/nagareproject/services-redis',
    packages=find_packages(),
    zip_safe=False,
    setup_requires=['setuptools_scm'],
    use_scm_version=True,
    install_requires=['redis', 'nagare-server'],
    entry_points='''
        [nagare.commands]
        redis = nagare.admin.redis:Commands

        [nagare.commands.redis]
        info = nagare.admin.redis:Info
        clients = nagare.admin.redis:Clients
        config = nagare.admin.redis:Config
        size = nagare.admin.redis:Size

        [nagare.services]
        redis = nagare.services.redis:Redis
    '''
)
