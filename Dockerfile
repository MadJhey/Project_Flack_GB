FROM python:3.8.10-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --no-cache --user -r requirements.txt

COPY . .

#COPY wait-for-postgres.sh .
#RUN chmod +x wait-for-postgres.sh

EXPOSE 5000
#CMD ["python3", "-m" , "flask", "init-db"]
#CMD ["python3", "-m" , "flask", "init-db"]
#CMD ["python3", "-m" , "flask", "create-users"]
#CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]
