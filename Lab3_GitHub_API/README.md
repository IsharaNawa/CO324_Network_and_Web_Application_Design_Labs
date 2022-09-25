# CO324 Lab 3: Exploring the GitHub API with Requests

## Objective

Use command-line tools to make HTTP requests to various APIs. At the end of the lab, you should be able to
* Use APIs via the Requests 3 Python module
* Set up authentication and sessions.
* Understand the difference between various HTTP request methods (verbs.)
* Be able to interpret HTTP responses and status codes.
* Awareness of common HTTP headers. 

## Preparation
Install Python version 3.7 or newer on your computer. These instructions assume a Linux environment. If you prefer to use Windows, follow these [instructions to install WSL2.](https://docs.microsoft.com/en-us/windows/wsl/install-win10) Run the following commands in a shell in this lab’s working directory. Change the python version number appropriately.
1. Refer to this for more information about [pipenv](https://docs.python-guide.org/dev/virtualenvs/).
```bash
pip3 install pipenv
pipenv install requests --python 3.8
pipenv shell
```

2. Create a Github account if you have not already done so. Log in and create a Personal API token (PAT) that you will use to authenticate yourself: [Personal Access Tokens](https://github.com/settings/tokens). Copy the generated token to a text file.

3. Install a [REST client](https://insomnia.rest/).

## Instructions
* Use the **Requests 3 module only** with standard built-in modules in Python to complete these exercises.
* Put the solutions to coding exercises for the files in `src/` directory.
* **Put your E Number as a comment** in top of each source file.
* **DO NOT** change any code in `test/` directory.

## References
* [Using the Requests Library in Python](https://www.pythonforbeginners.com/requests/using-requests-in-python/)
* [Python’s Requests Library (Guide)](https://realpython.com/python-requests/)
* [Requests III: HTTP for Humans and Machines, alike.](https://3.python-requests.org/)
* [GitHub REST API](https://docs.github.com/en/rest/guides)

## Exercises
Exercises can be found in each Question folder in the `src/`.