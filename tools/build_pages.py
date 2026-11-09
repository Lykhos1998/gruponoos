#!/usr/bin/env python3
"""Genera las páginas HTML estáticas de Grupo Noos con header/footer compartidos."""
import sys, pathlib

OUT = pathlib.Path(sys.argv[1])

PHONE_DISPLAY = "55 7100 4711"
PHONE_TEL = "+525571004711"
WA = "525523781229"
WA_DISPLAY = "55 2378 1229"
EMAIL = "ceo@croixrom.mx"
EMAIL2 = "a.castaneda@croixrom.mx"
IG = "https://www.instagram.com/croixrom/"
FB = "https://www.facebook.com/croixrom"
ADDR1 = "Blvd. Adolfo Ruiz Cortines 3720, Torre II, Piso 8, Col. Jardines del Pedregal, Alcaldía Álvaro Obregón, C.P. 01900, CDMX"
ADDR2 = "Saturnino Herrán 17, Col. San José Insurgentes, Alcaldía Benito Juárez, C.P. 03900, CDMX"

I = {
 "arrow": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="square"><path d="M4 12h15M13 6l6 6-6 6"/></svg>',
 "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M12 2 4 5v6c0 5 3.4 9.4 8 11 4.6-1.6 8-6 8-11V5z"/><path d="m8.5 12 2.5 2.5 4.5-5"/></svg>',
 "building": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 21V4h10v17M14 9h6v12M2 21h20M7 8h1M10 8h1M7 12h1M10 12h1M7 16h1M10 16h1M17 13h1M17 17h1"/></svg>',
 "car": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M3 13l2-6h14l2 6v5H3z"/><path d="M3 13h18"/><circle cx="7" cy="16" r="1.4"/><circle cx="17" cy="16" r="1.4"/><path d="M5 18v2M19 18v2"/></svg>',
 "target": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.2" fill="currentColor"/><path d="M12 1v4M12 19v4M1 12h4M19 12h4"/></svg>',
 "chart": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M3 3v18h18"/><path d="m7 15 4-4 3 3 6-7"/><path d="M15 7h5v5"/></svg>',
 "camera": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M3 6h13l5 3-5 3H3z"/><path d="M8 12v4H4M8 16v4"/><circle cx="11" cy="9" r="1.2"/></svg>',
 "life": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="4"/><path d="m5.6 5.6 3.6 3.6M14.8 14.8l3.6 3.6M18.4 5.6l-3.6 3.6M9.2 14.8l-3.6 3.6"/></svg>',
 "event": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="3" y="5" width="18" height="16"/><path d="M3 10h18M8 3v4M16 3v4"/><path d="m9 15 2 2 4-4"/></svg>',
 "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M5 3h4l2 5-2.5 1.5a11 11 0 0 0 6 6L16 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 5a2 2 0 0 1 2-2"/></svg>',
 "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="3" y="5" width="18" height="14"/><path d="m3 6 9 7 9-7"/></svg>',
 "pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M12 22s7-6.2 7-12a7 7 0 1 0-14 0c0 5.8 7 12 7 12z"/><circle cx="12" cy="10" r="2.5"/></svg>',
 "wa": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M17.5 14.4c-.3-.1-1.7-.8-2-.9-.3-.1-.5-.1-.7.1-.2.3-.8.9-.9 1.1-.2.2-.3.2-.6.1-.3-.1-1.2-.5-2.3-1.4-.9-.8-1.4-1.7-1.6-2-.2-.3 0-.5.1-.6l.4-.5c.2-.2.2-.3.3-.5.1-.2 0-.4 0-.5l-.9-2.2c-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.4s1 2.8 1.2 3c.1.2 2 3.1 4.9 4.3.7.3 1.2.5 1.7.6.7.2 1.3.2 1.8.1.6-.1 1.7-.7 1.9-1.4.2-.7.2-1.2.2-1.4-.1-.1-.3-.2-.6-.3zM12 21.8c-1.8 0-3.5-.5-5-1.4l-.4-.2-3.7 1 1-3.6-.2-.4A9.8 9.8 0 1 1 12 21.8zm8.4-18.2A11.8 11.8 0 0 0 1.9 17.9L.2 24l6.3-1.7A11.8 11.8 0 0 0 24 12c0-3.2-1.2-6.1-3.6-8.4z"/></svg>',
 "ig": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor"/></svg>',
 "fb": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M14 8h3V4h-3c-2.8 0-4.5 1.8-4.5 4.6V11H7v4h2.5v9h4v-9h3l.5-4h-3.5V8.8c0-.5.3-.8.5-.8z"/></svg>',
}

NAV = [
 ("index.html", "Inicio"),
 ("nosotros.html", "Nosotros"),
 ("servicios.html", "Servicios"),
 ("capacitacion.html", "Capacitación"),
 ("tecnologia.html", "Tecnología"),
 ("equipamiento.html", "Equipamiento"),
]

def head(title, desc, page):
    return f'''<!doctype html>
<html lang="es-MX" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#05080b">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="assets/img/logo-grupo-noos.png">
<meta property="og:locale" content="es_MX">
<link rel="icon" type="image/png" sizes="32x32" href="assets/img/icon-32.png">
<link rel="apple-touch-icon" href="assets/img/icon-192.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Oswald:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/styles.css">
</head>
<body>
<a class="sr-only" href="#main">Saltar al contenido</a>
'''

