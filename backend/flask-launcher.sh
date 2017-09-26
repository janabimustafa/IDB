#!/usr/bin/env sh
gunicorn rest:app -b :5000 --reload