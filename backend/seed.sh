#!/bin/bash
python -m data_collection.rarity
python -m data_collection.serial_importer data_collection/serial.txt
python -m data_collection.serial_importer data_collection/supplemental_data.txt
python -m data_collection.serial_importer data_collection/paint_data.txt
python -m data_collection.crateItemRelation
python -m data_collection.serial_importer data_collection/players.txt