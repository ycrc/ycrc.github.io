# Manage Permissions for Sharing

## Home Directories

**Do not give your home directory group write permissions. This will break your ability to log into the cluster.**  If you need to share something in your home directory, either move it your project directory or ask [hpc@yale.edu](mailto:hpc@yale.edu) for assistance.

## Shared Group Directories

Upon request we can setup directories for sharing scripts or data across your research group. These directories can either have read-only permissions for the group (so no one accidentally modifies something) or read and write permissions for shared data directories.

If interested, email us at [hpc@yale.edu](mailto:hpc@yale.edu) to request such a directory.

## Share With Specific Users or Other Groups

It can be very useful to create shared directories that can be read and written by multiple users, or all members of a group.  The linux command `setfacl` is useful for this, but can be complicated to use. We recommend that you create a shared directory somewhere in your `project` or `scratch60` directories, rather than `home`. When sharing a sub-directory in your `project` or `scratch60`, you need first share your `project` or `scratch60`, and then share the sub-directory. Here are some simple scenarios. 

!!!warning
    Your `~/project` and `~/scratch60` directories are actually symlinks (shortcuts) to elsewhere on the filesystem. Either run `mydirectories` or `readlink - f dirname` (replace `dirname` with the one you are interested in) to get their true paths. Otherwise you will receive errors related to read permissions for your home-space.

### Share a Directory with All Members of a Group

To share a new directory called `shared` in your project directory with group `othergroup`:

```
setfacl -m "g:othergroup:rx" $(readlink -f ~/project)
cd ~/project
mkdir shared
setfacl -m "g:othergroup:rwx" shared
```

### Share a Directory with a Particular Person

To share a new directory called `shared` with a person with netid `aa111`:

```
setfacl -m "u:aa111:rx" $(readlink -f ~/project)
cd ~/project
mkdir shared
setfacl -m "u:aa111:rwx" shared
```

### Remove Sharing of a Directory

To remove a group `othergroup` from sharing of a directory called `shared`:

```
setfacl -R -x "g:othergroup" shared
```

To remove a person with netid `aa111` from sharing of a directory called `shared`:

```
setfacl -R -x "u:aa111" shared
```
