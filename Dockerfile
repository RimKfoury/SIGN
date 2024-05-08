# Use an official Nginx image as a parent image
FROM nginx:latest

# Remove default nginx website
RUN rm -rf /usr/share/nginx/html/*

# Copy index.html, style.css, bg.mp4, and letter_images folder into the container at /usr/share/nginx/html
COPY index.html style.css bg.mp4 letter_images /usr/share/nginx/html/

# Expose port 80
EXPOSE 80

# Command to start nginx
CMD ["nginx", "-g", "daemon off;"]