def header(page):
    links = "\n".join(
        f'      <a href="{h}"{" aria-current=\"page\"" if h == page else ""}>{t}</a>' for h, t in NAV)
    solid = "" if page == "index.html" else ""
    return f'''<header class="site-header{solid}">
  <div class="wrap">
    <a class="brand" href="index.html" aria-label="Grupo Noos, inicio">
      <img src="assets/img/logo-grupo-noos.webp" alt="" width="44" height="60">
      <span class="brand-text"><strong>Grupo Noos</strong><span>Seguridad Privada</span></span>
    </a>
    <button class="nav-toggle" aria-label="Abrir menú" aria-expanded="false" aria-controls="nav"><span></span></button>
    <nav class="nav" id="nav" aria-label="Principal">
{links}
      <a class="btn btn-primary" href="contacto.html"{" aria-current=\"page\"" if page == "contacto.html" else ""}>Cotizar</a>
    </nav>
  </div>
</header>
<main id="main">
'''

FOOTER = f'''</main>

<section class="cta-band">
  <div class="wrap">
    <div class="reveal">
      <span class="eyebrow">Hablemos</span>
      <h2>Su seguridad es nuestra <span class="hl">prioridad</span>.</h2>
      <p>Cuéntenos qué necesita proteger y le enviamos una propuesta a la medida.</p>
    </div>
    <div class="btn-row reveal" data-delay="1">
      <a class="btn btn-primary" href="contacto.html">Solicitar cotización {I["arrow"]}</a>
      <a class="btn btn-ghost" href="https://wa.me/{WA}" target="_blank" rel="noopener">{I["wa"]} WhatsApp</a>
    </div>
  </div>
</section>

<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div class="footer-brand">
        <img src="assets/img/logo-grupo-noos.webp" alt="Grupo Noos Seguridad Privada" width="88" height="120" loading="lazy">
        <p>Seguridad privada, protección personal, capacitación y logística con altos estándares de calidad y atención personalizada.</p>
        <div class="socials">
          <a href="{IG}" target="_blank" rel="noopener" aria-label="Instagram">{I["ig"]}</a>
          <a href="{FB}" target="_blank" rel="noopener" aria-label="Facebook">{I["fb"]}</a>
          <a href="https://wa.me/{WA}" target="_blank" rel="noopener" aria-label="WhatsApp">{I["wa"]}</a>
        </div>
      </div>
      <div>
        <h4>Empresa</h4>
        <ul>
          <li><a href="nosotros.html">Nosotros</a></li>
          <li><a href="nosotros.html#permiso">Permiso oficial</a></li>
          <li><a href="nosotros.html#clientes">Clientes</a></li>
          <li><a href="contacto.html">Contacto</a></li>
        </ul>
      </div>
      <div>
        <h4>Servicios</h4>
        <ul>
          <li><a href="servicios.html#intramuros">Seguridad intramuros</a></li>
          <li><a href="servicios.html#escoltas">Escoltas</a></li>
          <li><a href="servicios.html#consultoria">Consultoría</a></li>
          <li><a href="capacitacion.html">Capacitación</a></li>
          <li><a href="tecnologia.html">Tecnología</a></li>
          <li><a href="servicios.html#eventos">Logística de eventos</a></li>
        </ul>
      </div>
      <div>
        <h4>Contacto</h4>
        <ul>
          <li><a href="tel:{PHONE_TEL}">Oficina: {PHONE_DISPLAY}</a></li>
          <li><a href="https://wa.me/{WA}" target="_blank" rel="noopener">WhatsApp: {WA_DISPLAY}</a></li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li>Jardines del Pedregal, Álvaro Obregón, CDMX</li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© <span id="year">2026</span> Grupo Noos Seguridad Privada. Todos los derechos reservados.</span>
      <span>Permiso SSC CDMX No. 0911-20 · Exp. 5248-20</span>
    </div>
  </div>
</footer>

<a class="wa-float" href="https://wa.me/{WA}" target="_blank" rel="noopener" aria-label="Escríbenos por WhatsApp">{I["wa"]}</a>
<script src="assets/js/main.js" defer></script>
</body>
</html>
'''

def page_hero(crumb, eyebrow, title, lead, bg):
    return f'''<section class="page-hero">
  <div class="hero-bg"><img src="assets/img/{bg}" alt="" fetchpriority="high"></div>
  <div class="grid-overlay"></div>
  <div class="wrap">
    <div class="crumbs"><a href="index.html">Inicio</a><span>/</span>{crumb}</div>
    <span class="eyebrow">{eyebrow}</span>
    <h1>{title}</h1>
    <p class="lead">{lead}</p>
  </div>
</section>
'''

def card(n, icon, title, text, href):
    return f'''      <a class="card reveal" href="{href}">
        <span class="card-num">{n:02d}</span>
        <span class="card-icon">{I[icon]}</span>
        <h3>{title}</h3>
        <p>{text}</p>
        <span class="link-arrow">Ver más {I["arrow"]}</span>
      </a>'''

CLIENTS = [
 ("inapesca", "INAPESCA", "Instituto Nacional de Pesca y Acuacultura", "Gobierno federal"),
 ("sedatu", "SEDATU", "Secretaría de Desarrollo Agrario, Territorial y Urbano", "Gobierno federal"),
 ("senasica", "SENASICA", "Servicio Nacional de Sanidad, Inocuidad y Calidad Agroalimentaria", "Gobierno federal"),
 ("aem", "AEM", "Agencia Espacial Mexicana", "Gobierno federal"),
 ("metro", "Metro CDMX", "Sistema de Transporte Colectivo", "Gobierno CDMX"),
 ("wandel", "Farmacéutica Wandel", "Industria farmacéutica", "Sector privado"),
 ("biomep", "BIOMEP", "Sector salud", "Sector privado"),
 ("stratominds", "Stratominds", "Potencializa tu mente", "Sector privado"),
]

def logo_tile(slug, name, hidden=False):
    alt = "" if hidden else name
    return (f'<div class="logo-tile"{" aria-hidden=\"true\"" if hidden else ""}>'
            f'<img class="mono" src="assets/img/clientes/{slug}-mono.webp" alt="{alt}" loading="lazy">'
            f'<img class="color" src="assets/img/clientes/{slug}.webp" alt="" loading="lazy"></div>')

