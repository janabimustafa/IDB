#!/usr/bin/env sh
echo "Populating db..."
sh seed.sh
exec gunicorn rest:app -b :5000 --reload