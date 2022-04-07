FROM php:8.1.0-cli


RUN pecl install openswoole-4.11.0

COPY ./app /code

EXPOSE 9501

WORKDIR /code/app

RUN echo "extension=openswoole.so" > /usr/local/etc/php/php.ini
CMD ["php", "server.php"]
# CMD ["php", "--ri", "swoole"]
# CMD ["grep", "swoole.so", "/usr/local/etc/php/php.ini"]
# CMD ["php", "--ini"]
# CMD ["php", "-m"]