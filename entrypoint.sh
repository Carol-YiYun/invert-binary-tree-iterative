#!/bin/sh
if [ "$1" = "run" ]; then
    python -m source.main
else
    pytest -v
fi