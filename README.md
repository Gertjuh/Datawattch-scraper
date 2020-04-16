# Datawattch-scraper to MQTT
A Python script to scrape data on the production of solar panels from the Datawattch website.
Version 2 is a working version that only retrieves the total Kwh delivered.
A new version must also contain the other data available on the Datawattch page.
I run this script on a Raspberry Pi v3 and use Cron to run it once every 10 minutes.
*/10 * * * * /usr/bin/python3 /home/pi/scraper_latest.py  >> /home/pi/scripts/script.log

I send the data via MQTT to Home Assistant.
I hav this in my sensors.yaml file:

# Zonnepanelen
sensor:
  - platform: "mqtt"
    name: Geleverd vandaag
    icon: "mdi:solar-panel"
    state_topic: "zigbee2mqtt/solar"
    unit_of_measurement: "Kwh"
    qos: 1
    value_template: '{{ value_json }}'
  - platform: template
    sensors:
      solar_today_lastchanged:
        value_template: >
          {% set values = [
            states.sensor.geleverd_vandaag.last_changed,
            ] %}
          {{ values | min }}
        device_class: timestamp

Work in progress:
1) build a second script to scrape the actual Watts delivered by the panels and run it every 5 min.
2) change the total_today script to run once a day.

Disclaimer: I am no Python developer or an expert on building Python scripts. But maybe I am a skilled Google search user ;-)
