# GW2 KDR

GW2 KDR is a online tool for checking the kill/death of each world per hour.

Coded by Saber Lily.1960 (acbetter@github). 

Powered by [Python](https://www.python.org/), [Vue.js](https://github.com/vuejs/vue) and [Day.js](https://github.com/iamkun/dayjs/). Thanks to [axios](https://github.com/axios/axios) and [Bulma](https://bulma.io/).

## Debug

You need install Python 3.7.x first. The script have some bugs in Python 3.6.x.

```bash
pip install requests
```

[Running a simple local HTTP server](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/set_up_a_local_testing_server)

```bash
# If Python version returned above is 3.X
python3 -m http.server
# On windows try "python" instead of "python3"
# If Python version returned above is 2.X
python -m SimpleHTTPServer
```

## Server Deploy

You need prepare a web server. I use CentOS and Python 3.7.6 here.

```bash
yum update -y
yum install wget
yum install gcc openssl-devel bzip2-devel libffi-devel
cd /usr/src
wget https://www.python.org/ftp/python/3.7.6/Python-3.7.6.tgz
tar xzf Python-3.7.6.tgz
cd Python-3.7.6
./configure --enable-optimizations
make altinstall
rm /usr/src/Python-3.7.6.tgz
```

And use these commands to check.

```bash
python3.7 -V
pip3.7 -V
```

I use crontab for run this script per hour.

```bash
yum install crontabs
systemctl start crond
systemctl enable crond
systemctl status crond
```

Then type command `crontab -e` to set up crontab and type command `crontab -l` to check.

```bash
0 * * * * cd /path/to/script && python3.7 kdr.py
5 * * * * yes | cp /path/to/script/matches.json /path/to/nginx/dir/matches.json
5 * * * * yes | cp /path/to/script/worlds.json /path/to/nginx/dir/worlds.json
```

For me, I use root account (not recommand, it's unsafe) and nginx server at path `/www/gw2skr/` to deploy at [https://gw2skr.com/kdr.html](https://gw2skr.com/kdr.html).

```bash
0 * * * * cd /root && python3.7 kdr.py
5 * * * * yes | cp /root/matches.json /www/gw2skr/matches.json
5 * * * * yes | cp /root/worlds.json /www/gw2skr/worlds.json
```

If you need clean up.

```bash
rm -rf kdr.py
rm -rf matches.json worlds.json
```

## Contributing

Pull requests are welcome.

For major changes, please open an issue first to discuss what you would like to change.

## License

[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)