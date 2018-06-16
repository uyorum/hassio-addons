ARG BUILD_FROM
FROM $BUILD_FROM

RUN apk add --no-cache tcpdump py-yaml py-pip py2-requests libressl
RUN pip --no-cache-dir install scapy

RUN wget https://raw.githubusercontent.com/uyorum/dash-ha/master/dash-ha.py -P /
COPY run.sh /
COPY json2yaml.py /

RUN chmod a+x /run.sh json2yaml.py dash-ha.py

CMD ["/run.sh"]
