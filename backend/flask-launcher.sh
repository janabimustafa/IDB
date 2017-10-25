#!/usr/bin/env sh
sh seed.sh
gunicorn rest:app -b :5000 --reload