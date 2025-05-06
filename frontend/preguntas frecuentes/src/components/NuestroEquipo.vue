<template>
    <div class="nuestro-equipo">
      <h1 class="titulo">Nuestro Equipo</h1>
      <div class="equipo-container">
        <div class="miembro" v-for="miembro in equipo" :key="miembro.id">
          <img :src="miembro.foto" :alt="miembro.nombre" class="foto">
          <div class="info">
            <h2 class="nombre">{{ miembro.nombre }}</h2>
            <p class="rol">{{ miembro.rol }}</p>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'NuestroEquipo',
    data() {
      return {
        equipo: [
          {
            id: 1,
            nombre: 'Angee Reyes',
            rol: 'Gerente lider de tecnologia',
            foto: 'images/angee-reyes.jpg',
          },
          {
            id: 2,
            nombre: 'Oscar Marino Garcias',
            rol: 'Líder Funcional - MM y BO',
            foto: 'https://via.placeholder.com/150',
          },
          {
            id: 3,
            nombre: 'Karen Eliana Caicedo B.',
            rol: 'Líder de Desarrollo SAP y Aplicativos',
            foto: 'https://via.placeholder.com/150',
          },
        ],
      };
    },
  };
  </script>
  
  <style scoped>
  .nuestro-equipo {
    padding: 2rem;
    text-align: center;
    background-color: #f9f9f9;
  }
  
  .titulo {
    font-size: 2rem;
    margin-bottom: 1.5rem;
    color: #333;
  }
  
  .equipo-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 2rem;
  }
  
  .miembro {
    background: white;
    border: 1px solid #ddd;
    border-radius: 10px;
    padding: 1rem;
    width: 250px;
    text-align: center;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  
  .foto {
    width: 100px;
    height: 100px;
    border-radius: 50%;
    object-fit: cover;
    margin-bottom: 1rem;
  }
  
  .info {
    margin-top: auto; /* Empuja la información hacia la parte inferior */
  }
  
  .nombre {
    font-size: 1.2rem;
    font-weight: bold;
    margin-bottom: 0.5rem;
  }
  
  .rol {
    font-size: 1rem;
    color: #555;
    margin-bottom: 0.5rem;
  }
  </style>