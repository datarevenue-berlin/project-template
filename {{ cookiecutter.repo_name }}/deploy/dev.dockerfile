FROM drtools/base:dev
COPY ../requirements.txt /requirements.txt
RUN pip3 install -r requirements.txt