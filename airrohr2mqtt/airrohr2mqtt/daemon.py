
import time

from airrohr2mqtt import mqtt
from airrohr2mqtt import airrohr

class Daemon:

	def __init__(self, config):
		self._config = config
		self._init_mqtt()
		self._init_airrohr()

	def run(self):
		while True:
			self._airrohr.update_and_publish(self._mqtt)
			time.sleep(30)

	def _init_mqtt(self):
		self._mqtt = mqtt.Mqtt(self._config.mqtt())
		self._mqtt.connect()

	def _init_airrohr(self):
		self._airrohr = airrohr.airrohr(self._config.airrohr())
