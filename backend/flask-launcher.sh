#!/usr/bin/env sh
sh seed.sh
exec gunicorn rest:app -b :5000 --reload