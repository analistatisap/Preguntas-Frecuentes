<template>
  <div class="container my-5">
    <div class="row align-items-center justify-content-center">
      <!-- Columna de texto -->
      <div class="col-md-6 mb-4 mb-md-0">
        <div class="p-4 rounded-3 bg-white shadow-sm">
          <h2 class="mb-3">Bienvenido</h2>
          <p class="lead">
            Al Portal de Preguntas Frecuentes del Área de Tecnología Este espacio fue creado para resolver tus dudas sobre el uso de nuestras plataformas (SAP, CRM, VTEX, etc.). . Aquí encontrarás manuales, tutoriales, videos, tips y respuestas a las preguntas más frecuentes realizadas por tus compañeros.                     Si no encuentras lo que estás buscando, el equipo de Tecnología está disponible para brindarte soporte.
          </p>
        </div>
      </div>
      <!-- Columna de tarjeta de bienvenida -->
      <div class="col-md-6 text-center">
        <div class="welcome-card">
          <canvas ref="bgCanvas" class="bg-canvas"></canvas>
          <div class="welcome-content">
            <h1>¡Hola {{ nombre }}!</h1>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue';

const nombre = ref('Usuario');
const bgCanvas = ref(null);
let animationId = null;

// Obtener el nombre del usuario logueado
onMounted(() => {
  const userData = localStorage.getItem('user');
  if (userData) {
    try {
      const user = JSON.parse(userData);
      let nombreExtraido = '';
      if (user.fullName) {
        nombreExtraido = user.fullName.split(' ')[0];
      } else if (user.first_name) {
        nombreExtraido = user.first_name;
      } else if (user.username) {
        nombreExtraido = user.username;
      }
      if (nombreExtraido) nombre.value = nombreExtraido;
    } catch (e) {
      nombre.value = 'Usuario';
    }
  }

  // --- Animación canvas (igual que antes) ---
  const canvas = bgCanvas.value;
  const ctx = canvas.getContext('2d');
  let width = canvas.width = canvas.offsetWidth;
  let height = canvas.height = canvas.offsetHeight;
  let mouse = { x: width / 2, y: height / 2 };

  const gradients = [
    ['#7f7fd5', '#86a8e7', '#91eac9'],
    ['#f7971e', '#ffd200', '#21d4fd'],
    ['#a18cd1', '#fbc2eb', '#fad0c4'],
    ['#43cea2', '#185a9d', '#f8ffae'],
  ];
  const grad = ctx.createLinearGradient(0, 0, width, height);
  const palette = gradients[Math.floor(Math.random() * gradients.length)];
  grad.addColorStop(0, palette[0]);
  grad.addColorStop(0.5, palette[1]);
  grad.addColorStop(1, palette[2]);

  const POINTS = 60;
  const points = [];
  function randomBetween(a, b) { return a + Math.random() * (b - a); }
  function lerp(a, b, t) { return a + (b - a) * t; }
  for (let i = 0; i < POINTS; i++) {
    points.push({
      x: Math.random() * width,
      y: Math.random() * height,
      vx: randomBetween(-0.3, 0.3),
      vy: randomBetween(-0.3, 0.3),
      r: randomBetween(1.5, 3.5),
      baseR: 0,
      glow: Math.random() > 0.8,
      color: grad,
    });
  }

  function draw() {
    ctx.clearRect(0, 0, width, height);
    ctx.save();
    ctx.globalAlpha = 0.85;
    ctx.fillStyle = '#181c2f';
    ctx.fillRect(0, 0, width, height);
    ctx.restore();
    for (let i = 0; i < POINTS; i++) {
      for (let j = i + 1; j < POINTS; j++) {
        const p1 = points[i];
        const p2 = points[j];
        const dx = p1.x - p2.x;
        const dy = p1.y - p2.y;
        const dist = Math.sqrt(dx * dx + dy * dy);
        if (dist < 120) {
          ctx.save();
          ctx.globalAlpha = lerp(0.15, 0.5, 1 - dist / 120);
          ctx.strokeStyle = grad;
          ctx.shadowColor = palette[1];
          ctx.shadowBlur = 8;
          ctx.beginPath();
          ctx.moveTo(p1.x, p1.y);
          ctx.lineTo(p2.x, p2.y);
          ctx.stroke();
          ctx.restore();
        }
      }
    }
    for (let i = 0; i < POINTS; i++) {
      const p = points[i];
      const dx = p.x - mouse.x;
      const dy = p.y - mouse.y;
      const dist = Math.sqrt(dx * dx + dy * dy);
      let r = p.r;
      if (dist < 100) {
        r = lerp(p.r, 7, 1 - dist / 100);
      }
      ctx.save();
      ctx.beginPath();
      ctx.arc(p.x, p.y, r, 0, Math.PI * 2);
      ctx.closePath();
      ctx.globalAlpha = 0.85;
      ctx.fillStyle = grad;
      if (p.glow) {
        ctx.shadowColor = palette[2];
        ctx.shadowBlur = 18;
      }
      ctx.fill();
      ctx.restore();
      if (p.glow && Math.random() > 0.98) {
        ctx.save();
        ctx.globalAlpha = 0.25;
        ctx.beginPath();
        ctx.arc(p.x, p.y, r * 2.5, 0, Math.PI * 2);
        ctx.fillStyle = palette[2];
        ctx.shadowColor = palette[2];
        ctx.shadowBlur = 30;
        ctx.fill();
        ctx.restore();
      }
    }
  }

  function animate() {
    for (let i = 0; i < POINTS; i++) {
      const p = points[i];
      p.x += p.vx;
      p.y += p.vy;
      if (p.x < 0 || p.x > width) p.vx *= -1;
      if (p.y < 0 || p.y > height) p.vy *= -1;
    }
    draw();
    animationId = requestAnimationFrame(animate);
  }

  function handleResize() {
    width = canvas.width = canvas.offsetWidth;
    height = canvas.height = canvas.offsetHeight;
    for (let i = 0; i < POINTS; i++) {
      points[i].x = Math.random() * width;
      points[i].y = Math.random() * height;
    }
  }

  function handleMouseMove(e) {
    const rect = canvas.getBoundingClientRect();
    mouse.x = e.clientX - rect.left;
    mouse.y = e.clientY - rect.top;
  }

  window.addEventListener('resize', handleResize);
  canvas.addEventListener('mousemove', handleMouseMove);
  animate();

  onBeforeUnmount(() => {
    window.removeEventListener('resize', handleResize);
    canvas.removeEventListener('mousemove', handleMouseMove);
    cancelAnimationFrame(animationId);
  });
});
</script>

<style scoped>
.welcome-card {
  position: relative;
  width: 100%;
  min-height: 320px;
  height: 320px;
  border-radius: 2rem;
  overflow: hidden;
  box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(24, 28, 47, 0.85);
}
.bg-canvas {
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  width: 100%;
  height: 100%;
  display: block;
  z-index: 1;
}
.welcome-content {
  position: relative;
  z-index: 2;
  width: 100%;
  text-align: center;
  color: #fff;
  text-shadow: 0 2px 16px rgba(0,0,0,0.25);
}
.welcome-content h1 {
  font-size: 3rem !important;
  font-weight: 800;
  letter-spacing: 1px;
  margin: 0;
  padding: 0.5em 0;
  color: #fff !important;
  -webkit-text-fill-color: #fff !important;
  background: none !important;
  text-shadow: 0 2px 16px rgba(0,0,0,0.25);
}
</style>