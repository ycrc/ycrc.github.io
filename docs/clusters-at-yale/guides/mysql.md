# Mysql

[MySQL](https://www.mysql.com) is a popular relational database. It has a community-developed free-to-use variant [MariaDB](https://mariadb.org) that is recommended for non-commercial use.  Because a database is usually thought of as a persistent service, it is not ordinarily run on HPC clusters, since
allocations on an HPC cluster are temporary.  If you need a persistent mysql database server, we recommend either installing mysql on a server in your
lab, or using ITS's [Spinup](https://spinup.internal.yale.edu) service.  In either case, the mysql server can be accessed remotely from the HPC clusters.

Spinup has serverless database servers (MySQL, PostgreSQL, and Microsoft SQL) that can automatically sleep when not being accessed.  While asleep, you only pay for the data storage. 

However, there are some use cases for running a MySQL/MariaDB server on the cluster that do make sense.  For example, some applications store their data in a 
mysql database that only needs to run when the application runs.  Most instructions for installing MySQL involve creating a persistent server and 
require admin privileges.  The instructions that follow walk you through the process of running a MariaDB server using [Apptainer](/clusters-at-yale/guides/containers) on a cluster compute node 
without any special privileges.  It uses a container created from an existing [Docker Hub](https://hub.docker.com) template. If you want to use the original MySQL instead, the process is very similar. Contact the YCRC for assistance.

All of the following must be done on an allocated compute node.  Do not do this on the login node!

### Step 1: Create an installation directory somewhere, and cd to it

```
mkdir ~/project/mariadb
cd ~/project/mariadb
```
When working with containers, it is usually helpful to avoid directory "shortcuts" and use the real location of the directory. Since ${HOME}/project is a shortcut, switch to the actual location first:
```
cd `readlink -f ${PWD}`
```
This will place you in the "actual" location of your project directory, which you can check via the "pwd" command.

### Step 2: Create data directories for MariaDB
```
mkdir -p ${PWD}/var/lib/mysql ${PWD}l/run/mariadb
```

### Step 3: Create a MariaDB container

Generate a local image of the desired release of MariaDB from Docker Hub. You can select the "latest" tag  to get the newest release, but it is usually helpful to know what particular version you are running. In this example we are pulling down a Red Hat 9 (ubi9) image with MariaDB 11.7.2, to closely match with the client tools installed on the clusters (as of May 2026).

```
apptainer pull docker://mariadb:11.7.2-ubi9
```

This will create an image named mariadb_11.7.2-ubi9.sif in the current directory. For ease of use, or to allow switching versions, make a short link name:
```
ln -s mariadb_11.72.-ubi9.sif mariadb.sif
```

### Step 4: Start the container and the MariaDB server, with no initial root password

```
apptainer instance run --contain \
    --bind ${PWD}/var/lib/mysql/:/var/lib/mysql \
    --bind ${PWD}/run/mariadb:/run/mariadb \
    --env MARIADB_ALLOW_EMPTY_ROOT_PASSWORD=1 \
    ./mariadb.sif mariadb-instance
```

To check that it is running:

```
apptainer instance list
```
```
ps -fu ${USER} | grep mariadbd
```
There should be an instance listed, and "mariadbd" should be running on the node.

### Step 5: Enter MariaDB in the running container
```
apptainer exec --contain --bind ${PWD}/run:/run/mariadb instance://mariadb-instance mariadb -u root
```
```
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 6
Server version: 11.7.2-MariaDB MariaDB Server

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]>
```
Success!  The server is working!   You will now probably want to set a password for the server root account:
```
MariaDB [(none)]> ALTER USER 'root'@'%' IDENTIFIED BY 'my-secret-pw';
Query OK, 0 rows affected (0.002 sec)

MariaDB [(none)]> FLUSH PRIVILEGES;
Query OK, 0 rows affected (0.001 sec)

MariaDB [(none)]> exit
```
Check that you can now connect with the password you set.
```
apptainer exec --contain --bind ${PWD}/run:/run/mariadb instance://mariadb-instance mariadb -h 127.0.0.1 -u root -p
```
```
Enter password: 
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 11
Server version: 11.7.2-MariaDB MariaDB Server

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> 
```
You can also specify the password on the command line (e.g., "-pmy-secret-pw").

### Step 6: Add a database user and permit it to login remotely
Next, in order to connect from outside the container, you need to add a user that is allowed to connect remotely and give that user permissions. This is one way to do that from the container.

You should probably substitute your name for elmerfudd and a better password for mypasswd!

```
MariaDB [(none)]> GRANT ALL PRIVILEGES ON *.* TO 'elmerfudd'@'%' IDENTIFIED BY 'mypasswd' WITH GRANT OPTION;
Query OK, 0 rows affected (0.002 sec)

MariaDB [(none)]> FLUSH PRIVILEGES;
Query OK, 0 rows affected (0.001 sec)

MariaDB [(none)]> 
```

Type exit to leave the container.  From that compute node, but outside the container, try connecting with:
```
module load MariaDB/11.7.0-GCC-13.3.0
mysql -u elmerfudd -h 127.0.0.1 -p
```

Now try connecting to that server from a different compute node by using the hostname of the node where the server is running (e.g.r205u23n02 ) instead of 127.0.0.1
```
module load MariaDB/11.7.0-GCC-13.3.0
mysql -u elmerfudd -h r205u23n02 -p
```

While connected, you can try actually using the server in the usual way to create a database and table:
```
MySQL [(none)]> create database rob;
Query OK, 1 row affected (0.00 sec)

MySQL [(none)]> use rob
Database changed
MySQL [rob]> create table users (name VARCHAR(20), id INT);
Query OK, 0 rows affected (0.11 sec)

...
```

Success!  You've earned a reward of your choice!

### Step 7: Shut the container down.
In the compute node session where you initially launched the instance:
```
apptainer instance stop mariadb-instance
```

Now that everything is installed, the next time you want to start the server, you'll only need to do step 5 (running the container instance). If you set a root password, you can omit the --env setting for empty root password.

### Step 8: Set up default login credentials (optional)
For connections from outside the container, you can place the credentials for the account you are using into the file ${HOME}/.my.cnf
```
[client]
user=elmerfudd
password='mypasswd'
```
Then any invocations of mysql / mariadb from outside the container to automatically connect with elmerfudd's username and password.
### Troubleshooting
Note that you'll run into a problem if two mysql instances are run on the same compute node, since by default they each
try to use port 3306.  The simplest solution is to specify a non-standard port in your .my.cnf file:

```
[mariadbd]
port=3310

[client]
port=3310
user=elmerfudd
password='mypasswd'
```



