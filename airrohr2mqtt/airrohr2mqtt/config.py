import yaml
import logging
import logging.config

class Config:
	"""Class for parsing airrohr2mqtt.yaml."""
	
	def __init__(self):
		"""Initialize Config class."""
		logging.config.fileConfig('logging.conf')
		self._mqtt = {}
		self._airrohr = {}
	
	
	def read(self, file='airrohr2mqtt.yaml'):
		"""Read config."""
		logging.debug("Reading %s", file)
		try:
			with open(file, 'r') as filehandle:
				config = yaml.load(filehandle)
				self._parse_mqtt(config)
				self._parse_airrohr(config)
		except FileNotFoundError as ex:
			logging.error("Error while reading %s: %s", file, ex)


	def _parse_mqtt(self, config):
		"""Parse the mqtt section of airrohr2mqtt.yaml."""
		if "mqtt" in config:
			self._mqtt = config["mqtt"]
		if not "host" in self._mqtt:
				raise ValueError("MQTT host not set")
		if not "port" in self._mqtt:
				raise ValueError("MQTT port not set")
		if not "user" in self._mqtt:
				raise ValueError("MQTT user not set")
		if not "password" in self._mqtt:
				raise ValueError("MQTT password not set")
		if not "topic" in self._mqtt:
				raise ValueError("MQTT topic not set")


	def _parse_airrohr(self, config):
		"""Parse the airrohr section of airrohr2mqtt.yaml."""
		if "airrohr" in config:
			self._airrohr = config["airrohr"]
		if not "host" in self._airrohr:
				raise ValueError("airrohr host not set")
		if not "port" in self._airrohr:
				raise ValueError("airrohr port not set")
		if not "sensors" in self._airrohr:
				raise ValueError("airrohr sensors not set")
		for item in self._airrohr["sensors"]:
			if not "id" in item:
				raise ValueError("Missing id for airrohr sensor")


	def mqtt(self):
		return self._mqtt

	def airrohr(self):
		return self._airrohr
