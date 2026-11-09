# Grupo Noos — Sitio web

Sitio multipágina estático (HTML, CSS y JS, sin frameworks) para **Grupo Noos Seguridad Privada**.
Se puede subir tal cual a GitHub Pages, Netlify, Vercel o cualquier hosting.

## Páginas

| Archivo | Contenido |
|---|---|
| `index.html` | Inicio: hero, cifras, servicios, metodología, clientes |
| `nosotros.html` | Perfil, áreas de negocio, permiso SSC, socios, logros, clientes |
| `servicios.html` | Intramuros, escoltas, consultoría, protección civil, eventos |
| `capacitacion.html` | Krav Magá, galería de entrenamiento, instructores, programas |
| `tecnologia.html` | Videovigilancia, prisiones, patrullas inteligentes |
| `equipamiento.html` | Uniforme oficial, equipo táctico y balístico, unidades |
| `contacto.html` | Datos, mapa y formulario que se envía por WhatsApp |

## Logotipos de clientes

Están en `assets/img/clientes/`, en dos versiones: `nombre.webp` a color y `nombre-mono.webp` en plata.
Para agregar un cliente, guarda las dos versiones con el mismo nombre y súmalo a la lista `CLIENTS`
en `tools/build_pages.py`.

## Cómo editar

El header, el footer y los datos de contacto son iguales en todas las páginas y se generan con:

```bash
python3 tools/build_pages.py .
```

Los teléfonos, correos y direcciones están al inicio de `tools/build_pages.py`. El número de WhatsApp
del formulario también está en `assets/js/main.js` (`WHATSAPP`).

Para verlo localmente: `python3 -m http.server` y abre http://localhost:8000

## Pendientes por confirmar con el cliente

- **Correos**: siguen siendo `@croixrom.mx`. Cambiarlos cuando exista el dominio de Grupo Noos.
- **WhatsApp**: se usa el 55 2378 1229. Confirmar que sea el número comercial.
- **Redes sociales**: los enlaces apuntan a `@croixrom`. Actualizarlos a las cuentas de Grupo Noos.
- **Permiso SSC 0911-20**: está a nombre de CROIXROM, S.A. de C.V. Confirmar que el cambio de nombre
  ya esté reflejado ante la SSC antes de publicarlo como de Grupo Noos.
