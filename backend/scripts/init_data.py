#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging

from anyio import run

from backend.database.db_mysql import create_table

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def init() -> None:
    logger.info('Creating initial data')
    await create_table()
    logger.info('Initial data created')


if __name__ == '__main__':
    run(init)  # type: ignore
