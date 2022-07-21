FROM openresty/openresty:buster
RUN apt-get update && apt-get install -y jq wireless-tools && apt-get clean && rm -rf /var/lib/{apt,dpkg,cache,log}
WORKDIR /app
COPY wifi.conf /etc/nginx/conf.d/default.conf
COPY signal .
COPY dummy /signal
EXPOSE 80