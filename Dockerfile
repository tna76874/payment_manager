FROM ghcr.io/tna76874/payment_managerbase:latest

# CREATE USER
RUN groupadd -r -g 1033 worker && \
    useradd -r -g worker -u 1033 -d /home/worker -s /bin/bash worker

USER worker
WORKDIR /home/worker

# COPY FILEs
COPY --chown=worker:worker server /home/worker

# ENTRY
EXPOSE 5000

RUN chmod +x /home/worker/entrypoint.sh

CMD ["sh", "-c", "/home/worker/entrypoint.sh"]
