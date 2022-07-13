#!/bin/bash
ebp-watch jb $1 &
live-server "$1/_bhild/html" &

