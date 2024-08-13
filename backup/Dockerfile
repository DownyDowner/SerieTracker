FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    borgbackup \
    postgresql-client \
    && apt-get clean

COPY backup.sh /usr/local/bin/backup.sh
RUN chmod +x /usr/local/bin/backup.sh

RUN mkdir -p /backup /borg-repo

CMD ["/usr/local/bin/backup.sh"]
