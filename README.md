# pymongo-mongodb-university

To restore a database you must use the mongorestore command (this command must be part of your operative system's PATH environment variable).

Before executing this command you need to have a running mongod instance.

The mongorestore utility restores a binary backup created by mongodump. By default, mongorestore looks for a database backup in the dump/ directory.

First of all, in a shell, terminal or cmd window; navigate to the parent directory of the dump directory and execute the following command:
mongorestore dump
