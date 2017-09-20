#!/usr/bin/env python
from time import time

from .components import cli
from .components import java
from .components import nginx
from .components import stage
from .components import sanity
from .components import consul
from .components import python
from .components import manager
from .components import riemann
from .components import composer
from .components import logstash
from .components import rabbitmq
from .components import influxdb
from .components import syncthing
from .components import amqpinflux
from .components import mgmtworker
from .components import postgresql
from .components import restservice
from .components import manager_ip_setter

from .components.globals import set_globals
from .components.validations import validate_machine

from .logger import get_logger
from .utils.files import remove_temp_files

logger = get_logger('Bootstrap')

COMPONENTS = [
    manager,
    manager_ip_setter,
    nginx,
    python,
    postgresql,
    rabbitmq,
    restservice,
    influxdb,
    amqpinflux,
    riemann,
    java,
    consul,
    syncthing,
    stage,
    composer,
    logstash,
    mgmtworker,
    cli,
    sanity
]

START_TIME = time()


def _print_time():
    running_time = time() - START_TIME
    m, s = divmod(running_time, 60)
    logger.notice(
        'Finished in {0} minutes and {1} seconds'.format(int(m), int(s))
    )


def install():
    logger.notice('Installing Cloudify Manager...')
    validate_machine()
    set_globals()

    for component in COMPONENTS:
        component.install()

    remove_temp_files()
    logger.notice('Cloudify Manager successfully installed!')
    _print_time()


def configure():
    logger.notice('Configuring Cloudify Manager...')
    set_globals()

    for component in COMPONENTS:
        component.configure()

    remove_temp_files()
    logger.notice('Cloudify Manager successfully configured!')
    _print_time()


def remove():
    logger.notice('Removing Cloudify Manager...')

    for component in COMPONENTS:
        component.remove()

    logger.notice('Cloudify Manager successfully removed!')
    _print_time()


if __name__ == '__main__':
    install()
