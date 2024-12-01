# Étape de développement
FROM node:18 AS development

WORKDIR /app
COPY package.json package-lock.json ./
RUN npm install
COPY . .

EXPOSE 5173

CMD ["npm", "run", "dev", "--", "--host"]

# Étape de build pour la production
FROM node:18 AS build

WORKDIR /app
COPY package.json package-lock.json ./
RUN npm install
COPY . .

RUN npm run build

# Étape de production : Servir les fichiers avec Nginx
FROM nginx:stable-alpine AS production

COPY --from=build /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
