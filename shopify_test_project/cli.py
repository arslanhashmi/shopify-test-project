"""
Click commands to demo retry on failure / rate limits via multi-threading.
"""
import logging
from threading import Thread

import click

from client.utils import get_products, get_product_variant

logger = logging.getLogger(__name__)


def spawn_threads(target, num_threads):
    """
    This is for parallel API calls in threads to demo corresponding
    retries on failure / rate limits.
    """
    logger.info(
        "Spawning %d threads. Each invoking => '%s'",
        num_threads, target.__name__
    )
    for _ in range(num_threads):
        t = Thread(target=target)
        t.start()


@click.group(help="Shopify Client Demo CLI")
def cli():
    pass


@cli.command()
@click.option(
    '--num_threads',
    '-th',
    default=20,
    type=int,
    help='Number of threads each executing a target. Valid: >0',
    required=True
)
@click.option(
    '--target',
    '-tgt',
    default='tr',
    type=str,
    help='Target for each thread, valid ones are: ti(i.e. test iterator) / tr(i.e. test retry)',
    required=True
)
def run(num_threads, target):

    if not (num_threads and num_threads > 0):
        raise click.BadParameter('number of threads are not valid.')

    if not (target and target in ['ti', 'tr']):
        raise click.BadParameter(
            "target value is not valid. Choose from ['ti', 'tr']."
        )

    if target == 'ti':
        spawn_threads(target=get_products, num_threads=num_threads)
    elif target == 'tr':
        spawn_threads(target=get_product_variant, num_threads=num_threads)


if __name__ == "__main__":
    cli()