def logo_marquee(rev=False):
    items = CLIENTS[::-1] if rev else CLIENTS
    row = "".join(logo_tile(c[0], c[1], hidden=rev) for c in items)
    dup = "".join(logo_tile(c[0], c[1], hidden=True) for c in items)
    return f'    <div class="logo-marquee{" rev" if rev else ""}"><div class="logo-track">{row}{dup}</div></div>'

def client_cards():
    return "\n".join(
        f'''      <figure class="client-card reveal" data-delay="{i % 4}">
        {logo_tile(slug, name)}
        <figcaption><span class="sector">{sector}</span><strong>{name}</strong><small>{desc}</small></figcaption>
      </figure>''' for i, (slug, name, desc, sector) in enumerate(CLIENTS))

PROCESS = [
 ("Diseño", "Diagnóstico de riesgos y diseño de la estrategia a la medida."),
 ("Planeación", "Definimos personal, turnos, equipo, tecnología y protocolos."),
 ("Implementación", "Despliegue de elementos y sistemas con supervisión constante."),
 ("Seguimiento", "Reportes, supervisión en sitio y comunicación directa."),
 ("Mejora continua", "Evaluamos y actualizamos la estrategia de forma permanente."),
]

def process():
    s = "\n".join(f'''      <div class="step reveal" data-delay="{min(i,3)}"><div class="step-dot"><span>{i+1:02d}</span></div><h3>{t}</h3><p>{d}</p></div>''' for i, (t, d) in enumerate(PROCESS))
    return f'    <div class="process">\n{s}\n    </div>'

# ---------------------------------------------------------------- INICIO
index = head("Grupo Noos | Seguridad Privada en CDMX",
  "Grupo Noos: seguridad privada, escoltas, seguridad intramuros, capacitación táctica y consultoría en seguridad. Permiso SSC CDMX 0911-20.", "index.html") + header("index.html") + f'''
<section class="hero">
  <div class="hero-bg"><img src="assets/img/equipo-noos.webp" alt="" fetchpriority="high"></div>
  <div class="grid-overlay"></div>
  <div class="wrap hero-inner">
    <div>
      <span class="eyebrow reveal">Seguridad privada · CDMX</span>
      <h1 class="reveal" data-delay="1">Su seguridad es nuestra <span class="hl">prioridad</span>.</h1>
      <p class="lead reveal" data-delay="2">Confíela en las mejores manos. Creamos soluciones integrales de seguridad con elementos capacitados, tecnología y estrategia, para que su organización cumpla sus objetivos sin preocupaciones.</p>
      <div class="btn-row reveal" data-delay="3">
        <a class="btn btn-primary" href="contacto.html">Solicitar cotización {I["arrow"]}</a>
        <a class="btn btn-ghost" href="servicios.html">Ver servicios</a>
      </div>
      <div class="hero-meta reveal" data-delay="3">
        <span>Permiso SSC CDMX</span><span>Elementos certificados</span><span>Atención personalizada</span>
      </div>
    </div>
    <div class="hero-badge">
      <span class="scan-ring"></span><span class="scan-ring r2"></span>
      <img src="assets/img/logo-grupo-noos.webp" alt="Escudo Grupo Noos Seguridad Privada" width="501" height="687">
    </div>
  </div>
</section>

<section class="stats" aria-label="Grupo Noos en cifras">
  <div class="stat reveal"><strong><em>SSC</em></strong><span>Permiso oficial vigente para prestar servicios de seguridad privada en CDMX</span></div>
  <div class="stat reveal" data-delay="1"><strong><span data-count="100">100</span><em>%</em></strong><span>De satisfacción de nuestros clientes</span></div>
  <div class="stat reveal" data-delay="2"><strong><span data-count="26">26</span><em>+</em></strong><span>Años de experiencia de nuestro instructor en Krav Magá israelí</span></div>
  <div class="stat reveal" data-delay="3"><strong><span data-count="8">8</span><em>+</em></strong><span>Instituciones públicas y empresas que confían en nosotros</span></div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <div class="reveal">
        <span class="eyebrow">Servicios</span>
        <h2>Soluciones integrales de seguridad</h2>
      </div>
      <p class="reveal" data-delay="1">Un equipo interdisciplinario, con experiencia en el sector público y privado, que piensa cada solución desde una óptica estratégica: del análisis a la implementación, la evaluación y la actualización.</p>
    </div>
    <div class="cards">
{card(1,"building","Seguridad intramuros","Resguardo de edificios corporativos, plazas e instalaciones de gobierno, con y sin arma.","servicios.html#intramuros")}
{card(2,"car","Escoltas y protección personal","Escoltas profesionales con licencia de portación incluida y vehículo escolta.","servicios.html#escoltas")}
{card(3,"chart","Consultoría y estudios de seguridad","Estrategias con enfoque organizacional: análisis de riesgos, protocolos y mejora continua.","servicios.html#consultoria")}
{card(4,"target","Centro de capacitación","Krav Magá israelí, tiro y formación integral para elementos de seguridad y escoltas.","capacitacion.html")}
{card(5,"camera","Tecnología y monitoreo","Videovigilancia inteligente, LPR, centros de control C4i/C5i y ciberseguridad.","tecnologia.html")}
{card(6,"event","Logística de grandes eventos","Diseño, planeación y ejecución logística de eventos y producciones a gran escala.","servicios.html#eventos")}
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="wrap split">
    <div class="split-media frame reveal">
      <img src="assets/img/escolta-vehiculo.webp" alt="Escolta de Grupo Noos junto a vehículo escolta" loading="lazy" width="1280" height="853">
      <span class="media-tag">Protección ejecutiva</span>
    </div>
    <div class="reveal" data-delay="1">
      <span class="eyebrow">¿Por qué Grupo Noos?</span>
      <h2>Juventud y experiencia, con <span class="hl">disciplina</span> táctica</h2>
      <p class="lead">Somos una empresa de vanguardia dedicada a crear soluciones integrales que ayuden a su organización a cumplir sus objetivos, con altos estándares de calidad y atención personalizada.</p>
      <ul class="checklist">
        <li>Permiso oficial de la Secretaría de Seguridad Ciudadana de la CDMX.</li>
        <li>Elementos capacitados en defensa personal, combate cuerpo a cuerpo y tiro.</li>
        <li>Equipamiento táctico profesional y unidades propias.</li>
        <li>Supervisión constante y comunicación directa con su equipo.</li>
      </ul>
      <p style="margin-top:28px"><a class="link-arrow" href="nosotros.html">Conozca más de nosotros {I["arrow"]}</a></p>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head center">
      <span class="eyebrow reveal">Metodología</span>
      <h2 class="reveal">Estrategias con enfoque organizacional</h2>
    </div>
{process()}
  </div>
</section>

<section class="section section-alt" aria-label="Clientes">
  <div class="wrap">
    <div class="section-head">
      <div class="reveal">
        <span class="eyebrow">Experiencia</span>
        <h2>Confían en nosotros</h2>
      </div>
      <p class="reveal" data-delay="1">Hemos dado servicio a dependencias de gobierno federal y local, y a empresas del sector privado.</p>
    </div>
  </div>
  <div class="logo-wall reveal">
{logo_marquee()}
{logo_marquee(rev=True)}
  </div>
  <div class="wrap">
    <div class="sector-strip reveal">
      <span><strong>4</strong> dependencias federales</span>
      <span><strong>1</strong> organismo de la CDMX</span>
      <span><strong>3</strong> empresas privadas</span>
      <a class="link-arrow" href="nosotros.html#clientes">Ver todos {I["arrow"]}</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap quote reveal">
    <blockquote>El verdadero soldado no lucha porque odia lo que tiene delante, sino porque ama lo que tiene detrás.</blockquote>
    <cite>G. K. Chesterton</cite>
  </div>
</section>
''' + FOOTER

