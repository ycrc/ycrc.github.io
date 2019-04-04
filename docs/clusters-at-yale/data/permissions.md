# Manage Permissions for Sharing

## Home Directories

**Do not give your home directory group write permissions. This will break your ability to log into the cluster.**  If you need to share something in your home directory, either move it your project directory or ask [hpc@yale.edu](mailto:hpc@yale.edu) for assistance.

## Shared Group Directories

Upon request we can setup directories for sharing scripts or data across your research group. These directories can either have read-only permissions for the group (so no one accidentally modifies something) or read and write permissions for shared data directories.

If interested, email us at [hpc@yale.edu](mailto:hpc@yale.edu) to request such a directory.

## Share With Specific Users or Other Groups

It can be very useful to create shared directories that can be read and written by multiple users, or all members of a group.  The linux command `setfacl` is useful for this, but can be complicated to use.  Here are some simple scenarios.  We recommend that you create a shared directory somewhere in your `project` or `scratch60` directories, rather than `home`.

!!!warning
    Your `~/project` and `~/scratch60` directories are actually symlinks (shortcuts) to elsewhere on the filesystem. Either run `mydirectories` or `readlink - f dirname` (replace `dirname` with the one you're interested in) to get their true paths. Give these true to people you are sharing with.

### Share a Directory with All Members of a Group

To share a new directory called `shared` with group `othergroup`:

```
mkdir shared
setfacl -d -m g:othergroup:rwx shared
```

### Share a Directory with a Particular Person

To share a new directory called `shared` with a person with netid `aa111`:

```
mkdir shared
setfacl -d -m u:aa111:rwx shared
```
