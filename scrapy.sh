#!/bin/bash
#crontab -e (run hourly)
#0 * * * * /home/vito/Tech/avtonetspider/scrapy.sh
PATH=$PATH:/usr/local/bin
export PATH
cd /home/vito/Tech/avtonetspider/
source pyenv/bin/activate
scrapy crawl 330d
scrapy crawl oldtimer
