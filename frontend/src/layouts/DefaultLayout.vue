<template>
    <div class="default-layout min-h-screen flex flex-col">
        <!-- Main Content Section -->
        <main class="flex-1 container mx-auto p-6">
            <slot />
        </main>
    </div>
</template>

<script>
export default {
    name: 'DefaultLayout',
};
</script>

<style scoped>
/* Scoped styles for custom overrides */
</style>
