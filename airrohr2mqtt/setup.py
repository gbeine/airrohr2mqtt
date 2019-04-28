from setuptools import setup

setup(name='airrohr2mqtt',
      version='0.2',
      description='airrohr 2 MQTT bridge',
      url='https://github.com/gbeine/airrohr2mqtt',
      author='Gerrit',
      author_email='mail@gerritbeine.de',
      license='MIT',
      packages=['airrohr2mqtt'],
      requires=[
          'logging',
          'paho.mqtt',
          'pyyaml',
        ],
      zip_safe=False)