# ---------------------------------------------------------------- NOSOTROS
nosotros = head("Nosotros | Grupo Noos Seguridad Privada",
  "Conozca a Grupo Noos: empresa de seguridad privada con permiso oficial SSC CDMX, equipo interdisciplinario y socios estratégicos en capacitación.", "nosotros.html") + header("nosotros.html") + page_hero(
  "Nosotros", "Quiénes somos", 'Confíela en las <span class="hl">mejores manos</span>',
  "Somos una empresa de vanguardia que integra juventud y experiencia para crear soluciones integrales de seguridad privada y logística.",
  "equipo-noos.webp") + f'''
<section class="section">
  <div class="wrap split">
    <div class="reveal">
      <span class="eyebrow">Perfil</span>
      <h2>Creamos soluciones <span class="hl">integrales</span></h2>
      <p class="lead">Somos una empresa de vanguardia dedicada a CREAR soluciones integrales para que su organización cumpla sus objetivos, con altos estándares de calidad y atención personalizada.</p>
      <p>Contamos con un equipo interdisciplinario, altamente capacitado en todos los temas de la seguridad y con amplia experiencia en el sector público y privado. Eso nos permite pensar cada solución desde una óptica estratégica y especializada, que abarca el análisis, la implementación, la evaluación y la actualización de la estrategia que su organización necesita.</p>
    </div>
    <div class="split-media reveal" data-delay="1">
      <img class="frame" src="assets/img/guardias-estacionamiento.webp" alt="Elementos de Grupo Noos con uniforme oficial en estacionamiento" loading="lazy" width="1280" height="853">
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="wrap">
    <div class="section-head">
      <div class="reveal"><span class="eyebrow">Áreas de negocio</span><h2>Dos divisiones, un mismo estándar</h2></div>
      <p class="reveal" data-delay="1">Estrategias de seguridad con enfoque organizacional: diseño, planeación, implementación, seguimiento y mejora continua.</p>
    </div>
    <div class="cards" style="grid-template-columns:repeat(auto-fit,minmax(min(100%,340px),1fr))">
{card(1,"shield","Elementos de seguridad intramuros y escoltas","Guardias para edificios e instalaciones, y protección personal con escoltas profesionales.","servicios.html")}
{card(2,"life","Centro de capacitación y consultoría","Capacitación táctica, consultoría en seguridad y protección civil para su organización.","capacitacion.html")}
    </div>
  </div>
</section>

<section class="section" id="permiso">
  <div class="wrap">
    <div class="credential reveal">
      <img src="assets/img/logo-grupo-noos.webp" alt="" loading="lazy">
      <div>
        <span class="eyebrow">Permiso oficial</span>
        <h2 style="font-size:clamp(1.6rem,3.4vw,2.4rem)">Autorizados por la Secretaría de Seguridad Ciudadana de la CDMX</h2>
        <p>Permiso para prestar servicios de seguridad privada, otorgado por la Dirección General de Seguridad Privada y Colaboración Interinstitucional, en las modalidades de <strong>I. Seguridad y protección personal</strong> y <strong>II. Vigilancia y protección de bienes</strong>.</p>
        <dl>
          <div><dt>Permiso</dt><dd>0911-20</dd></div>
          <div><dt>Expediente</dt><dd>5248-20</dd></div>
          <div><dt>Estatus</dt><dd class="hl">Vigente · Revalidado</dd></div>
        </dl>
      </div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="wrap">
    <div class="section-head">
      <div class="reveal"><span class="eyebrow">Socios estratégicos</span><h2>Aliados que nos hacen más fuertes</h2></div>
      <p class="reveal" data-delay="1">Trabajamos con especialistas reconocidos para que la capacitación de nuestros elementos sea integral.</p>
    </div>
    <div class="people">
      <div class="person reveal"><span class="role">Defensa personal</span><h3>Asociación Mexicana de Krav Magá</h3><ul><li>Método israelí de defensa personal y combate cuerpo a cuerpo y armado.</li><li>Dirigido a elementos de seguridad privada, escoltas y custodios.</li></ul></div>
      <div class="person reveal" data-delay="1"><span class="role">Tiro</span><h3>Professional Shooter</h3><ul><li>Entrenamiento de tiro defensivo y manejo seguro de armas.</li><li>Prácticas en campo y simulador de tiro virtual.</li></ul></div>
      <div class="person reveal" data-delay="2"><span class="role">Capacitación integral</span><h3>Yonhathan Achury</h3><ul><li>Aliado estratégico para la capacitación integral de elementos de seguridad.</li></ul></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap split reverse">
    <div class="split-media reveal">
      <img class="frame" src="assets/img/eventos.webp" alt="Evento organizado por el equipo de Grupo Noos" loading="lazy" style="aspect-ratio:4/3;object-fit:cover">
    </div>
    <div class="reveal" data-delay="1">
      <span class="eyebrow">Nuestros logros</span>
      <h2>Resultados que <span class="hl">hablan</span></h2>
      <ul class="checklist">
        <li>Incremento en ventas de los clientes atendidos de entre 15&nbsp;% y 25&nbsp;%.</li>
        <li>100&nbsp;% de satisfacción de nuestros clientes.</li>
        <li>Nuestro líder de proyectos recibió el premio al mejor organizador de eventos a nivel nacional de la revista <em>Convenciones</em> (2017).</li>
        <li>Nominación a liderazgo por excelencia a nivel nacional, HEEL (2019).</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-alt" id="clientes">
  <div class="wrap">
    <div class="section-head">
      <div class="reveal"><span class="eyebrow">Experiencia</span><h2>Nuestros principales clientes</h2></div>
      <p class="reveal" data-delay="1">Dependencias de gobierno y empresas privadas que han confiado su seguridad a nuestro equipo.</p>
    </div>
    <div class="client-cards">
{client_cards()}
    </div>
  </div>
</section>
''' + FOOTER

