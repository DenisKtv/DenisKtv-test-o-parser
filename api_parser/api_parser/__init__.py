from __future__ import absolute_import, unicode_literals
from .celery_config import app as celery_app
import pymysql


__all__ = ('celery_app',)

pymysql.version_info = (1, 4, 6, "final", 0)
pymysql.install_as_MySQLdb()
