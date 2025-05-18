<template>
  <div class="pagina-tips-manuales">
    <h1 class="titulo-pagina">Tips y Manuales SAP</h1>
    <p class="descripcion-pagina">
      En este espacio encontrarás material de apoyo, el cual podrás usar de soporte durante el
      desarrollo de tu gestión a través de los diferentes sistemas de Información que la compañía
      ha dispuesto para ti.
    </p>
    <div class="grid-manuales">
      <div v-for="(manual, index) in manuales" :key="index" class="cuadro-manual">
        <h3>{{ manual.titulo }}</h3>
        <div class="icono-manual">
          <a :href="manual.link" target="_blank" class="manual-icon-link">
            <img :src="manual.icono" :alt="manual.titulo">
          </a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TipsYManuales',
  data() {
    return {
      manuales: [
        // Añade la propiedad 'link' a cada objeto con la URL de SharePoint
        { titulo: 'Manual: Ofertas', icono: '/imgtipsymanuales/ofertas.png', link: 'https://grupodecor.sharepoint.com/calidad/manualesap/Documentos%20compartidos/Forms/AllItems.aspx?id=%2Fcalidad%2Fmanualesap%2FDocumentos%20compartidos%2FManuales%20Area%20Comercial%2FTI%2DMAN%2D175%20Manual%20Ofertas%20Movilidad%20V01%2Epdf&parent=%2Fcalidad%2Fmanualesap%2FDocumentos%20compartidos%2FManuales%20Area%20Comercial' },
        { titulo: 'Manual: Pedidos', icono: '/imgtipsymanuales/pedidos.png', link: 'https://grupodecor.sharepoint.com/calidad/manualesap/Documentos%20compartidos/Forms/AllItems.aspx?id=%2Fcalidad%2Fmanualesap%2FDocumentos%20compartidos%2FManuales%20Area%20Comercial%2FCreaci%C3%B3n%20Pedido%20de%20Venta%20V07%2Epdf&parent=%2Fcalidad%2Fmanualesap%2FDocumentos%20compartidos%2FManuales%20Area%20Comercial' },
        { titulo: 'Manual: Clientes', icono: '/imgtipsymanuales/clientes.png', link: 'https://grupodecor.sharepoint.com/calidad/manualesap/Documentos%20compartidos/Forms/AllItems.aspx?id=%2Fcalidad%2Fmanualesap%2FDocumentos%20compartidos%2FManuales%20Area%20Comercial%2FTI%2DMAN%2D171%20Manual%20Creaci%C3%B3n%20Socio%20de%20Negocio%20Movilidad%20V01%2Epdf&parent=%2Fcalidad%2Fmanualesap%2FDocumentos%20compartidos%2FManuales%20Area%20Comercial' },
        { titulo: 'Manual: Entregas', icono: '/imgtipsymanuales/entregas.png', link: 'https://grupodecor.sharepoint.com/calidad/manualesap/Documentos%20compartidos/Forms/AllItems.aspx?id=%2Fcalidad%2Fmanualesap%2FDocumentos%20compartidos%2FManuales%20Area%20Comercial%2FTI%2DMAN%2D172%20Manual%20Entrega%20de%20Salida%20Movilidad%20V01%2Epdf&parent=%2Fcalidad%2Fmanualesap%2FDocumentos%20compartidos%2FManuales%20Area%20Comercial' },
        { titulo: 'Manual: ATP', icono: '/imgtipsymanuales/atp.png', link: 'https://grupodecor.sharepoint.com/calidad/manualesap/Documentos%20compartidos/Forms/AllItems.aspx?id=%2Fcalidad%2Fmanualesap%2FDocumentos%20compartidos%2FManuales%20Area%20Comercial%2FTI%2DMAN%2D173%20Manual%20Verificaci%C3%B3n%20de%20Disponibilidad%20ATP%20V01%2Epdf&parent=%2Fcalidad%2Fmanualesap%2FDocumentos%20compartidos%2FManuales%20Area%20Comercial' },
        { titulo: 'Manual: Facturas', icono: '/imgtipsymanuales/facturas.png', link: 'https://grupodecor.sharepoint.com/calidad/manualesap/Documentos%20compartidos/Forms/AllItems.aspx?id=%2Fcalidad%2Fmanualesap%2FDocumentos%20compartidos%2FManuales%20Area%20Comercial%2FTI%2DMAN%2D174%20Manual%20Factura%20PQR%20y%20WF%20V01%2Epdf&parent=%2Fcalidad%2Fmanualesap%2FDocumentos%20compartidos%2FManuales%20Area%20Comercial' },
        { titulo: 'Manual: Instalacion Movilidad', icono: '/imgtipsymanuales/movilidad.png', link: 'https://grupodecor.sharepoint.com/calidad/manualesap/Documentos%20compartidos/Forms/AllItems.aspx?id=%2Fcalidad%2Fmanualesap%2FDocumentos%20compartidos%2FManuales%20Area%20Comercial%2FTI%2DMAN%2D168%20Manual%20Ingreso%20Movilidad%20V02%2Epdf&parent=%2Fcalidad%2Fmanualesap%2FDocumentos%20compartidos%2FManuales%20Area%20Comercial' },
        { titulo: 'Manual: Afluencia', icono: '/imgtipsymanuales/afluencia.png', link: 'https://c8450f47-07d2-4221-a56c-0a352fe167b0.filesusr.com/ugd/37b12c_0390e973084a43848a783aa345e362c8.pdf' },
        { titulo: 'Manual: Citas en Bodega', icono: '/imgtipsymanuales/citas-bodega.png', link: 'https://grupodecor.sharepoint.com/calidad/gestiondocumentos/tecnologiainformacion/Forms/AllItems.aspx?id=%2Fcalidad%2Fgestiondocumentos%2Ftecnologiainformacion%2FInstructivos%2FTI%2DINS%2D004%20Instructivo%20Portal%20Agendador%20Citas%20V01%2Epdf&parent=%2Fcalidad%2Fgestiondocumentos%2Ftecnologiainformacion%2FInstructivos' },
        { titulo: 'Manual: Caja General', icono: '/imgtipsymanuales/caja-general.png', link: 'https://grupodecor.sharepoint.com/calidad/manualesap/Documentos%20compartidos/Forms/AllItems.aspx?id=%2Fcalidad%2Fmanualesap%2FDocumentos%20compartidos%2FManuales%20%C3%81rea%20Cartera%20%2D%20FI%20%2DCO%2FTI%2DMAN%2D104%20Manejo%20de%20Recaudos%20para%20Usuarios%20SAP%20V09%2Epdf&parent=%2Fcalidad%2Fmanualesap%2FDocumentos%20compartidos%2FManuales%20%C3%81rea%20Cartera%20%2D%20FI%20%2DCO' },
        { titulo: 'Manual: Oferta y pedido exportacion', icono: '/imgtipsymanuales/oferta-exportacion.png', link: 'https://grupodecor.sharepoint.com/calidad/manualesap/Documentos%20compartidos/Manuales%20Area%20Comercial/TI-MAN-185%20Manual%20de%20Oferta%20y%20Pedido%20Exportaciones%20V01.pdf' },
        { titulo: 'Manual: Crear cliente - DecorMovil', icono: '/imgtipsymanuales/crear-cliente.png', link: 'https://grupodecor.sharepoint.com/calidad/manualesap/Documentos%20compartidos/Manuales%20Area%20Comercial/TI-MAN-171%20Manual%20Creaci%C3%B3n%20Socio%20de%20Negocio%20Movilidad%20V01.pdf' },
        { titulo: 'Manual: Portal Clientes CD', icono: '/imgtipsymanuales/portal-clientes-cd.png', link: 'https://grupodecor.sharepoint.com/calidad/gestiondocumentos/tecnologiainformacion/Forms/AllItems.aspx?id=%2Fcalidad%2Fgestiondocumentos%2Ftecnologiainformacion%2FInstructivos%2FTI%2DINS%2D003%20Instructivo%20Portal%20Clientes%20Decorceramica%20V02%2Epdf&parent=%2Fcalidad%2Fgestiondocumentos%2Ftecnologiainformacion%2FInstructivos' },
        { titulo: 'Manual: Portal Clientes NV', icono: '/imgtipsymanuales/portal-clientes-nv.png', link: 'https://grupodecor.sharepoint.com/calidad/gestiondocumentos/tecnologiainformacion/Forms/AllItems.aspx?id=%2Fcalidad%2Fgestiondocumentos%2Ftecnologiainformacion%2FInstructivos%2FTI%2DINS%2D002%20Instructivo%20Portal%20Clientes%20NovaCasa%20V02%2Epdf&parent=%2Fcalidad%2Fgestiondocumentos%2Ftecnologiainformacion%2FInstructivos' },
        { titulo: 'Manual: Pedido de muestra gratuita', icono: '/imgtipsymanuales/pedido-muestra.png', link: 'https://grupodecor-my.sharepoint.com/personal/jpina_grupodecor_com/_layouts/15/AccessDenied.aspx?Source=https%3A%2F%2Fgrupodecor%2Dmy%2Esharepoint%2Ecom%2F%3Ab%3A%2Fp%2Fjpina%2FERi47SsZbmdMjNli4yZ351oBU0u3iEdvHwnbUQXI6Vp4fQ%3Fe%3DGV3F6S&correlation=4b8a9ca1%2D100b%2D0000%2Dab65%2De090d905be49&Type=web&SiteId=123d0212%2Df13c%2D434f%2Db7d4%2D3d97f07cd836' },
        { titulo: 'Manual: Pedido de donacion', icono: '/imgtipsymanuales/pedido-donacion.jpg', link: 'https://grupodecor-my.sharepoint.com/personal/jpina_grupodecor_com/_layouts/15/AccessDenied.aspx?Source=https%3A%2F%2Fgrupodecor%2Dmy%2Esharepoint%2Ecom%2F%3Ab%3A%2Fp%2Fjpina%2FEf03yJ0NukVClZX%5FB67o7u4BfQFbTM0KAlfayXLEQsiPrA%3Fe%3DOPh7VI&correlation=4f8a9ca1%2D004a%2D0000%2Dab65%2De20d9f4c0924&Type=web&SiteId=123d0212%2Df13c%2D434f%2Db7d4%2D3d97f07cd836' },
      ],
    };
  },
};
</script>

