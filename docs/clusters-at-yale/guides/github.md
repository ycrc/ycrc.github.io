# Version Control with GitHub

Whether developing large frameworks or simply working on small scripts, version control is an important tool to 
ensure that your work is never lost. 
We recommend using `git` for its flexibility and versatility.
Here we will cover the basics of version control and how to use `git` and GitHub to establish best-practices for 
research. 

## What is version control?

Version contol is an easy and powerful way to track changes to your work. 
This extends from code to writing documents (if using LaTeX/Tex). 
It produces and saves "tagged" copies of your project so that you don't need to worry about breaking your 
code-base.
This provides a "coding safety net" to let you try new features while retaining the ability to roll-back to a 
working version.

## What is `git` and how does it work?

Git is a tool that tracks changes to a file (or set of files) through a series of snapshots called "commits" or 
"revisions". 
These snapshots are stored in "repositories" which contain the history of all the changes to that file. 
This helps prevent repetative naming or `project_final_final2_v3.txt` problems. 
It acts as a record of all the edits, along with the ability to compare the current version to previous commits. 

## How to create a `git` repository

You can create a repository at any time by running the following commands:

```sh
cd /path/to/your/project

# initialize the repository
git init

# add files to be tracked
git add main.py input.txt 

# commit the files to the repository, creating the first snapshot
git commit -m "Initial Commit"
```

This sets up a repository containing a single snapshot of the project's two files.
We can then edit these files and commit the changes into a new snapshot:

```sh

# edit files
echo "changed this file" >> input.txt
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   input.txt

no changes added to commit (use "git add" and/or "git commit -a")
```
Finally, we can stage `input.txt` and then commit the changes:

```sh
# stage changes for commit
git add input.txt
git commit -m "modified input file"

```

## Configuring `git`

It's very helpful to configure your email and username with `git`:

```sh
git config --global user.name "Your Name"
git config --global user.email "your.email@yale.edu"
```
This will then tag your changes with your name and email when collaborating with people on a larger 
project. 

## Working with remote repositories on GitHub

We recommend using an off-site repository like [GitHub](https://github.com) that provides a secure and co-located 
backup of your local repositories. 

To start, create a repository on GitHub by going to <https://github.com/new> and providing a name and 
choose either public or private access.
Then you can connect your local repository to the GitHub repo (named `my_new_repo`):

```sh
git remote add origin git@github.com:user_name/my_new_repo.git
git push -u origin master
```

Alternatively, a repository can be created on GitHub and then cloned to your local machine:
```sh
$ git clone git@github.com:user_name/my_new_repo.git
Cloning into 'my_new_repo'...
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (3/3), done.

```
This creates a new directory (`my_new_repo`) where you can place all your code.


After making any changes and commiting them to the local repository, you can "push" them to a remote repository:

```sh
# commit to local repository
git commit -m "new changes"

# push commits to remote repository on GitHub
git push

```

## Educational GitHub

All students and research staff are able to request free Educational discounts from GitHub. 
This provides a "Pro" account for free, including unlimited private repositories. 

To get started, create a free GitHub account with your Yale email address. 
Then go to <https://education.github.com> and request the educational discount. 
It normally takes less than 24 hours for them to grant the discount.

Educational discounts are also available for teams and collaborations. 
This is perfect for a research group or collaboration and can include non-Yale affiliated people. 


## Resources and links

- [YCRC Version Control Bootcamp](https://research.computing.yale.edu/training/ycrc-bootcamps/version-control-git)
- [Educational GitHub](https://education.github.com)
- [GitHub's Try-it](http://try.github.io)
- [Instruqt Getting Started With Git](https://play.instruqt.com/public/topics/getting-started-with-git)

