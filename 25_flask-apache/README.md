# how-to :: DEPLOY A FLASK APP ON UBUNTU
---
## Overview
Guide to deploying a webapp onto your server ip address.

### Estimated Time Cost: 30 minutes

### Prerequisites:

- You will need to have created a droplet and downloaded Apache on it
- You will need to have created a user/know how to ssh as a user
- Install mod_wsgi, virtualEnvironment, python, and Flask

Deploying the flask app
1. cd /var/www (this is where you will create your directories)
2. Make a directory named whatever you want. In this case we use 'FlaskApp'
3. Create basic directories, setup the virtual environment, and make a flask app
4. We have to create a config file using this command
 ```
  sudo nano /etc/apache2/sites-available/FlaskApp.conf
```
5. Edit in the file and paste 
```
<VirtualHost *:80>
		ServerName IPADDRESS
		ServerAdmin admin@mywebsite.com
		WSGIScriptAlias / /var/www/FlaskApp/flaskapp.wsgi
		<Directory /var/www/FlaskApp/FlaskApp/>
			Order allow,deny
			Allow from all
		</Directory>
		ErrorLog ${APACHE_LOG_DIR}/error.log
		LogLevel warn
		CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>

```
6. Next we have to create a .wsgi file with these commands
```
cd /var/www/FlaskApp
sudo nano flaskapp.wsgi 
```
7. Paste in this code
```
#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/FlaskApp/")

from FlaskApp import app as application
application.secret_key = 'Add your secret key'

```
8. Finally restart apache2 to save this
```
sudo service apache2 restart 
```


### Resources
* https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps
---

Accurate as of (last update): 2022-01-19

#### Contributors:  
Justin Zou, pd2  
