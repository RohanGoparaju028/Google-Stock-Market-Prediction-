FROM python:3.14.3-trixie
ENV PATH="/usr/local/bin:$PATH"
WORKDIR /app # WORKDIR creates a directory called an app and manages what are thew changes the container from that folder 

COPY requirment.txt .
RUN pip install -r requirment.txt
