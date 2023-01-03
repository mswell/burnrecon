FROM python:3.12.0a3-slim

COPY --from=golang:1.18.2-bullseye /usr/local/go/ /usr/local/go/

WORKDIR /root

ENV PATH="/usr/local/go/bin:${PATH}"

ENV GOPATH /go

ENV PATH $GOPATH/bin:$PATH

RUN mkdir -p "$GOPATH/src" "$GOPATH/bin" && chmod -R 777 "$GOPATH"
RUN apt update && apt install -y libpcap-dev build-essential

COPY install_hacktools.sh /root

RUN chmod +x /root/install_hacktools.sh

RUN ./install_hacktools.sh

COPY requirements.txt .

RUN pip install -r requirements.txt




