<template>
  <div id="app">
    <nav>
      <router-link to="/">Chat</router-link>
      <router-link to="/image-description">Description d'image</router-link>
    </nav>
    <router-view />
    <!-- Affiche le composant correspondant à la route actuelle -->
  </div>
</template>

<script>
export default {
  name: 'App',
};
</script>

<style>
/* Styles pour le menu de navigation */
nav {
  background: #007bff;
  padding: 10px;
  display: flex;
  gap: 20px;
  justify-content: center;
}

nav a {
  color: white;
  text-decoration: none;
  font-weight: bold;
}

nav a.router-link-exact-active {
  text-decoration: underline;
}
</style>
