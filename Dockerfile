FROM python:3.7-alpine3.9

MAINTAINER Thomas Maier <contact@thomas-maier.net>

RUN pip install bottle

COPY path_return_service.py /path_return_service.py

CMD ["python", "/path_return_service.py"]
