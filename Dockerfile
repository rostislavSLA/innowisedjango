FROM python:3.9.5

WORKDIR .

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

#EXPOSE 5000

#CMD [ "python", "./app.py" ]