# ---------------------------------------------------------------- SERVICIOS
def sblock(id_, n, title, lead, bullets, tags, media, reverse=False):
    lis = "\n".join(f"          <li>{b}</li>" for b in bullets)
    tg = "".join(f'<span class="tag">{t}</span>' for t in tags)
    return f'''    <article class="service-block{" reverse" if reverse else ""}" id="{id_}">
      <div class="split-media reveal">{media}</div>
      <div class="reveal" data-delay="1">
        <div class="service-index">{n:02d}</div>
        <h2 style="font-size:clamp(1.8rem,3.6vw,2.8rem)">{title}</h2>
        <p class="lead">{lead}</p>
        <ul class="checklist">
{lis}
        </ul>
        <div class="tags">{tg}</div>
      </div>
    </article>'''

def img(src, alt):
    return f'<img class="frame" src="assets/img/{src}" alt="{alt}" loading="lazy">'
PH = '<div class="ph frame"><img src="assets/img/logo-grupo-noos.webp" alt="" loading="lazy"></div>'

servicios = head("Servicios | Grupo Noos Seguridad Privada",
  "Seguridad intramuros, escoltas con licencia de portación, consultoría en seguridad, protección civil y logística de eventos en CDMX.", "servicios.html") + header("servicios.html") + page_hero(
  "Servicios", "Lo que hacemos", 'Servicios de <span class="hl">seguridad</span> a la medida',
  "Desde el resguardo de un edificio hasta la protección personal de ejecutivos: diseñamos, planeamos e implementamos la estrategia que su organización necesita.",
  "escolta-vehiculo.webp") + f'''
<section class="section" style="padding-top:clamp(24px,4vw,48px)">
  <div class="wrap">
{sblock("intramuros",1,"Seguridad intramuros","Resguardo profesional de edificios, corporativos, plazas e instalaciones de gobierno, con y sin arma.",
 ["Guardias intramuros para oficinas, edificios e instalaciones de gobierno.","Control de accesos, rondines y bitácoras.","Servicio con y sin arma, según el nivel de riesgo.","Supervisión en sitio y reportes periódicos."],
 ["Vigilancia","Protección de bienes","Control de accesos"], img("guardias-estacionamiento.webp","Guardias de Grupo Noos en resguardo de estacionamiento"))}
{sblock("escoltas",2,"Escoltas y protección personal","Escoltas profesionales con licencia de portación incluida, para ejecutivos, funcionarios y sus familias.",
 ["Escoltas con licencia de portación de arma incluida.","Vehículo escolta y traslados seguros.","Análisis de rutas y protocolos de protección.","Personal capacitado en Krav Magá y tiro defensivo."],
 ["Protección ejecutiva","Vehículo escolta","Traslados"], img("escolta-vehiculo.webp","Escolta de Grupo Noos con vehículo escolta"), True)}
{sblock("consultoria",3,"Consultoría y estudios de seguridad","Estrategias de seguridad con enfoque organizacional, pensadas desde una óptica estratégica y especializada.",
 ["Análisis y diagnóstico de riesgos.","Diseño de protocolos y planes de seguridad.","Implementación, evaluación y actualización de la estrategia.","Seguimiento y mejora continua."],
 ["Análisis de riesgos","Protocolos","Mejora continua"], img("atencion-cliente.webp","Elemento de Grupo Noos entregando reporte a un cliente"))}
{sblock("proteccion-civil",4,"Protección civil","Consultoría y capacitación en protección civil para que su organización esté preparada ante cualquier emergencia.",
 ["Asesoría en programas internos de protección civil.","Capacitación de brigadas.","Simulacros y planes de respuesta a emergencias."],
 ["Brigadas","Simulacros","Prevención"], img("capacitacion-aula.webp","Sesión de capacitación con elementos de Grupo Noos"), True)}
{sblock("eventos",5,"Producciones integrales y logística de eventos","Diseñamos, planeamos e implementamos grandes eventos para su organización. Nuestro personal suma juventud y experiencia en la organización de eventos a gran escala.",
 ["Diseño, planificación y ejecución logística de grandes eventos.","Seguridad para eventos, convenciones y conferencias.","Liderados por un organizador de eventos premiado a nivel nacional."],
 ["Logística","Convenciones","Eventos a gran escala"], img("eventos.webp","Conferencia nacional organizada por el equipo de Grupo Noos"))}
  </div>
</section>
''' + FOOTER

