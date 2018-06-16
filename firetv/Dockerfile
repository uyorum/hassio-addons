ARG BUILD_FROM
FROM $BUILD_FROM

RUN apk add --no-cache swig libressl-dev python-dev libusb py-yaml py-flask py-pip build-base

RUN pip --no-cache-dir install adb==1.2.0
RUN pip --no-cache-dir install flask
RUN pip --no-cache-dir install https://pypi.python.org/packages/source/M/M2Crypto/M2Crypto-0.24.0.tar.gz

ARG FIRETV_VERSION
RUN pip install --no-cache-dir "firetv[firetv-server]==${FIRETV_VERSION}"

COPY run.sh /

COPY json2yaml.py /
RUN chmod a+x /run.sh json2yaml.py

CMD ["/run.sh"]
