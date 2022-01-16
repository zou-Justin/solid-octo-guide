# how-to :: CREATE A DIGITAL OCEAN DROPLET WITH UBUNTU AND APACHE
---
## Overview
Guide to creating an ubuntu 20.04 virtual machine ("droplet") and installing Apache2 web server on it.

### Estimated Time Cost: 30 minutes

### Prerequisites:

- You will need to have a Digital Ocean Account (Credit Card Needed)
- 
Creating a Droplet
1. First to create your droplet, choose all of the cheapest options and Ubuntu as your OS
2. Choose NYC as your Server
3. For your ssh key, you can use the ones you already have on your computer. If you want to access it:
    ```
    cat ~/.ssh/id_rsa.pub
    ```
    and then copy and paste it in
4. Click Create!

Accessing the server and installing
1. First you should ssh as a root user
    ```
   ssh root@ServerIP
    ```
2. Then you would create a user once you're in the server
    ```
    adduser Name
    ```
3. Once you create your password you can then use  ```su Name``` to switch to the user and start using sudo commands to install packages.

### Resources
* https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-on-ubuntu-20-04
* https://www.digitalocean.com/community/questions/error-permission-denied-publickey-when-i-try-to-ssh
* https://www.digitalocean.com/community/questions/secure-ubuntu-server-for-non-root-user-using-only-ssh-keys?answer=22286
* https://phoenixnap.com/kb/ssh-permission-denied-publickey
* https://www.digitalocean.com/community/tutorials/how-to-create-a-new-sudo-enabled-user-on-ubuntu-18-04-quickstart
* https://www.digitalocean.com/docs/droplets/how-to/
* https://www.digitalocean.com/community/questions/error-permission-denied-publickey-when-i-try-to-ssh?answer=44730
* https://www.digitalocean.com/docs/droplets/how-to/connect-with-ssh/putty/
* https://www.digitalocean.com/docs/droplets/how-to/add-ssh-keys/create-with-openssh/
* https://www.digitalocean.com/docs/droplets/how-to/connect-with-ssh/openssh/

(please verify ; some of these are old links)

---

Accurate as of (last update): 2022-01-16

#### Contributors:  
Justin Zou, pd2  