# ---------------------------------------------------------------- CAPACITACIÓN
capacitacion = head("Centro de Capacitación | Grupo Noos",
  "Centro de capacitación táctica: Krav Magá israelí, combate cuerpo a cuerpo y armado, tiro y formación integral para elementos de seguridad y escoltas.", "capacitacion.html") + header("capacitacion.html") + page_hero(
  "Capacitación", "Centro de capacitación", 'Elementos <span class="hl">entrenados</span> para responder',
  "Formación integral para cuerpos de seguridad: defensa personal, combate cuerpo a cuerpo y armado, tiro y protocolos de protección.",
  "krav-panoramica.webp") + f'''
<section class="section">
  <div class="wrap split">
    <div class="split-media reveal">
      <img class="frame" src="assets/img/krav-clase.webp" alt="Instructor de Krav Magá demostrando defensa con arma ante un grupo de elementos" loading="lazy" style="aspect-ratio:4/5;object-fit:cover">
      <span class="media-tag">Combate cuerpo a cuerpo</span>
    </div>
    <div class="reveal" data-delay="1">
      <span class="eyebrow">Krav Magá israelí</span>
      <h2>Método israelí de defensa personal y combate <span class="hl">cuerpo a cuerpo y armado</span></h2>
      <p class="lead">Dirigido a cuerpos de seguridad: elementos de seguridad privada, escoltas y custodios.</p>
      <ul class="checklist">
        <li>Defensa ante agresiones con y sin arma.</li>
        <li>Control y neutralización de amenazas.</li>
        <li>Respuesta bajo estrés en escenarios reales.</li>
        <li>Avalado por la Asociación Mexicana de Krav Magá.</li>
      </ul>
    </div>
  </div>
</section>


<section class="section section-alt">
  <div class="wrap">
    <div class="section-head">
      <div class="reveal"><span class="eyebrow">En campo</span><h2>Entrenamiento <span class="hl">real</span></h2></div>
      <p class="reveal" data-delay="1">Prácticas de tiro en campo, defensa personal en tatami y formación en aula. Así se preparan nuestros elementos.</p>
    </div>
    <div class="gallery">
      <figure class="g-wide reveal"><img src="assets/img/krav-panoramica.webp" alt="Práctica grupal de Krav Magá con defensa ante arma blanca" loading="lazy"><figcaption>Krav Magá · Asociación Mexicana de Krav Magá</figcaption></figure>
      <figure class="g-tall reveal" data-delay="1"><img src="assets/img/tiro-instruccion.webp" alt="Instructor dando indicaciones en campo de tiro" loading="lazy"><figcaption>Instrucción de tiro</figcaption></figure>
      <figure class="g-tall reveal" data-delay="2"><img src="assets/img/tiro-escopeta.webp" alt="Práctica de tiro con escopeta en campo" loading="lazy"><figcaption>Tiro con arma larga</figcaption></figure>
      <figure class="reveal"><img src="assets/img/tiro-blanco.webp" alt="Blanco de tiro con impactos agrupados" loading="lazy"><figcaption>Precisión</figcaption></figure>
      <figure class="reveal" data-delay="1"><img src="assets/img/tiro-practica.webp" alt="Ejercicio táctico de control en equipo" loading="lazy"><figcaption>Ejercicio táctico</figcaption></figure>
      <figure class="g-wide reveal"><img src="assets/img/capacitacion-aula.webp" alt="Elementos de Grupo Noos en sesión de capacitación en aula" loading="lazy"><figcaption>Formación en aula</figcaption></figure>
      <figure class="g-wide reveal" data-delay="1"><img src="assets/img/equipo-noos.webp" alt="Elementos de Grupo Noos formados con uniforme oficial" loading="lazy"><figcaption>Elementos Grupo Noos</figcaption></figure>
    </div>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="section-head">
      <div class="reveal"><span class="eyebrow">Instructores</span><h2>Formados por los mejores</h2></div>
      <p class="reveal" data-delay="1">Nuestros programas los imparten instructores con trayectoria internacional y aliados especializados.</p>
    </div>
    <div class="people">
      <div class="person reveal"><span class="role">Master Instructor · 4° Darga</span><h3>Viktor Nesharim <small style="display:block;font-size:.6em;color:var(--silver);margin-top:6px">Víctor Aguilar</small></h3>
        <ul><li>26 años de experiencia en Krav Magá israelí.</li><li>Alumno directo del Gran Maestro Avi Abeceedon.</li><li>Egresado de The Academic College at Wingate, Israel.</li></ul></div>
      <div class="person reveal" data-delay="1"><span class="role">Tiro defensivo</span><h3>Professional Shooter</h3>
        <ul><li>Prácticas de tiro en campo.</li><li>Manejo seguro de armas.</li><li>Simulador de tiro virtual.</li></ul></div>
      <div class="person reveal" data-delay="2"><span class="role">Aliado estratégico</span><h3>Yonhathan Achury</h3>
        <ul><li>Capacitación integral de elementos de seguridad.</li></ul></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head center">
      <span class="eyebrow reveal">Programas</span>
      <h2 class="reveal">¿Qué aprenden nuestros elementos?</h2>
    </div>
    <div class="cards">
{card(1,"shield","Defensa personal","Krav Magá israelí aplicado a la seguridad privada, escoltas y custodios.","contacto.html")}
{card(2,"target","Tiro y manejo de armas","Tiro defensivo en campo, simulador de tiro virtual y universidad virtual.","contacto.html")}
{card(3,"car","Protección ejecutiva","Protocolos de escolta, traslados seguros y análisis de rutas.","contacto.html")}
{card(4,"building","Seguridad intramuros","Control de accesos, rondines, bitácoras y atención a incidentes.","contacto.html")}
{card(5,"life","Protección civil","Formación de brigadas, primeros auxilios y respuesta a emergencias.","contacto.html")}
{card(6,"chart","Consultoría","Capacitación a la medida para los equipos de seguridad de su empresa.","contacto.html")}
    </div>
  </div>
</section>
''' + FOOTER

