FROM nginx:alpine

# Copy nginx config (inside gateway folder)
COPY gateway/nginx.conf /etc/nginx/conf.d/default.conf

# Copy frontend build files (from frontend service)
COPY frontend/public/ /usr/share/nginx/html/

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
