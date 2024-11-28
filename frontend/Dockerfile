FROM node:18

# Étape de build
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm install
COPY . .
RUN npm run build

# Étape de serveur
FROM nginx:alpine
COPY --from=0 /app/dist /usr/share/nginx/html

# Ajouter la configuration personnalisée pour Nginx
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
