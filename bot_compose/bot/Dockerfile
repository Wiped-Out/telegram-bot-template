FROM python:3.9
WORKDIR /bot

COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD cd src && sleep 5 && python3 main.py
