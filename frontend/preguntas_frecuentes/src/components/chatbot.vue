<!-- filepath: src/components/Chatbot.vue -->
<template>
    <div id="webchat"></div>
  </template>
  
  <script>
  export default {
    name: "Chatbot",
    mounted() {
      // Inicializa el widget de Rasa Webchat
      window.WebChat.default.init({
        selector: "#webchat", // ID del contenedor
        initPayload: "/get_started", // Mensaje inicial opcional
        customData: { language: "es" }, // Datos personalizados
        socketUrl: "http://localhost:5005", // URL del servidor de Rasa
        socketPath: "/webhooks/rest/webhook", // Ruta del socket
        title: "Chatbot", // Título del chatbot
        subtitle: "Estoy aquí para ayudarte", // Subtítulo opcional
        params: {
          storage: "session", // Almacena la sesión del usuario
        },
      });
    },
  };
  </script>
  
  <style>
  /* Opcional: Estilo para el contenedor del chatbot */
  #webchat {
    position: fixed;
    bottom: 20px;
    right: 20px;
    z-index: 1000;
  }
  </style>