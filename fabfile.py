#!/usr/bin/python
from fabric.api import *
from fabric.context_managers import *

env.user = 'ubuntu'
env.hosts = ['111.231.81.104']
env.password = 'qwli96163'
u="root"
p="password"

def lump():

    run(" apt-get update")
    run(
        " apt-get install vim htop make mysql-server mysql-client nginx  git git-core  libpcre3 libpcre3-dev  memcached libmysqlclient-dev python-dev")
    run(" mkdir  /home/opt")
    put("./default","/etc/nginx/sites-available/default",use_=True)
    run(" service nginx restart")
    redis
    run(" wget http://download.redis.io/releases/redis-4.0.2.tar.gz;tar xzf redis-4.0.2.tar.gz;cd ./redis-4.0.2;make;make install;src/redis-server")

    put("./requirements.txt","/home")
    run(" pip install -r /home/requirements.txt")
    run(" apt install python-pip")
    run(" pip install --egg mysql-connector-python-rf")


    github
    run(" ssh-keygen -t rsa -b 4096 -C \"475098936@qq.com\";eval $(ssh-agent -s);ssh-add ~/.ssh/id_rsa")
    get("~/.ssh/id_rsa.pub","./id_rsa.pub")
    run(" git clone git@github.com:superdun/PureNewsServer.git /home/opt/PureNewsServer")

    sql
    put("./db","/home/db")
    run(" mysql -u%s -p%s < /home/db"%(u,p))
    #https://blog.csdn.net/u014710843/article/details/80276035
    supersisor
    run(" mkdir /home/log;touch /home/log/gunicorn.log;touch /home/log/gunicorn.err")
    put("./supervisor.conf","/home/supervisor.conf" ,use_=True)
    run(" supervisord -c /home/supervisor.conf")
    run(" supervisorctl -c /home/supervisor.conf status")



