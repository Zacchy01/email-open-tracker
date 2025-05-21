# Use an official PHP image
FROM php:8.2-apache

# Install necessary PHP extensions
RUN docker-php-ext-install pdo pdo_mysql

# Enable Apache rewrite module
RUN a2enmod rewrite

# Copy your YOURLS files into the container
COPY . /var/www/html/

# Set working directory
WORKDIR /var/www/html/

# Expose port 8080 (Render's default)
EXPOSE 8080

# Start Apache
CMD ["apache2-foreground"]
