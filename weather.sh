#!/usr/bin/env bash

dir="$1"
source "$dir/.venv/bin/activate"
python "$dir/weather.py" "$dir"
