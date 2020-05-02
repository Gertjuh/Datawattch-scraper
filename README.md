# Datawattch-scraper solarpanel data to MQTT
Two Python scripts to scrape data on the production of solar panels from the Datawattch website (https://app.datawattch.com/app)
Version 2 of the scripts are the working versions that retrieve both current Watts delivered as the totals up till the moment the script is run.

I run these scripts on a Raspberry Pi v3 using cron.

*/6 4-23 * * * /usr/bin/python3 /home/pi/scraper_now.py  >> /home/pi/logs/scraper_now.log
*/14 4-23 * * * /usr/bin/python3 /home/pi/scraper_totals.py >> /home/pi/logs/scraper_totals.log
56 23 * * * /usr/bin/python3 /home/pi/scraper_totals.py >> /home/pi/logs/scraper_totals.log

I send the data via MQTT to Home Assistant. I then save historical data to InfluxDB and visualize it with Grafana. See the Dashboard in de Wiki pages.


Disclaimer: I am not a Python developer or an expert on building Python scripts. But maybe I am a skilled Google search user ;-)
