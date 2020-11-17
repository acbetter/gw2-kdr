# GW2 KDR

GW2 KDR is a online tool for checking the kill/death of each world per hour.

Coded by Saber Lily.1960 aka [acbetter@github](https://github.com/acbetter).

Powered by [Python](https://www.python.org/), [Vue.js](https://github.com/vuejs/vue) and [Day.js](https://github.com/iamkun/dayjs/). Thanks to [axios](https://github.com/axios/axios) and [Bulma](https://bulma.io/).

View Online Demo: [https://voidpin.com/tools/wvw-server-kdr/](https://voidpin.com/tools/wvw-server-kdr/)

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

## Server Deploy for Debian 10

You need prepare a web server. I use Debian 10 and Python 3.7.3 here.

Use these commands to check.

```bash
which python3
python3 -V

which pip3
pip3 -V
pip3 install requests
```

I use crontab for run this script per hour.

> In my Debian 10, cron is installed by default. However, if it is not installed on your machine, run the following few commands on the terminal with root privileges. [scource](https://vitux.com/how-to-setup-a-cron-job-in-debian-10/)

```bash
apt-get update
apt-get install cron
```

First of all, we need download the script.

```bash
cd ~
git clone https://github.com/acbetter/gw2-kdr.git
```

Then type command `crontab -e` to set up crontab tasks and type command `crontab -l` to check.

```bash
1 * * * * cd /path/to/script && /usr/bin/python3 kdr.py
3 * * * * yes | cp /path/to/script/matches.json /path/to/nginx/dir/matches.json
3 * * * * yes | cp /path/to/script/worlds.json /path/to/nginx/dir/worlds.json
```

For me, I use root account (not recommand, it's unsafe) and candy server at path `/var/www/api/` to deploy at [https://gw2skr.com/kdr.html](https://gw2skr.com/kdr.html).

```bash
1 * * * * cd /root/gw2-kdr/ && /usr/bin/python3 kdr.py
3 * * * * yes | cp /root/gw2-kdr/matches.json /var/www/api/matches.json
3 * * * * yes | cp /root/gw2-kdr/worlds.json /var/www/api/worlds.json
```

If you need clean up.

```bash
rm -rf kdr.py
rm -rf matches.json worlds.json
```

I use crontab for run this script per hour.

```bash
systemctl start cron
systemctl enable cron
systemctl status cron
```

## Server Deploy for CentOS 7

If you use CentOS 7, here's a way to install Python 3.7.x

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
pip3.7 install requests
```

I use crontab for run this script per hour.

```bash
yum install crontabs
systemctl start crond
systemctl enable crond
systemctl status crond
```

The rest is the same as Debian 10.

## Contributing

Pull requests are welcome.

For major changes, please open an issue first to discuss what you would like to change.

## License

[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)
