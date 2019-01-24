# Manage Permissions for Sharing

## Home Directories

**Do not give your home directory group write permissions. This will break your ability to log into the cluster.**  If you need to share something in your home directory, either move it your project directory or ask [hpc@yale.edu](mailto:hpc@yale.edu) for assistance.

## Shared Group Directories

Upon request we can setup directories for sharing scripts or data across your research group. These directories can either have read-only permissions for the group (such as for protecting programs) or read and write permissions for shared data directories. For example:

```
/gpfs/loomis/home/fas/nagai/programs
# or
/gpfs/loomis/project/fas/nagai/data
```

If interested, email us at [hpc@yale.edu] to request such a directory.

## Share With Specific Users or Other Groups

It can be very useful to create shared directories that can be read and written by multiple users, or all members of a group.  The linux command setfacl is very useful for this, but can be complicated to use.  Here are some simple scenarios.  We recommend that you create the shared directory in your project dir, rather than home.

### Share a Directory with All Members of a Group (e.g. othergroup)

```
mkdir shared
```

```
setfacl -m g:othergroup:rwx shared
```

```
setfacl -d -m g:othergroup:rwx shared
```

### Share a Directory with a Particular Person (e.g. netid aa111)

```
mkdir shared
```

```
setfacl -m u:aa111:rwx shared
```

```
setfacl -d -m u:aa111:rwx shared
```