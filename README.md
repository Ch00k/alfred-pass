# alfred-pass

Alfred Workflow for getting passwords from [pass](https://www.passwordstore.org) password manager.

The workflow uses `pass` command-line tool under the hood.

## Requirements

`pass` and Python 3 are required. To install both with Homebrew execute

```
$ brew install pass python3
```

The workflow assumes that the passwords storage directory is in `~/.password-store`.

# Installation

Download the latest release (`pass.alfredworkflow` file) from [Releases](https://github.com/Ch00k/alfred-pass/releases)
page, double-click on the downloaded file, and follow Alfred's instructions.

# Usage

In Alfred command line type `pass` followed by a filter term matching an account you want to get a password for. The
password will be copied to the clipboard in transient mode (i.e. it will *not* actually show up in clipboard
history).
