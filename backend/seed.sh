#!/bin/bash
python -m data_collection.load_constants
python -m data_collection.serial_importer data_collection/serial.txt
python -m data_collection.serial_importer data_collection/decals.txt
python -m data_collection.serial_importer data_collection/supplemental_data.txt
python -m data_collection.serial_importer data_collection/paint_data.txt
python -m data_collection.relation_importer data_collection/relation.txt
python -m data_collection.relation_importer data_collection/body_decals.txt
python -m data_collection.serial_importer data_collection/players.txt