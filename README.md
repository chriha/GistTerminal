GistTerminal
=========

GistTerminal is a small command line tool to search your public and private Gists.

See [CONTRIBUTING.md](https://github.com/chriha/GistTerminal/blob/master/CONTRIBUTING.md) for further information when contributing to this project.

## Getting started

### Requirements

Python 2.7+

### Install GistTerminal

1. 

### Set your GitHub API token

1. Go to your GitHub **Account settings**
2. click in the left navigation on **Applications**
3. and generate a new **Personal access token**
4. copy the new token and set it via
```shell
gist -t YOUR_TOKEN
```

## Usage

For initial help, just type `gist -h` in your command line

```
Usage:   gist [-b] [-c] [-h] [-l] [-o] [-s <search string>] [-t <GitHub API token>]
Options:
         -h                      Show this help
         -b                      Open a selected Gist in the Webbrowser
         -c                      Copy a selected Gist into your clipboard
         -l                      List all your Gists
         -s <search string>      Search for a string in all Gist descriptions
         -t <GitHub API token>   Set your GitHub API token to access your Gists

Legend: private Gist, public Gist, error
```


### External modules used

- [Pyperclip](http://coffeeghost.net/2010/10/09/pyperclip-a-cross-platform-clipboard-module-for-python/)
