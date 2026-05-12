#!/bin/bash

LOG_DIR="/var/log"

echo "Iniciando limpieza de logs..."

sudo find $LOG_DIR -type f -name "*.log" -mtime +7 -exec rm -f {} \;

echo "Limpieza completada."