# ---------------------------------------------------------------- TECNOLOGÍA
def techrow(img_, alt, eyebrow, title, items, reverse=False):
    lis = "\n".join(f"          <li>{x}</li>" for x in items)
    return f'''    <div class="tech-row{" reverse" if reverse else ""} reveal">
      <div class="media"><img src="assets/img/{img_}" alt="{alt}" loading="lazy"></div>
      <div class="body">
        <span class="eyebrow">{eyebrow}</span>
        <h2 style="font-size:clamp(1.6rem,3vw,2.3rem)">{title}</h2>
        <ul class="checklist">
{lis}
        </ul>
      </div>
    </div>'''

tecnologia = head("Tecnología | Grupo Noos Seguridad Privada",
  "Videovigilancia inteligente, arcos LPR, centros de control C4i y C5i, ciberseguridad, seguridad penitenciaria y patrullas inteligentes.", "tecnologia.html") + header("tecnologia.html") + page_hero(
  "Tecnología", "Tecnología", 'Inteligencia que <span class="hl">vigila</span> 24/7',
  "Integramos tecnología de punta a nuestras estrategias de seguridad: videovigilancia inteligente, centros de control y patrullas conectadas.",
  "tec-control.webp") + f'''
<section class="section">
  <div class="wrap">
{techrow("tec-cctv.webp","Cámara domo de videovigilancia","Videovigilancia e inteligencia","Monitoreo inteligente",
 ["CCTV con videovigilancia inteligente.","Arcos carreteros con lectura de placas (LPR).","Autopista digital.","Inteligencia.","Centros de control C4i y C5i.","Ciberseguridad."])}
{techrow("tec-control.webp","Operador en centro de control con múltiples monitores","Sistemas penitenciarios","Seguridad en prisiones",
 ["Centro de control.","Seguridad perimetral.","Detección de objetos.","Sistemas de intercomunicación."], True)}
{techrow("tec-patrulla.webp","Torreta de patrulla encendida","Unidades conectadas","Patrullas inteligentes",
 ["Control 360° con cámaras fijas y domo.","Grabación local y remota.","Cámaras LPR (lectura de placas)."])}
  </div>
</section>
''' + FOOTER

# ---------------------------------------------------------------- EQUIPAMIENTO
def gear(src, title, text):
    return f'''      <div class="gear reveal"><div class="gear-img"><img src="assets/img/{src}" alt="{title}" loading="lazy"></div><h3>{title}</h3><p>{text}</p></div>'''

equipamiento = head("Equipamiento y Unidades | Grupo Noos",
  "Uniformes tácticos, equipamiento 5.11, chalecos antibalas nivel III y IIIA, casco balístico y unidades de Grupo Noos.", "equipamiento.html") + header("equipamiento.html") + page_hero(
  "Equipamiento", "Equipamiento", 'Equipados para <span class="hl">cualquier</span> escenario',
  "Nuestros elementos portan uniforme táctico, equipo de protección balística y cuentan con unidades propias para responder con rapidez.",
  "guardias-estacionamiento.webp") + f'''

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <div class="reveal"><span class="eyebrow">Uniforme oficial</span><h2>Identidad <span class="hl">Grupo Noos</span></h2></div>
      <p class="reveal" data-delay="1">Chamarra táctica negra con escudos Grupo Noos, pantalón cargo verde olivo, fornitura completa, gorra y botas tácticas. También contamos con uniforme azul marino para servicios intramuros.</p>
    </div>
    <div class="uniform">
      <figure class="reveal"><img src="assets/img/uniforme-frente.webp" alt="Uniforme Grupo Noos, vista frontal" loading="lazy"><figcaption>Frente</figcaption></figure>
      <figure class="reveal" data-delay="1"><img src="assets/img/uniforme-espalda.webp" alt="Uniforme Grupo Noos, vista posterior con leyenda Seguridad Privada" loading="lazy"><figcaption>Espalda</figcaption></figure>
      <figure class="u-wide reveal" data-delay="2"><img src="assets/img/uniforme-perfil.webp" alt="Uniforme Grupo Noos, vistas laterales" loading="lazy"><figcaption>Perfiles</figcaption></figure>
    </div>
  </div>
</section>
<section class="section section-alt">
  <div class="wrap">
    <div class="section-head">
      <div class="reveal"><span class="eyebrow">Uniforme táctico</span><h2>Imagen profesional, desempeño táctico</h2></div>
      <p class="reveal" data-delay="1">Equipo de marcas líderes en el sector táctico, como 5.11 Tactical, o equivalentes, para mayor comodidad, resistencia y presencia.</p>
    </div>
    <div class="gear-grid">
{gear("eq-camisola.webp","Camisola táctica","5.11 Fast-Tac o similar.")}
{gear("eq-chamarra.webp","Chamarra táctica","5.11 Horn Jacket o similar.")}
{gear("eq-pantalon.webp","Pantalón táctico","5.11 Fast-Tac o similar.")}
{gear("eq-botas.webp","Botas Tactical Gear","5.11 Speed 3.0 o similar.")}
{gear("eq-fornitura.webp","Fornitura táctica","5.11 o similar.")}
{gear("eq-chaleco-tactico.webp","Chaleco antibalas","Nivel III, estándar israelí.")}
{gear("eq-chaleco-antibalas.webp","Chaleco antibalas discreto","Para uso bajo la camisa.")}
{gear("eq-casco.webp","Casco balístico MICH","Aramida, nivel IIIA, norma NIJ (9 mm y .44 Magnum).")}
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="wrap split">
    <div class="split-media frame reveal">
      <img src="assets/img/escolta-vehiculo.webp" alt="Vehículo escolta de Grupo Noos" loading="lazy">
      <span class="media-tag">Vehículo escolta</span>
    </div>
    <div class="reveal" data-delay="1">
      <span class="eyebrow">Unidades</span>
      <h2>Unidades propias, <span class="hl">listas</span> para operar</h2>
      <p class="lead">Contamos con vehículos rotulados y vehículos escolta para supervisión, traslados y protección ejecutiva.</p>
      <ul class="checklist">
        <li>Vehículos escolta para protección personal.</li>
        <li>Unidades de supervisión de servicios.</li>
        <li>Opción de patrullas inteligentes con cámaras y grabación remota.</li>
      </ul>
      <p style="margin-top:28px"><a class="link-arrow" href="tecnologia.html">Ver tecnología {I["arrow"]}</a></p>
    </div>
  </div>
</section>
''' + FOOTER

