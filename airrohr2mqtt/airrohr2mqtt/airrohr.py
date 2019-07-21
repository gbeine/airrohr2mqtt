
import json
import urllib.request

class airrohr:

	def __init__(self, config):
		self._config = config
		self._init_sensors()
		self._init_url()


	def update_and_publish(self, mqtt):
		data = self._update()

		mqtt.publish("software_version", data["software_version"])
		mqtt.publish("age", data["age"])
		for value_type, value in data["data"].items():
			topic = self._sensors[value_type]
			mqtt.publish(topic, value)

	def _init_sensors(self):
		self._sensors = {}
		for item in self._config["sensors"]:
			if not "id" in item:
				raise ValueError("Missing id for airrohr device")
			self._sensors[item["id"]] = item["id"]


	def _init_url(self):
		self._url = "http://{}:{}/data.json".format(self._config["host"], self._config["port"])


	def _update(self):
		json = self._fetch_json()

		data = {}

		if not "software_version" in json:
			raise ValueError("Missing software_version in airrohr data")
		if not "age" in json:
			raise ValueError("Missing age in airrohr data")
		if not "sensordatavalues" in json:
			raise ValueError("Missing airrohr sensordatavalues")

		data["software_version"] = json["software_version"]
		data["age"] = json["age"]
		data["data"] = {}

		for item in json["sensordatavalues"]:
			if not "value_type" in item:
				continue
			if not "value" in item:
				continue
				
			data["data"][item["value_type"]] = item["value"]

		return data


	def _fetch_json(self):
		try:
			request = urllib.request.urlopen(self._url)
			return json.loads(request.read().decode())
		except urllib2.URLError, err:
			print "Some other error happened:", err.reason
