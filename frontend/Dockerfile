FROM node:18

# Installer les dépendances
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm install

# Copier le code source
COPY . .

# Construire l'application Vue.js
RUN npm run build

# Utiliser un serveur statique
FROM nginx:alpine
COPY --from=0 /app/dist /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
