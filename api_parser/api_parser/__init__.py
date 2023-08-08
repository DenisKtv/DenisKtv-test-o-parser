from __future__ import absolute_import, unicode_literals

import pymysql

from .celery_config import app as celery_app

__all__ = ('celery_app',)

pymysql.version_info = (1, 4, 6, "final", 0)
pymysql.install_as_MySQLdb()
