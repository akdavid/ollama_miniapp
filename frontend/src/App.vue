<template>
    <div id="app">
        <!-- Header -->
        <header class="header">
            <nav class="nav">
                <!-- Logo -->
                <router-link to="/" class="logo-container">
                    <img src="@/assets/logo.webp" alt="Ollama MiniApp Logo" class="logo-image" />
                </router-link>

                <!-- Navigation Links -->
                <div class="nav-links">
                    <router-link to="/" class="nav-link">Home</router-link>
                    <router-link to="/chat" class="nav-link">Chat</router-link>
                    <router-link to="/image-description" class="nav-link"
                        >Image Description</router-link
                    >
                </div>
            </nav>
        </header>

        <!-- Main Content -->
        <main class="main-content">
            <router-view />
        </main>

        <!-- Footer -->
        <footer class="footer">© 2024 Ollama MiniApp. All rights reserved.</footer>
    </div>
</template>

<script>
export default {
    name: 'App',
};
</script>

<style>
/* Header */
.header {
    background-color: #007bff;
    color: white;
    padding: 1rem 0;
}

.nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 1rem;
}

/* Logo */
.logo-container {
    display: flex;
    align-items: center;
    gap: 1rem;
    text-decoration: none; /* Remove underline from router-link */
    color: inherit; /* Inherit color for the text */
}

.logo-image {
    height: 60px; /* Increased height for better visibility */
    width: auto;
    border-radius: 8px; /* Optional: Add rounded corners to the logo */
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* Optional: Add shadow for contrast */
    background-color: white; /* Optional: Add background for better visibility */
    padding: 0.5rem; /* Optional: Add padding inside the background */
}

.logo-text {
    font-size: 2rem; /* Increase font size for the text */
    font-weight: bold;
    color: #ffffff; /* Ensure text color contrasts well with the header */
}

/* Navigation Links */
.nav-links {
    display: flex;
    gap: 1.5rem; /* Increase spacing between links */
}

.nav-link {
    color: white;
    text-decoration: none;
    font-weight: bold;
    font-size: 1.1rem; /* Slightly larger font for better readability */
}

.nav-link:hover {
    text-decoration: underline;
}

/* Main Content */
.main-content {
    padding: 2rem;
    max-width: 1200px;
    margin: 0 auto;
}

/* Footer */
.footer {
    background-color: #343a40;
    color: #adb5bd;
    text-align: center;
    padding: 1rem;
}
</style>
