# Yale Center for Research Computing (YCRC) Documentation - Agent Rules & Guidelines

Welcome to the YCRC Documentation codebase! This workspace contains the source documentation for the Yale Center for Research Computing (hosted at [docs.ycrc.yale.edu](https://docs.ycrc.yale.edu)).

---

## 1. Project Overview & Architecture

- **Engine**: [MkDocs](https://www.mkdocs.org/) with [mkdocs-material](https://squidfunk.github.io/mkdocs-material/) theme.
- **Source Branch**: `src` (All source markdown files reside here in `docs/`).
- **Deployment Branch**: `master` (Contains compiled static HTML output managed by `mkdocs gh-deploy`).
- **Configuration**: Main site config and sidebar navigation are defined in `mkdocs.yml`.
- **Platform**: The project is based on [github pages](https://docs.github.com/en/pages) using [mkdocs](https://www.mkdocs.org/user-guide/deploying-your-docs/)

---

## 2. Workspace Branching & Workflow Rules

- **Branch Safety**:
  - Always work on the **`src`** branch.
  - **NEVER** edit files directly on the `master` branch.
- **Adding New Pages**:
  - Place new `.md` files in the appropriate subdirectory inside `docs/`.
  - Register the new page in [`mkdocs.yml`] under the `nav:` hierarchy.

---

## 3. Environment & Development Commands

### Environment Setup
- Python version: 3.10 / 3.12
- Conda environment: `mkdocs`
- Installation: `pip install -r requirements.txt`

### Build & Testing Commands
- **Local Development Server**:
  ```bash
  mkdocs serve
  ```
  Runs a live-reloading local web server to preview changes.

- **Deploy to GitHub Pages**:
  ```bash
  mkdocs gh-deploy
  ```
  Builds the site and pushes static assets to the `master` branch.

---

## 4. Documentation Style Guide

Follow the YCRC documentation standards for all edits and new content:

### Content Structure (Diátaxis Framework)
Categorize content into one of four types:
1. **Tutorials**: Learning-oriented lessons for beginners.
2. **How-To Guides**: Task-oriented step-by-step solutions to specific problems.
3. **Reference**: Technical descriptions of cluster hardware, software, and machinery.
4. **Explanation**: Discursive articles explaining concepts and architecture.

### Language & Tone
- Use active, consistent tense and direct address (e.g., *"You can run..."* instead of *"This can be run..."*).
- Avoid judgmental words like *"simply"*, *"just"*, *"obviously"*, or *"easily"*.

### Headings
- Every page **must** start with an `# H1 Title` at line 1.
- Use **Title Case** for all headings.
- Use base verb forms instead of `-ing` forms (e.g., `## Transfer Data` instead of `## Transferring Data`).

### Links & Filenames
- Use hyphenated lowercase for filenames (e.g., `job-scheduling.md`), no underscores or spaces.
- **Internal Links**: Omit the `.md` extension when linking to internal documentation pages (e.g., `[SSH Connection](/clusters-at-yale/access/ssh)`).

### Code Snippets & Fencing
- Always specify language identifier on code blocks (e.g., ````bash`).
- Do **not** include prompt indicators (`$`, `#`) in copyable shell code snippets unless clarifying node prompt contexts.
- Use realistic dummy values (e.g., `netid`, `job_12345`) rather than angle brackets `<option>`.
- Embed reusable snippet files from `docs/files/` using PyMdown snippets notation:
  ```markdown
  --8<-- "docs/files/example_job.sh"
  ```

### Naming Conventions
- Capitalize software names when referencing the product (e.g., Slurm, Conda, OpenOnDemand).
- Use backticks for command names (e.g., `sbatch`, `module load`, `conda`).
- Use abbreviated unit symbols for memory/storage (e.g., `4G`, `100G`, `2T`).
