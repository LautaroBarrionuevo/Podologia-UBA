# Podología UBA — Sitio desplegado

Sitio en vivo: https://podologia-uba.vercel.app/

## Pasos para buildar y ver en local

Requisitos:
- Tener instalado `node` y `npm` (opcional para deploy con Vercel CLI)
- Tener instalado `sass` CLI (o usar `npm` scripts)

Comandos comunes:

- Compilar SCSS a CSS (usando Dart Sass):

  ```bash
  sass --no-source-map scss:assets/css
  ```

- Compilar y comprimir:

  ```bash
  sass --no-source-map --style=compressed scss:assets/css
  ```

- Servir localmente (simple, usando `http-server` o Live Server):

  ```bash
  npx http-server . -c-1 -p 8080
  # o usar la extensión Live Server en VS Code
  ```

- Deploy a Vercel (si ya configuraste y tienes `vercel`):

  ```bash
  npx vercel --prod
  ```

## Archivos importantes

- `index.html` — página principal
- `pages/` — páginas secundarias (`contacto.html`, `empleo.html`, `login-medico.html`, `login-paciente.html`)
- `scss/` — código fuente SCSS
- `assets/css/style.css` — CSS compilado usado en producción

## Notas rápidas

- El sitio está desplegado en Vercel con HTTPS.
- Para volver a desplegar: compilar SCSS y luego ejecutar `npx vercel --prod`.
