// fetchWithAuth.js
// Utilidad para peticiones autenticadas con refresco automático de token JWT

const API_BASE = 'http://172.16.29.5:8000'; // Cambia si tu backend usa otra URL

function parseJwt(token) {
  try {
    const base64Url = token.split('.')[1];
    const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
    const jsonPayload = decodeURIComponent(atob(base64).split('').map(function(c) {
      return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
    }).join(''));
    return JSON.parse(jsonPayload);
  } catch (e) {
    console.error('Error parsing JWT:', e);
    return null;
  }
}

function isTokenExpired(token) {
  const payload = parseJwt(token);
  if (!payload || !payload.exp) {
    console.log('Token inválido o sin exp');
    return true;
  }
  // exp está en segundos
  const isExpired = (Date.now() / 1000) > payload.exp - 30; // 30s de margen
  console.log('Token expirado:', isExpired, 'Exp:', new Date(payload.exp * 1000));
  return isExpired;
}

export async function refreshToken() {
  console.log('Intentando refrescar token...');
  const refresh = localStorage.getItem('refresh');
  if (!refresh) {
    console.log('No hay refresh token');
    return false;
  }
  
  try {
    const res = await fetch(`${API_BASE}/api/token/refresh/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ refresh })
    });
    
    console.log('Respuesta refresh token:', res.status);
    
    if (res.ok) {
      const data = await res.json();
      localStorage.setItem('access', data.access);
      console.log('Token refrescado exitosamente');
      return true;
    } else {
      console.log('Error al refrescar token:', res.status);
      localStorage.removeItem('access');
      localStorage.removeItem('refresh');
      return false;
    }
  } catch (error) {
    console.error('Error en refresh token:', error);
    return false;
  }
}

export async function fetchWithAuth(url, options = {}) {
  console.log('fetchWithAuth llamado para:', url);
  
  let access = localStorage.getItem('access');
  console.log('Token actual:', access ? 'Presente' : 'Ausente');
  
  if (!access || isTokenExpired(access)) {
    console.log('Token expirado o ausente, intentando refrescar...');
    const refreshed = await refreshToken();
    if (!refreshed) {
      console.log('No se pudo refrescar el token, redirigiendo al login');
      window.location.href = '/login';
      return Promise.reject('Sesión expirada.');
    }
    access = localStorage.getItem('access');
    console.log('Token refrescado:', access ? 'Presente' : 'Ausente');
  }
  
  options.headers = {
    ...(options.headers || {}),
    'Authorization': `Bearer ${access}`,
  };
  
  console.log('Realizando petición con headers:', options.headers);
  return fetch(url, options);
} 