# GitHub Pages

## Personal Website

A personal website is a great way to build an online presence for both academic and professional activities.
We recommend using [GitHub Pages](https://guides.github.com/features/pages/) as a tool to maintain and host static websites and blogs.
Unlike other hosting platforms, the whole website can be written using [Markdown](https://www.markdownguide.org), a simple widely-used markup language.
GitHub provides a tutorial to get started with Markdown ([link](https://guides.github.com/features/mastering-markdown/)).

To get started, you're going to need a GitHub account.
You can follow the instructions on our [GitHub guide](./github.md) to set up a free account.
Once you have an account, you will need to create a repository for your website.
It's important that you name your repository `username.github.io`  where username is replaced with your actual account name (`ycrc-test` in this example).

![Create the repository](/img/ghpages_1.png)

Make sure to initialize the repo with a README, which will help get things started.
After clicking "Create" your repository will look like this:

![Empty repository](/img/ghpages_2.png)

From here, you can click on "Settings" to enable GitHub Pages publication of your site.
Scroll down until you see **GitHub Pages**:

![Settings](/img/ghpages_3.png)

GitHub provides a number of templates to help make your website look professional.
Click on "Choose a Theme" to see examples of these themes:

![Choose a theme](/img/ghpages_4.png)

Pick one that you like and click "Select theme".
Note, some of these themes are aimed at blogs versus project sites, pick one that best fits your desired style.
You can change this later, so feel free to try one out and see what you think.

After selecting your theme, you will be directed back to your repository where the README.md has been updated with some basics about how Markdown works and how you can start creating your website.

![Sample text](/img/ghpages_5.png)

Scroll down and commit these changes (leaving the sample text in place).

![Commit changes](/img/ghpages_6.png)

You can now take a look at how GitHub is rendering your site:

![Rendered website!](/img/ghpages_7.png)

That's it, this site is now hosted at [ycrc-test.github.io](http://ycrc-test.github.io)!
You now have a simple-to-edit and customize site that can be used to host your CV, detail your academic research, or showcase your independent projects.

## Project website

In addition to hosting a stand-alone website, GitHub Pages can be used to create pages for specific projects or repositories.
Here we will take an existing repository [amazing-python-project](https://github.com/ycrc-test/amazing_python_project) and add a GitHub Pages website on a new branch.

![Existing repository](/img/project_GHP_1.png)

Click on the Branch pull-down and create a new branch titled `gh-pages`:

![Create gh-pages branch](/img/project_GHP_2.png)

Remove any files from that branch and create a new file called `index.md`:

![Create index.md](/img/project_GHP_3.png)

Add content to the page using Markdown syntax:

![Add content](/img/project_GHP_4.png)

To customize the site, click on `Settings` and then scroll down to `GitHub Pages`:

![Settings](/img/project_GHP_5.png)

![GH Pages](/img/project_GHP_6.png)

Click on the `Theme Chooser` and select your favorite style:

![Choose your style](/img/project_GHP_8.png)

Finally, you can navigate to your website and see it live!

![Live page](/img/project_GHP_9.png)

## Conclusions

We have detailed two ways to add static websites to your work, either as a professional webpage or a project-specific site.
This can help increase your works impact and give you a platform to showcase your work.

### Further Reading

- [Jekyll](https://jekyllrb.com): the tool that powers GitHub Pages
- [GitHub Learning Lab](https://lab.github.com/githubtraining/github-pages)
- [Academic Pages](https://academicpages.github.io): forkable template for academic websites
- [Jekyll Academic](https://ncsu-libraries.github.io/jekyll-academic-docs/about/)

### Example GitHub Pages Websites

- [GitHub and Government](https://government.github.com), https://github.com/github/government.github.com
- [ElectronJS](https://electronjs.org), https://github.com/electron/electronjs.org
- [Twitter GitHub](https://twitter.github.io), https://github.com/twitter/twitter.github.io
- [React](https://reactjs.org), https://github.com/facebook/react
