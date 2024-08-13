#!/bin/bash

BACKUP_DIR="/backup"
BORG_REPO="/borg-repo"
DB_HOST="db"
DB_USER="postgres"
DB_PORT="5432"
DB_PASSWORD="admin"

export PGPASSWORD=$DB_PASSWORD

# Initialize the Borg repository if not already initialized
if [ ! -d "$BORG_REPO" ] || [ ! "$(ls -A $BORG_REPO)" ]; then
    echo "Initializing Borg repository at $BORG_REPO"
    borg init --encryption=none $BORG_REPO
else
    echo "Borg repository already initialized."
fi

while true; do
    TIMESTAMP=$(date +"%Y%m%d%H%M%S")
    SQL_DUMP="${BACKUP_DIR}/backup_${TIMESTAMP}.sql"

    echo "Creating SQL dump: ${SQL_DUMP}"

    # Create an SQL dump of the database via TCP/IP
    pg_dumpall -h $DB_HOST -U $DB_USER -p $DB_PORT -f $SQL_DUMP

    if [ -f "$SQL_DUMP" ]; then
        echo "SQL dump created: ${SQL_DUMP}"

        # Back up with Borg
        echo "Backing up with Borg: $SQL_DUMP"
        borg create --stats --compression lz4 $BORG_REPO::backup_$TIMESTAMP $SQL_DUMP

        echo "Backup completed."

        # You can uncomment the next line to prune old backups
        # echo "Pruning old backups..."
        # borg prune --keep-daily=7 --keep-weekly=4 --keep-monthly=6 $BORG_REPO

        echo "Backup completed. Waiting for 1 hour..."
    else
        echo "SQL dump failed, skipping backup."
    fi

    # Wait for 1 hour (3600 seconds)
    sleep 3600
done
