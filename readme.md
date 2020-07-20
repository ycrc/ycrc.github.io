# Readme

All the source files for the site are stored in the branch `src`. **Never** directly modify files in the `master` branch. We use [mkdocs](https://www.mkdocs.org/) to build the site; the required python packages are in `requirements.txt`.


## Setup

* Clone the repo from `https://github.com/ycrc/ycrc.github.io`
* Switch to the src branch. DO NOT make changes the master branch, it is for the compiled site only: `git checkout src`

* Setup your Python environment

``` bash
conda create --name mkdocs python=3.7
source activate mkdocs
pip install -r requirements.txt
```

## Deployment Procedure

### Test

To test out changes you've made, run:

``` bash
mkdocs serve
```

This allows you to proofread and see your changes with formatting without affecting the live version of the site.

### Commit & Push

Make sure to commit and push your changes on the `src` branch to github.

### Deploy

To deploy your local changes to the site (from the root directory of the repo):

``` bash
mkdocs gh-deploy
```

## Add a New Page

If your contribute a new page (as opposed to editing an existing one) and want it to show up in the navigation sidebar, you need to edit the `mkdocs.yml` file in the root of this branch and add the page to the `nav:` section. The filename (without the .md) will be the url location and the page title (what shows in the sidebar) will be the first H1 mkdocs finds on your page -- so choose wisely.

## Style Guide

### Headings

* Always include an H1 at the top a page
* In headings, use the base form of a verb instead of the -ing form. E.g "Transfer Data" vs "Transferring Data"
* Headings should always be title case

### Pages, Filenames and Links

* Filenames for pages should have dashes, no underscores, for whitespace.
* When linking to another internal page, don't include the `.md` file extension. We have experienced inconsistent behavior with it.
* This: `See our [X11 forwarding documentation](/cluster-at-yale/access/x11) for instructions.` Not this `See our [X11 forwarding](/cluster-at-yale/access/x11) documentation for instructions.` or this `See our [X11 forwarding Documentation](/cluster-at-yale/access/x11) for instructions.`
* `Guides` subpages are in alphabetical order.

### Code Snippets

* Specify the language when when using code fencing (i.e. ```).  This will provide proper code coloring.

All multi-line code formatted text in the docs can easily be copy/pasted to someone's command prompt. With this in mind,

* Don't include the command prompt (e.g. `$`) in example commands, unless you trying to make a clarification about what nodes you are on.
* Show examples with dummy values rather than using `[varname]` or `<option>` . The failure messages will be more useful, and redirects can be destructive.
* If you provide a file worth downloading and also display it, place it in `docs/files` and use [https://facelessuser.github.io/pymdown-extensions/extensions/snippets/#snippets-notation](snippets) to include it. 

example from `docs/clusters-at-yale/job-scheduling.md`:

~~~ markdown

Here is an example submission script that prints some job information and exits:

``` bash
--8<-- "docs/files/example_job.sh"
```

Save [this file](/files/example_job.sh) as `example_job.sh`, then submit it with:

~~~



### Other Conventions

* When referring to software (e.g. Slurm or Conda), capitalize the name of the software (unless it really isn't correct, eg "iOS"). If you are referring to the associated command (e.g. `conda`), place the command in backticks.
* When specifying gigabytes/gibibytes, just use the first letter (e.g. G or T), to avoid confusing between the two. A description of our convention is described in storage documentation pages (we generally use gibibytes everywhere).
