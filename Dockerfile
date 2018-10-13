FROM bamos/openface:latest

RUN apt-get update && apt-get install -y

# Flask
RUN pip install Flask 
RUN pip install flask_sqlalchemy

EXPOSE 8000 9000 5000