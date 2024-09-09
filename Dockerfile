FROM python:3-alpine

WORKDIR /airrohr2mqtt

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY airrohr2mqtt .

CMD [ "python", "./airrohr2mqtt" ]
