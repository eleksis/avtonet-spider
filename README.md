What you need
$ sudo apt-get install python-dev python-pip python-virtualenv

How you get it working
$ cd <project_dir>
$ virtualenv -p python2 pyenv
$ source pyenv/bin/activate
$ pip install scrapy
$ scrapy crawl <spider>

To run periodicaly

$ chmod a+x scrapy.sh
$ crontab -e
> 0 * * * * /home/vito/Tech/avtonetspider/scrapy.sh
