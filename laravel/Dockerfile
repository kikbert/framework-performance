FROM php:8.1.0-cli

COPY ./app /code

EXPOSE 8000

WORKDIR /code/app

CMD ["php", "artisan", "serve", "--host=0.0.0.0"]