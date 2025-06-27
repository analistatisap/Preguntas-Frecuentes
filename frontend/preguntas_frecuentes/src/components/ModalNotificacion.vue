<template>
  <transition name="modal-fade">
    <div v-if="visible" class="modal-overlay" @click.self="$emit('aceptar')">
      <div class="modal-card">
        <div class="modal-header">
          <slot name="icon">
            <svg width="36" height="36" viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="12" fill="#e3e8f0"/><path d="M12 7v5" stroke="#185a9d" stroke-width="2" stroke-linecap="round"/><circle cx="12" cy="16" r="1.2" fill="#185a9d"/></svg>
          </slot>
          <h2>{{ titulo }}</h2>
        </div>
        <div class="modal-body">
          <p>{{ mensaje }}</p>
        </div>
        <div class="modal-footer">
          <button class="btn-aceptar" @click="$emit('aceptar')">Aceptar</button>
        </div>
      </div>
    </div>
  </transition>
</template>

<script setup>
defineProps({
  titulo: { type: String, required: true },
  mensaje: { type: String, required: true },
  visible: { type: Boolean, required: true }
});
</script>

<style scoped>
.modal-fade-enter-active, .modal-fade-leave-active {
  transition: opacity 0.25s;
}
.modal-fade-enter-from, .modal-fade-leave-to {
  opacity: 0;
}
.modal-overlay {
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(24, 28, 47, 0.35);
  backdrop-filter: blur(3px);
  z-index: 1000;
  display: flex;
  align-items: center;
  justify-content: center;
}
.modal-card {
  background: #fff;
  border-radius: 1.2rem;
  box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.18);
  min-width: 340px;
  max-width: 90vw;
  padding: 2.2rem 2rem 1.5rem 2rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  animation: popIn 0.3s cubic-bezier(.4,1.6,.6,1) 1;
}
@keyframes popIn {
  0% { transform: scale(0.85); opacity: 0; }
  100% { transform: scale(1); opacity: 1; }
}
.modal-header {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 1rem;
}
.modal-header h2 {
  font-size: 1.25rem;
  font-weight: 700;
  color: #185a9d;
  margin: 0.5rem 0 0 0;
  text-align: center;
}
.modal-body {
  color: #222;
  font-size: 1.08rem;
  text-align: center;
  margin-bottom: 1.5rem;
}
.btn-aceptar {
  background: linear-gradient(90deg, #7f7fd5, #86a8e7, #91eac9);
  color: #fff;
  font-weight: 600;
  border: none;
  border-radius: 2rem;
  padding: 0.6rem 2.2rem;
  font-size: 1.08rem;
  box-shadow: 0 2px 8px #7f7fd522;
  cursor: pointer;
  transition: background 0.2s, box-shadow 0.2s;
}
.btn-aceptar:hover {
  background: linear-gradient(90deg, #185a9d, #43cea2);
  box-shadow: 0 4px 16px #185a9d22;
}
</style> 