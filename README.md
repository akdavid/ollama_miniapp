# Ollama MiniApp

**Ollama MiniApp** est une application web permettant de dialoguer avec un modèle de langage, tel que Llama, via une interface utilisateur intuitive. Ce projet repose sur un backend FastAPI, un frontend Vue.js, et utilise Ollama pour exécuter les modèles de langage.

![Capture d'écran](ollama_miniapp.png) <!-- Ajoutez une capture d'écran ici -->

## Fonctionnalités

- **Interface utilisateur intuitive** : Une interface web pour envoyer des messages au modèle et afficher les réponses.
- **Backend extensible** : Basé sur FastAPI.
- **Déploiement Dockerisé** : Installation rapide avec Docker Compose.
- **Personnalisation des modèles** : Configurez `LLM_MODEL` pour choisir le modèle à utiliser.

## Architecture

- **Frontend** : Développé avec Vue.js, il offre une interface interactive et réactive.
- **Backend** : API REST construite avec FastAPI pour gérer la communication entre le frontend et Ollama.
- **Modèles de langage** : Exécutés via l'API Ollama.

---

## Prérequis

- **Docker** : Installez Docker et Docker Compose avant de continuer.

---

## Installation et déploiement

1. **Clonez ce dépôt** :

   ```bash
   git clone https://github.com/akdavid/ollama_miniapp.git
   cd ollama_miniapp
   ```

2. **Configurez votre environnement** :

   ```bash
   cp .env.example .env
   ```

3. **Lancez l'application** :

   ```bash
   docker-compose up --build
   ```

4. **Accédez à l'interface web** : [http://localhost:8080](http://localhost:8080)

---

## Utilisation

1. Ouvrez votre navigateur et rendez-vous à l'URL [http://localhost:8080](http://localhost:8080).
2. Tapez un message dans la barre de saisie et cliquez sur "Envoyer".
3. Observez la réponse générée par le modèle.

---

## Variables d'environnement

Les variables suivantes peuvent être configurées dans le fichier `.env` :

- **`LLM_MODEL`** : Définit le modèle de langage utilisé (exemple : `gemma:2b`).
- **`OLLAMA_API_URL`** : URL de l'API Ollama pour la génération de texte (par défaut : `http://ollama:11434/api/generate`).

---

## Ports utilisés

- **Frontend** : `8080`
- **Backend** : `8000`
- **Ollama** : `11434`

---

## Limitations connues

- **Prérequis matériels** : L'application est optimisée pour les CPU modernes avec support AVX2. Aucun GPU n'est requis pour les modèles actuels.
- **Modèles compatibles** : Actuellement, seuls les modèles disponibles via Ollama sont pris en charge.

---

## Contribution

Les contributions sont les bienvenues ! Si vous trouvez un bug ou souhaitez proposer une fonctionnalité, ouvrez une issue ou soumettez une pull request.

1. Clonez ce dépôt.
2. Créez une nouvelle branche pour vos modifications.
3. Testez votre code localement.
4. Envoyez une pull request avec une description claire.

---

## Licence

Ce projet est sous licence [MIT](./LICENSE).
