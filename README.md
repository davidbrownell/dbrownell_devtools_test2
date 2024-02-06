# dbrownell_devtools_test2

---
## Action Items Before Deploying this Code

The code in this directory has been automatically generated based on a [cookiecutter](https://github.com/cookiecutter/cookiecutter) template. Additional steps must be completed before this code can be deployed.

`Please complete these steps and remove these instructions before deploying this code.`

### Gist to store dynamic build information
BugBug: Desc

#### Create the gist

1) Navigate to https://gist.github.com/
2) Create a file named `README.md` with the contents `Gist used bu GitHub Action workflows to store and retrieve dynamic information (oftentimes used to create and display badges).`
3) Click the `Create secret gist` button
4) Copy the gist id (this will be the hex string at the end of the url associated with the gist that was just created)

#### Save the gist id as a GitHub Actions Secret

1) Navigate to https://github.com/davidbrownell/dbrownell_devtools_test2/settings/secrets/actions
2) Click the `New repository secret` button in the `Repository secrets` section
3) Enter `GIST_ID` for `Name`
4) Copy the gist id for `Secret`
5) Click the `Add secret` button

#### Update this file with your gist id

1) In this file, replace `__YOUR_GIST_ID_HERE__` with the hex string copied above.

### PyPi Token
BugBug: Desc

#### Create the PyPi Token
1) Navigate to https://pypi.org
2) Login or Create an account (if necessary)
3) Click the `Account settings` link
4) Click the `Add API token` button
5) For `Token name`, enter `GitHub Publish Action (dbrownell_devtools_test2)`
6) For `Scope`, select one of the following values:
- `Entire account (all projects)` if the package has never been published before
- `Project: dbrownell-devtools-test2` if the package has been published before
7) Click the `Create token` button
8) Click the `Copy token` button


#### Save the token as a GitHub Actions Secret
1) Navigate to https://github.com/davidbrownell/dbrownell_devtools_test2/settings/secrets/actions
2) Click the `New repository secret` button in the `Repository secrets` section
3) Enter `PYPI_TOKEN` for `Name`
4) Copy the pypi token for `Secret`
5) Click the `Add secret` button

---

[![CI](https://github.com/davidbrownell/dbrownell_devtools_test2/actions/workflows/standard.yaml/badge.svg?event=push)](https://github.com/davidbrownell/dbrownell_devtools_test2/actions/workflows/standard.yaml)
[![Code Coverage](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/davidbrownell/__YOUR_GIST_ID_HERE__/raw/dbrownell_devtools_test2_coverage.json)](https://github.com/davidbrownell/dbrownell_devtools_test2/actions)
[![License](https://img.shields.io/github/license/davidbrownell/dbrownell_devtools_test2?color=dark-green)](https://github.com/davidbrownell/dbrownell_devtools_test2/blob/master/LICENSE.txt)
[![GitHub commit activity](https://img.shields.io/github/commit-activity/y/davidbrownell/dbrownell_devtools_test2?color=dark-green)](https://github.com/davidbrownell/dbrownell_devtools_test2/commits/main/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/dbrownell_devtools_test2?color=dark-green)](https://pypi.org/project/dbrownell-devtools-test2/)
[![PyPI - Version](https://img.shields.io/pypi/v/dbrownell_devtools_test2?color=dark-green)](https://pypi.org/project/dbrownell-devtools-test2/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/dbrownell_devtools_test2)](https://pypistats.org/packages/dbrownell-devtools-test2)

BugBug: Usage information here
