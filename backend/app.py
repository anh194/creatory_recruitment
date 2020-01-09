# -*- coding: utf-8 -*-

from admin import display_measurement
from admin.config import basedir
import logging

app = display_measurement.create_app()
app.logger.setLevel(logging.ERROR)

if __name__ == '__main__':
	print(str(basedir))
	app.run(host='0.0.0.0', port=8003, use_reloader=False)
