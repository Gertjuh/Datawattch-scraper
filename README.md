# Datawattch-scraper
A Python script to scrape data on the production of solar panels from the Datawattch website.
Version 2 is a working version that only retrieves the total Kwh delivered.
A new version must also contain the other data available on the Datawattch page.
I run this script on a Raspberry Pi v3 and use Cron to run it once every 10 minutes.
*/10 * * * * /usr/bin/python3 /home/pi/scraper_latest.py  >> /home/pi/scripts/script.log
