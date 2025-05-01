# Use the official Nginx image as a base
FROM nginx:latest

# Copy your custom html content into the default Nginx webroot
COPY ./html /usr/share/nginx/html

# Expose port 80 (optional, but good practice to document the port)
EXPOSE 80

# The default command from the base image will run Nginx
CMD ["nginx", "-g", "daemon off;"]


