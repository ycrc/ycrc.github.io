# Readme

## Deployment Procedure

## Style Guide

### Headings

- Always include an H1 at the top a page
- In headings, use the base form of a verb instead of the -ing form. E.g "Transfer Data" vs "Transferring Data"
- Headings should always be title case

### Pages, Filenames and Links

- filenames for pages should have dashes, no underscores, for whitespace.
- When linking to another internal page, don't include the `.md` file extension. We have experienced inconsistent behavior with it.
- This: `See our [X11 forwarding documentation](/cluster-at-yale/access/x11) for instructions.` Not this `See our [X11 forwarding](/cluster-at-yale/access/x11) documentation for instructions.` or this `See our [X11 forwarding Documentation](/cluster-at-yale/access/x11) for instructions.`
- `Guides` subpages are in alphabetical order.

### Code Snippets

- When using code fencing (e.g. ```), specify the langauge after the first set of backticks, if applicable.  This will provide proper code coloring.
- When giving an example of a command, don't include the command prompt (e.g. `$`) unless you trying to make a clarification about what nodes you are on.

### Other Conventions

- When referring to software (e.g. Slurm or Conda), capitalize the name of the software (unless it really isn't correct, eg "iOS"). If you are referring to the associated command (e.g. `conda`), place the command in backticks.
- When specifying gigabytes/gibibytes, just use the first letter (e.g. G or T), to avoid confusing between the two. A description of our convention is described in storage documentation pages (we generally use gibibytes everywhere).