# ---------------------------------------------------------------- CONTACTO
contacto = head("Contacto | Grupo Noos Seguridad Privada",
  "Solicite una cotización de seguridad privada, escoltas o capacitación. Oficinas en Jardines del Pedregal, CDMX.", "contacto.html") + header("contacto.html") + page_hero(
  "Contacto", "Contacto", 'Solicite su <span class="hl">cotización</span>',
  "Cuéntenos qué necesita proteger. Le respondemos a la brevedad con una propuesta a la medida.",
  "tec-cctv.webp") + f'''
<section class="section">
  <div class="wrap contact-grid">
    <div class="reveal">
      <span class="eyebrow">Datos de contacto</span>
      <h2 style="font-size:clamp(1.8rem,3.4vw,2.6rem)">Estamos para servirle</h2>
      <ul class="contact-list">
        <li><span class="ic">{I["phone"]}</span><div><small>Oficina</small><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></div></li>
        <li><span class="ic">{I["wa"]}</span><div><small>WhatsApp</small><a href="https://wa.me/{WA}" target="_blank" rel="noopener">{WA_DISPLAY}</a></div></li>
        <li><span class="ic">{I["mail"]}</span><div><small>Correo</small><a href="mailto:{EMAIL}">{EMAIL}</a><br><a href="mailto:{EMAIL2}">{EMAIL2}</a></div></li>
        <li><span class="ic">{I["pin"]}</span><div><small>Oficina corporativa</small><address>{ADDR1}</address></div></li>
        <li><span class="ic">{I["pin"]}</span><div><small>Oficina Benito Juárez</small><address>{ADDR2}</address></div></li>
      </ul>
      <iframe class="map" title="Ubicación de Grupo Noos" loading="lazy" referrerpolicy="no-referrer-when-downgrade"
        src="https://www.google.com/maps?q=Blvd.+Adolfo+Ruiz+Cortines+3720,+Jardines+del+Pedregal,+01900+CDMX&output=embed"></iframe>
    </div>
    <form class="form reveal" id="contact-form" data-delay="1" novalidate>
      <span class="eyebrow">Formulario</span>
      <h3 style="margin-bottom:24px">Cuéntenos de su proyecto</h3>
      <div class="form-row">
        <div class="field"><label for="f-nombre">Nombre *</label><input id="f-nombre" name="nombre" required autocomplete="name"></div>
        <div class="field"><label for="f-empresa">Empresa</label><input id="f-empresa" name="empresa" autocomplete="organization"></div>
      </div>
      <div class="form-row">
        <div class="field"><label for="f-tel">Teléfono *</label><input id="f-tel" name="telefono" type="tel" required autocomplete="tel"></div>
        <div class="field"><label for="f-correo">Correo</label><input id="f-correo" name="correo" type="email" autocomplete="email"></div>
      </div>
      <div class="field"><label for="f-servicio">Servicio de interés *</label>
        <select id="f-servicio" name="servicio" required>
          <option value="">Seleccione una opción</option>
          <option>Seguridad intramuros</option>
          <option>Escoltas y protección personal</option>
          <option>Consultoría y estudios de seguridad</option>
          <option>Capacitación</option>
          <option>Protección civil</option>
          <option>Tecnología y monitoreo</option>
          <option>Logística de eventos</option>
          <option>Otro</option>
        </select>
      </div>
      <div class="field"><label for="f-msg">Mensaje *</label><textarea id="f-msg" name="mensaje" required placeholder="¿Qué necesita proteger? ¿Dónde? ¿Cuántos elementos y en qué horario?"></textarea></div>
      <button class="btn btn-primary" type="submit" style="width:100%">{I["wa"]} Enviar por WhatsApp</button>
      <p class="form-note">Al enviar se abrirá WhatsApp con su mensaje listo. Sus datos se usan solo para atender su solicitud.</p>
    </form>
  </div>
</section>
''' + FOOTER

pages = {"index.html": index, "nosotros.html": nosotros, "servicios.html": servicios,
         "capacitacion.html": capacitacion, "tecnologia.html": tecnologia,
         "equipamiento.html": equipamiento, "contacto.html": contacto}
for name, html in pages.items():
    (OUT / name).write_text(html, encoding="utf-8")
    print("ok", name, len(html))
