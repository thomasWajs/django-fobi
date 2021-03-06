"""
- ``CSV_DELIMITER`` (string)
- ``CSV_QUOTECHAR`` (string)
"""

__title__ = 'fobi.contrib.plugins.form_handlers.db_store.settings'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2014 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'CSV_DELIMITER', 'CSV_QUOTECHAR',
)

from fobi.contrib.plugins.form_handlers.db_store.conf import get_setting

CSV_DELIMITER = get_setting('CSV_DELIMITER')
CSV_QUOTECHAR = get_setting('CSV_QUOTECHAR')
