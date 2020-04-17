FROM python:3-slim

COPY requirements.txt /usr/local/src/
RUN pip install --no-cache-dir -r /usr/local/src/requirements.txt

COPY miniflux-init-db.py /usr/bin/miniflux-init-db

ENTRYPOINT ["/usr/bin/miniflux-init-db"]
