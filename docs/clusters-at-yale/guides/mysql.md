# Mysql

[Mysql](https://www.mysql.com) is a popular relational database.  Because a database is usually thought of as a persistent service, it is not ordinarily run on HPC clusters, since
allocations on an HPC cluster are temporary.  If you need a persistent mysql database server, we recommend either installing mysql on a server in your
lab, or using ITS's [Spinup](https://spinup.internal.yale.edu) service.  In either case, the mysql server can be accessed remotely from the HPC clusters.

However, there are some use cases for running a mysql server on the cluster that do make sense.  For example, some applications store their data in a 
mysql database that only needs to run when the application runs.  Most instructions for installing mysql involve creating a persistent server and 
require admin privileges.  The instructions that follow walk you through the process of running a mysql server using singularity on a cluster compute node 
without any special privileges.  It uses a singularity [container](https://www.hpc.iastate.edu/guides/containers/mysql-server) 
developed by Robert Grandin at Iowa State (Thanks!) 

All of the following must be done on an allocated compute node.  Do not do this on the login node!

### Step 1: Create an installation directory somewhere, and cd to it

```
mkdir ~/project/mysql
cd ~/project/mysql
```

### Step 2: Create two config files

Put the following in ~/.my.cnf.  Note that you should change the password in both files
to something else.

```
[mysqld]
innodb_use_native_aio=0
init-file=${HOME}/.mysqlrootpw

[client]
user=root
password='my-secret-pw'
```

Put the following in ~/.mysqlrootpw
```
SET PASSWORD FOR 'root'@'localhost' = PASSWORD('my-secret-pw');
```

### Step 3: Create data directories for mysql
```
mkdir -p ${PWD}/mysql/var/lib/mysql ${PWD}/mysql/run/mysqld
```

### Step 4: Make a link to the mysql image file

The mysqld image file can be found under the apps tree on each cluster.
For example, on Grace:/gpfs/loomis/apps/singularity/img/mysql/mysqld-5.7.21.simg.  We recommend that you make a link to it in your mysql directory:

```
ln -s /gpfs/loomis/apps/singularity/img/mysql/mysqld-5.7.21.simg mysql.simg
```


### Step 5: Start the container.  Note that this doesn't actually start the service yet.

```
singularity instance start --bind ${HOME} \
    --bind ${PWD}/mysql/var/lib/mysql/:/var/lib/mysql \
    --bind ${PWD}/mysql/run/mysqld:/run/mysqld \
    ./mysql.simg mysql
```

To check that it is running:

```
singularity instance list
```

### Step 6: Start the mysqld server within the container

```
singularity run instance://mysql
```

You'll see lots of output, but at the end you should see a message like this
```
2022-02-21T17:16:21.104527Z 0 [Note] mysqld: ready for connections.
Version: '5.7.21'  socket: '/var/run/mysqld/mysqld.sock'  port: 3306  MySQL Community Server (GPL)
```

### Step 7: Enter the running container
```
singularity exec instance://mysql /bin/bash
```

Connect locally as root user while in the container, using the password you set in the config files in step 2.
```
Singularity> mysql -u root -p
Enter password:
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 3
Server version: 5.7.21 MySQL Community Server (GPL)

Copyright (c) 2000, 2018, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
```

Success!  The server is working!  Type exit to get out of mysql, but remain in the container:

### Step 8: Add a database user and permit it to login remotely
Next, in order to connect from outside the container, you need to add a user that is allowed to connect remotely and give that user permissions.   
This is one way to do that from the container shell. 

You should probably substitute your name for elmerfudd and a better password for mypasswd!

```
Singularity> mysql -e "GRANT ALL PRIVILEGES ON *.* TO 'elmerfudd'@'%' IDENTIFIED BY 'mypasswd' WITH GRANT OPTION"
Singularity> mysql -e "FLUSH PRIVILEGES"
```

Type exit to leave the container.  From that compute node, but outside the container, try connecting with:
```
mysql -u elmerfudd -h 127.0.0.1 -p
```

Now try connecting to that server from a different compute node by using the hostname of the node where the server is running (e.g. c22n01) instead of 127.0.0.1
```
mysql -u elmerfudd -h c22n01 -p
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

### Step 9 Shut the container down.

```
Singularity instance stop mysql
```

Now that everything is installed, the next time you want to start the server, you'll only need to do steps 5 (starting the container)
and 6 (starting the mysql server).

Note that you'll run into a problem if two mysql instances are run on the same compute node, since by default they each
try to use port 3306.  The simplest solution is to specify a non-standard port in your .my.cnf file:

```
[mysqld]
port=3310
innodb_use_native_aio=0
init-file=${HOME}/.mysqlrootpw

[client]
port=3310
user=root
password='my-secret-pw'
```



