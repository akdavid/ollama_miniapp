<template>
    <DefaultLayout>
        <Chat />
    </DefaultLayout>
</template>

<script>
import Chat from '../components/chat/Chat.vue';
import DefaultLayout from '../layouts/DefaultLayout.vue';

export default {
    components: { Chat, DefaultLayout },
};
</script>