<style scoped>
.pagina-tips-manuales {
  padding: 2rem;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  color: #333;
}

.titulo-pagina {
  text-align: center;
  color: #007bff;
  margin-bottom: 1rem;
}

.descripcion-pagina {
  text-align: center;
  color: #555;
  margin-bottom: 2rem;
}

.grid-manuales {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
}

.cuadro-manual {
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  padding: 1.5rem;
  text-align: center;
  transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out; /* Añadir transición para box-shadow */
  cursor: pointer; /* Añadir cursor pointer para indicar que es clickeable */
}

.cuadro-manual:hover {
  transform: scale(1.05);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15); /* Efecto de sombra al pasar el mouse */
}

.icono-manual {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100px;
  margin-bottom: 1rem;
}

/* Estilo para el enlace dentro del icono */
.icono-manual .manual-icon-link {
    display: flex; /* Permite centrar la imagen dentro del enlace */
    justify-content: center;
    align-items: center;
    width: 100%; /* Asegura que el enlace ocupe el área del icono */
    height: 100%; /* Asegura que el enlace ocupe el área del icono */
    text-decoration: none; /* Quitar el subrayado del enlace */
     transition: transform 0.3s ease-in-out; /* Transición para el efecto de escala del icono */
}

/* Efecto al pasar el mouse sobre el enlace/icono */
.icono-manual .manual-icon-link:hover img {
    transform: scale(1.1); /* Hacer la imagen del icono un poco más grande al pasar el mouse */
}


.icono-manual img {
  max-width: 80%;
  max-height: 80%;
  display: block; /* Asegura que la imagen se muestre correctamente */
  transition: transform 0.3s ease-in-out; /* Añadir transición también a la imagen */
}

.cuadro-manual h3 {
  color: #333;
  margin-top: 0;
  font-size: 1.2rem;
}
</style>