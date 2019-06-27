# Contributing to FLOCX

FLOCX uses pull requests to add new features, patch bugs and address issues etc. 

There are multiple ways one can contribute a pull request, we recommend the following the workflow.

1. Clone the `master` of repository to your local repository.
2. Make a copy of the local repository on your computer: `git clone https://github.com/<yourGitHubUsername>/flocx`
        `
3. For every new PR create a new branch from the up to date master branch `git checkout -b <new feature name> master`
4. Save often, save small by doing `git commit --amend; git push -f`
    * This maintains a single commit per feature, unless the PR includes multiple big changes.
    * In case multiple big changes are included, make one commit per big change. 
5. Always keep your local master `origin/master`  in sync with the upstream repository. `upstream/master`

6. Once the patch is ready, create a Pull Request on the upstream repository. 

7. Once the review comments are addressed it will be merged with the master.


