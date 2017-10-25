#!/bin/bash
python data_collection/rarity.py
python data_collection/serial_importer.py data_collection/serial.txt
python data_collection/serial_importer.py data_collection/supplemental_data.txt