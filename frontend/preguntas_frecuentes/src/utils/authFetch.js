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
    return null;
  }
}

function isTokenExpired(token) {
  const payload = parseJwt(token);
  if (!payload || !payload.exp) return true;
  // exp está en segundos
  return (Date.now() / 1000) > payload.exp - 30; // 30s de margen
}

export async function refreshToken() {
  const refresh = localStorage.getItem('refresh');
  if (!refresh) return false;
  const res = await fetch(`${API_BASE}/api/token/refresh/`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ refresh })
  });
  if (res.ok) {
    const data = await res.json();
    localStorage.setItem('access', data.access);
    return true;
  } else {
    localStorage.removeItem('access');
    localStorage.removeItem('refresh');
    return false;
  }
}

export async function fetchWithAuth(url, options = {}) {
  let access = localStorage.getItem('access');
  if (!access || isTokenExpired(access)) {
    const refreshed = await refreshToken();
    if (!refreshed) {
      window.location.href = '/login';
      return Promise.reject('Sesión expirada.');
    }
    access = localStorage.getItem('access');
  }
  options.headers = {
    ...(options.headers || {}),
    'Authorization': `Bearer ${access}`,
  };
  return fetch(url, options);
} 