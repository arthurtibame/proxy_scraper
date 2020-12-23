FROM python:3.6
LABEL maintainer="arthur.sl.lin@modovision.com"
COPY ./proxy_scraper /proxy_scraper
WORKDIR /proxy_scraper
RUN pip install -r requirements.txt
ENTRYPOINT [ "scrapy" ]
CMD [ "crawl proxy" ]