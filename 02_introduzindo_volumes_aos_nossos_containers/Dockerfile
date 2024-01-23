# FROM imagem:tag-servidor #
FROM php:8-apache

# WORKDIR /the/workdir/path #
WORKDIR /var/www/html/

# COPY source dest #
COPY . .

# EXPOSE port #
EXPOSE 80

# RUN comando_de_permissao usuario:grupo  em_todos_os_arquivos #
RUN chown -R www-data:www-data /var/www