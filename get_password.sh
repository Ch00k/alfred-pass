#!/usr/bin/env bash

set -e

pass show "$1" | head -1 | tr -d '\n'
osascript -e 'display notification "Copied passowrd to clipboard" with title "pass"'
