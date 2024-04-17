FROM ubuntu
RUN apt update -y && apt install fortunes fortune fortune-mod cowsay netcat -y
WORKDIR /usr/games
COPY wisecow.sh .

ENV PATH="${PATH}:/usr/games"

EXPOSE 4499

CMD [ "bash", "wisecow.sh", "--port", "4499" ]
