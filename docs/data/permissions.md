# Share with Cluster Users

## Home Directories

**Do not give your home directory group write permissions. This will break your ability to log into the cluster.**  If you need to share files currently located in your home directory, either move it your project directory or [contact us](/#get-help) for assistance finding an appropriate location.

### `project` and `scratch60` links in Home Directories

For convenience, we create a symlink, or shortcut, in every home directory called `project` and `~/scratch60` (and `palmer_scratch` on [Grace](/clusters/grace)) that go to your respective [storage spaces](/data/hpc-storage). However, if another user attempts to access any data via your symlink, they will receive errors related to permissions for your home space.

You can run `mydirectories` or `readlink - f dirname` (replace `dirname` with the one you are interested in) to get the "true" paths, which is more readily accesible to other users.

## Share Data within your Group

By default, all project, purchased allocation and scratch60 directories are readable by other members of your group. As long as they use the true path (not the shortcut your home directory, see above), no permission changes should be needed.

If you want to ensure all new files and directories you create have group *write* permission, add the following line to your `~/.bashrc` files:

```
umask 0002
```

### Shared Group Directories

Upon request we can setup directories for sharing scripts or data across your research group. These directories can either have read-only permissions for the group (so no one accidentally modifies something) or read and write permissions for all group members. If interested, [contact us](/#get-help) to request such a directory.

## Share With Specific Users or Other Groups

It can be very useful to create shared directories that can be read and written by multiple users, or all members of a group. The linux command `setfacl` is useful for this, but can be complicated to use. We recommend that you create a shared directory somewhere in your `project` or `scratch60` directories, rather than `home`. When sharing a sub-directory in your `project` or `scratch60`, you need first share your `project` or `scratch60`, and then share the sub-directory. Here are some simple scenarios.
    

### Share a Directory with All Members of a Group

To share a new directory called `shared` in your project directory with group `othergroup`:

```
setfacl -m g:othergroup:rx $(readlink -f ~/project)
cd ~/project
mkdir shared
setfacl -m g:othergroup:rwX shared
setfacl -d -m g:othergroup:rwX shared
```

### Share a Directory with a Particular Person

To share a new directory called `shared` with a person with netid `aa111`:

```
setfacl -m u:aa111:rx $(readlink -f ~/project)
cd ~/project
mkdir shared
setfacl -m u:aa111:rwX shared
setfacl -d -m u:aa111:rwX shared
```

If the shared directory already exists and contains files and directories, you should run the setfacl commands recursively, using -R:

```
setfacl -R -m u:aa111:rwX shared
setfacl -R -d -m u:aa111:rwX shared
```

Note that only the owner of a file or directory can run setfacl on it.

### Remove Sharing of a Directory

To remove a group `othergroup` from sharing of a directory called `shared`:

```
setfacl -R -x g:othergroup shared
```

To remove a person with netid `aa111` from sharing of a directory called `shared`:

```
setfacl -R -x u:aa111 shared
```
