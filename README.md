# airrohr2mqtt - An airrohr HTTP to MQTT bridge

## Installation

### Installation using Docker

```
docker run -it --rm --name airrohr2mqtt -v airrohr2mqtt.conf:/etc/airrohr2mqtt.conf docker.io/gbeine/airrohr2mqtt
```

### Installation using Podman

```
podman run -it --rm --name airrohr2mqtt -v airrohr2mqtt.conf:/etc/airrohr2mqtt.conf docker.io/gbeine/airrohr2mqtt
```

### Native installation with Python venv

The installation requires at least Python 3.9.

Philosophy is to install it under /usr/local/lib/airrohr2mqtt and control it via systemd.

```
cd /usr/local/lib
git clone https://github.com/gbeine/airrohr2mqtt.git
cd airrohr2mqtt
./install
```

The `install` script creates a virtual python environment using the `venv` module.
All required libraries are installed automatically.
Depending on your system this may take some time.

## Configuration

The configuration is located in `/etc/airrohr2mqtt.conf`.

Each configuration option is also available as command line argument.

- copy `airrohr2mqtt.conf.example`
- configure as you like

| option                   | default                  | arguments                  | comment                                                                                |
|--------------------------|--------------------------|----------------------------|----------------------------------------------------------------------------------------|
| `mqtt_host`              | 'localhost'              | `-m`, `--mqtt_host`        | The hostname of the MQTT server.                                                       |
| `mqtt_port`              | 1883                     | `--mqtt_port`              | The port of the MQTT server.                                                           |
| `mqtt_keepalive`         | 30                       | `--mqtt_keepalive`         | The keep alive interval for the MQTT server connection in seconds.                     |
| `mqtt_clientid`          | 'airrohr2mqtt'           | `--mqtt_clientid`          | The clientid to send to the MQTT server.                                               |
| `mqtt_user`              | -                        | `-u`, `--mqtt_user`        | The username for the MQTT server connection.                                           |
| `mqtt_password`          | -                        | `-p`, `--mqtt_password`    | The password for the MQTT server connection.                                           |
| `mqtt_topic`             | 'airrohr'                | `-t`, `--mqtt_topic`       | The topic to publish MQTT message.                                                     |
| `mqtt_tls`               | -                        | `--mqtt_tls`               | Use SSL/TLS encryption for MQTT connection.                                            |
| `mqtt_tls_version`       | 'TLSv1.2'                | `--mqtt_tls_version`       | The TLS version to use for MQTT. One of TLSv1, TLSv1.1, TLSv1.2.                       |
| `mqtt_verify_mode`       | 'CERT_REQUIRED'          | `--mqtt_verify_mode`       | The SSL certificate verification mode. One of CERT_NONE, CERT_OPTIONAL, CERT_REQUIRED. |
| `mqtt_ssl_ca_path`       | -                        | `--mqtt_ssl_ca_path`       | The SSL certificate authority file to verify the MQTT server.                          |
| `mqtt_tls_no_verify`     | -                        | `--mqtt_tls_no_verify`     | Do not verify SSL/TLS constraints like hostname.                                       |
| `http_host`              | 'localhost'              | `--http_host`              | The address to bind the HTTP server. Default is localhost                              |
| `http_port`              | 8080                     | `--http_port`              | The port of the HTTP server. Default is 8080                                           |
| `verbose`                | -                        | `-v`, `--verbose`          | Be verbose while running.                                                              |
| -                        | '/etc/airrohr2mqtt.conf' | `-c`, `--config`           | The path to the config file.                                                           |
| `items`                  | see below                | -                          | The configuration for the items on the KNX bus.                                        |

### airrohr configuration

Use the URL `http://<http_host>:<http_port>/airrohr/<sensor_id>` for the push notification.

## Running knx2mqtt

I use [systemd](https://systemd.io/) to manage my local services.

## Support

I have not the time (yet) to provide professional support for this project.
But feel free to submit issues and PRs, I'll check for it and honor your contributions.

## License

The whole project is licensed under BSD-3-Clause license. Stay fair.
