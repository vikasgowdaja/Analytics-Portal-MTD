# 1️⃣ Build Stage
FROM node:18-alpine AS build

WORKDIR /app

# Install dependencies
COPY package*.json ./
RUN npm install

# Copy all client files & build
COPY . .
RUN npm run build


# 2️⃣ Production Stage - Serve using NGINX
FROM nginx:alpine

# Copy Vite's build output
COPY --from=build /app/dist /usr/share/nginx/html

# Expose port 80 for production hosting
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
