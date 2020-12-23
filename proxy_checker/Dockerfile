FROM python:3.6
LABEL maintainer="arthur.sl.lin@modovision.com"
COPY . /proxy_checker
WORKDIR /proxy_checker
RUN pip install -r requirements.txt
ENTRYPOINT [ "python" ]
CMD [ "checker.py" ]