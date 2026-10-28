#!/usr/bin/env python3
"""Generate the static pages of trima.ae from one template (EN + DE).

Edit texts here, then run:  python3 tools/build.py
The generated HTML files are committed; GitHub Pages serves them as they are.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

T = {
    "en": {
        "home": "/", "legal": "/legal/", "other_lang": "de", "other_home": "/de/", "other_label": "DE",
        "other_name": "Deutsch",
        "nav_companies": "Companies", "nav_contact": "Contact", "id_companies": "companies", "id_contact": "contact",
        "home_label": "Trima – home",
        "description": "Trima is the parent company of VIRENTIO, LOCENTIO and EXEMPTIO. "
                       "Currently being established in the IFZA free zone, Dubai. Contact: contact@trima.ae",
        "og_description": "Parent company of VIRENTIO, LOCENTIO and EXEMPTIO.",
        "eyebrow": "Trima · Dubai",
        "h1": "The parent company of a group of ventures in content, data and business software.",
        "lead": "Trima brings VIRENTIO, LOCENTIO and EXEMPTIO together under one roof. "
                "The company is currently being established in the IFZA free zone, Dubai.",
        "cta_contact": "Get in touch", "cta_companies": "Our companies",
        "facts": [("Group", "Three companies"),
                  ("Seat", "Dubai, IFZA free zone – in formation"),
                  ("Contact", '<a href="mailto:contact@trima.ae">contact@trima.ae</a>')],
        "companies_eyebrow": "The group", "companies_h2": "Our companies",
        "companies_intro": "Three companies under one roof, each with its own focus.",
        # VIRENTIO is shown as the wide lead card. Never mention AI/automation for the editing itself
        # (decision D-129); AI videos are an openly labelled service line of their own (D-135).
        "virentio": {
            "url": "https://virentio.app/en",
            "lead": "VIRENTIO turns streams, podcasts and videos into content that reaches people – for creators, "
                    "agencies and companies, with a personal contact person from the first clip on.",
            "services_title": "What we do",
            "services": ["Clips for TikTok, Instagram Reels and YouTube Shorts",
                         "Long-form edits and complete podcast packages",
                         "Thumbnails and titles",
                         "Publishing across several accounts, with clear reporting",
                         "Translation and dubbing",
                         "AI videos and animations"],
            "button": "Visit virentio.app",
        },
        "companies": [
            ("virentio", "VIRENTIO", "Social media agency", "", "", 49),
            ("locentio", "LOCENTIO", "Data &amp; technology",
             "LOCENTIO develops data-driven software. More details will follow at launch.",
             "In development", 58),
            ("exemptio", "EXEMPTIO", "Finance &amp; tax for SMEs",
             "A financial and business operating system for small and mid-sized companies: taxes, payroll, "
             "costs and cash flow – correct, documented and in cooperation with tax advisors.",
             "In development", 50),
        ],
        "contact_eyebrow": "Contact", "contact_h2": "Get in touch",
        "contact_text": "For partners, banks and all other enquiries, please write to us.",
        "contact_button": "Write an email",
        "footer_about": "Parent company of VIRENTIO, LOCENTIO and EXEMPTIO. Dubai, United Arab Emirates – in formation.",
        "footer_companies": "Companies", "footer_contact": "Contact", "footer_legal": "Legal",
        "legal_label": "Legal notice", "footer_note": "No cookies, no tracking.",
        "legal_title": "Legal notice",
        "legal_body": """      <h1>Legal notice</h1>
      <p>Trima is currently being established in the IFZA free zone, Dubai, United Arab Emirates.</p>
      <p>The full company details (registered name, licence number and registered address) will be published on this page as soon as the licence has been issued.</p>
      <h2>Contact</h2>
      <p><a href="mailto:contact@trima.ae">contact@trima.ae</a></p>
      <h2>This website</h2>
      <p>This website does not use cookies, analytics or any third-party resources.</p>""",
        "logo_alt": "Trima",
        "art_alt": "Justitia with scales – the Trima emblem",
    },
    "de": {
        "home": "/de/", "legal": "/de/impressum/", "other_lang": "en", "other_home": "/", "other_label": "EN",
        "other_name": "English",
        "nav_companies": "Firmen", "nav_contact": "Kontakt", "id_companies": "firmen", "id_contact": "kontakt",
        "home_label": "Trima – Startseite",
        "description": "Trima ist die Dachgesellschaft von VIRENTIO, LOCENTIO und EXEMPTIO, derzeit in Gründung "
                       "in der Freihandelszone IFZA, Dubai. Kontakt: contact@trima.ae",
        "og_description": "Dachgesellschaft von VIRENTIO, LOCENTIO und EXEMPTIO.",
        "eyebrow": "Trima · Dubai",
        "h1": "Die Dachgesellschaft einer Gruppe von Unternehmen für Content, Daten und Unternehmens&shy;software.",
        "lead": "Unter Trima sind VIRENTIO, LOCENTIO und EXEMPTIO gebündelt. "
                "Die Gesellschaft wird derzeit in der Freihandelszone IFZA in Dubai gegründet.",
        "cta_contact": "Kontakt aufnehmen", "cta_companies": "Unsere Firmen",
        "facts": [("Gruppe", "Drei Firmen"),
                  ("Sitz", "Dubai, Freihandelszone IFZA – in Gründung"),
                  ("Kontakt", '<a href="mailto:contact@trima.ae">contact@trima.ae</a>')],
        "companies_eyebrow": "Die Gruppe", "companies_h2": "Unsere Firmen",
        "companies_intro": "Drei Firmen unter einem Dach, jede mit eigenem Schwerpunkt.",
        "virentio": {
            "url": "https://virentio.app/",
            "lead": "VIRENTIO macht aus Streams, Podcasts und Videos Inhalte, die ankommen – für Creator, Agenturen "
                    "und Unternehmen, mit fester Ansprechperson vom ersten Clip an.",
            "services_title": "Was wir machen",
            "services": ["Clips für TikTok, Instagram Reels und YouTube Shorts",
                         "Langvideo-Schnitt und Podcast-Komplettpakete",
                         "Thumbnails und Titel",
                         "Veröffentlichung über mehrere Accounts, mit klarem Reporting",
                         "Übersetzung und Synchronisation",
                         "KI-Videos und Animationen"],
            "button": "Zu virentio.app",
        },
        "companies": [
            ("virentio", "VIRENTIO", "Social-Media-Agentur", "", "", 49),
            ("locentio", "LOCENTIO", "Daten &amp; Technologie",
             "LOCENTIO entwickelt datengestützte Software. Mehr dazu zum Start.",
             "In Entwicklung", 58),
            ("exemptio", "EXEMPTIO", "Finanzen &amp; Steuern für KMU",
             "Ein Finanz- und Betriebssystem für kleine und mittlere Unternehmen: Steuern, Lohn, Kosten und "
             "Liquidität – korrekt, belegt und in Zusammenarbeit mit Steuerberatern.",
             "In Entwicklung", 50),
        ],
        "contact_eyebrow": "Kontakt", "contact_h2": "Schreiben Sie uns",
        "contact_text": "Für Partner, Banken und alle anderen Anfragen erreichen Sie uns per E-Mail.",
        "contact_button": "E-Mail schreiben",
        "footer_about": "Dachgesellschaft von VIRENTIO, LOCENTIO und EXEMPTIO. Dubai, Vereinigte Arabische Emirate – in Gründung.",
        "footer_companies": "Firmen", "footer_contact": "Kontakt", "footer_legal": "Rechtliches",
        "legal_label": "Impressum", "footer_note": "Keine Cookies, kein Tracking.",
        "legal_title": "Impressum",
        "legal_body": """      <h1>Impressum</h1>
      <p>Trima wird derzeit in der Freihandelszone IFZA in Dubai, Vereinigte Arabische Emirate, gegründet.</p>
      <p>Die vollständigen Angaben zur Gesellschaft (Firma, Lizenznummer und Anschrift) werden hier veröffentlicht, sobald die Lizenz erteilt ist.</p>
      <h2>Kontakt</h2>
      <p><a href="mailto:contact@trima.ae">contact@trima.ae</a></p>
      <h2>Diese Website</h2>
      <p>Diese Website verwendet keine Cookies, keine Analyse-Werkzeuge und keine Inhalte von Drittanbietern.</p>""",
        "logo_alt": "Trima",
        "art_alt": "Justitia mit Waage – das Trima-Zeichen",
    },
}


def head(t, lang, title, canonical, description=None, index=True, extra=""):
    alt = ""
    if index:
        alt = """
  <link rel="alternate" hreflang="en" href="https://trima.ae/">
  <link rel="alternate" hreflang="de" href="https://trima.ae/de/">
  <link rel="alternate" hreflang="x-default" href="https://trima.ae/">
  <meta property="og:type" content="website">
  <meta property="og:title" content="Trima">
  <meta property="og:description" content="{og}">
  <meta property="og:url" content="https://trima.ae{canonical}">
  <meta property="og:image" content="https://trima.ae/assets/img/trima-logo.jpg">""".format(
            og=t["og_description"], canonical=canonical)
    desc = f'\n  <meta name="description" content="{description}">' if description else ""
    robots = "" if index else '\n  <meta name="robots" content="noindex">'
    return f"""<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>{desc}{robots}
  <link rel="canonical" href="https://trima.ae{canonical}">{alt}
  <meta name="theme-color" content="#080605">
  <link rel="icon" href="/favicon.ico" sizes="any">
  <link rel="icon" type="image/png" sizes="32x32" href="/assets/img/favicon-32.png">
  <link rel="icon" type="image/png" sizes="48x48" href="/assets/img/favicon-48.png">
  <link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">
  <link rel="stylesheet" href="/assets/css/site.css">
  <script>document.documentElement.classList.add("js")</script>
  <script src="/assets/js/site.js" defer></script>{extra}
</head>
<body>"""


def brand(t):
    return f"""<a class="brand" href="{t['home']}" aria-label="{t['home_label']}">
        <img class="emblem" src="/assets/img/trima-emblem.webp" alt="" width="44" height="44">
        <img class="word" src="/assets/img/trima-wordmark.webp" alt="{t['logo_alt']}" width="118" height="23">
      </a>"""


def header(t, on_home=True):
    base = "" if on_home else t["home"]
    return f"""
  <header class="site-header">
    <div class="wrap">
      {brand(t)}
      <nav class="nav" aria-label="Menu">
        <a class="hide-sm" href="{base}#{t['id_companies']}">{t['nav_companies']}</a>
        <a href="{base}#{t['id_contact']}">{t['nav_contact']}</a>
        <a class="lang" href="{t['other_home']}" hreflang="{t['other_lang']}" lang="{t['other_lang']}">{t['other_label']}</a>
      </nav>
    </div>
  </header>
"""


def footer(t, lang):
    items = []
    for key, name, *_ in t["companies"]:
        items.append(f'<li><a href="{t["virentio"]["url"]}" rel="noopener">{name}</a></li>' if key == "virentio"
                     else f"<li>{name}</li>")
    return f"""
  <footer class="site-footer">
    <div class="wrap">
      <div class="footer-grid" data-reveal>
        <div>
          {brand(t)}
          <p>{t['footer_about']}</p>
        </div>
        <div>
          <h4>{t['footer_companies']}</h4>
          <ul>{''.join(items)}</ul>
        </div>
        <div>
          <h4>{t['footer_contact']}</h4>
          <ul><li><a href="mailto:contact@trima.ae">contact@trima.ae</a></li></ul>
        </div>
        <div>
          <h4>{t['footer_legal']}</h4>
          <ul>
            <li><a href="{t['legal']}">{t['legal_label']}</a></li>
            <li><a href="{t['other_home']}" hreflang="{t['other_lang']}" lang="{t['other_lang']}">{t['other_name']}</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom"><span>© 2026 Trima</span><span>{t['footer_note']}</span></div>
    </div>
  </footer>
</body>
</html>
"""


def home(lang, intro="", extra_head="", index=True, canonical=None):
    t = T[lang]
    facts = "\n".join(f'      <div class="fact"><dt>{k}</dt><dd>{v}</dd></div>' for k, v in t["facts"])
    cards = []
    for i, (key, name, field, desc, status, h) in enumerate(t["companies"], 1):
        if key == "virentio":
            v = t["virentio"]
            items = "".join(f"<li>{x}</li>" for x in v["services"])
            cards.append(f"""          <article class="company virentio featured" data-reveal data-spot>
            <div class="featured-main">
              <div class="top"><img src="/assets/img/virentio.png" alt="" width="52" height="{round(52 * h / 56)}"><span class="num">0{i}</span></div>
              <h3>{name}</h3>
              <p class="field">{field}</p>
              <p class="desc">{v['lead']}</p>
              <a class="btn btn-accent" href="{v['url']}" rel="noopener">{v['button']} <span aria-hidden="true">→</span></a>
            </div>
            <div class="featured-services">
              <p class="services-title">{v['services_title']}</p>
              <ul class="services">{items}</ul>
            </div>
          </article>""")
            continue
        cards.append(f"""          <article class="company {key}" data-reveal data-spot style="--d: {(i - 1) * .12:.2f}s">
            <div class="top"><img src="/assets/img/{key}.png" alt="" width="44" height="{round(44 * h / 56)}"><span class="num">0{i}</span></div>
            <h3>{name}</h3>
            <p class="field">{field}</p>
            <p class="desc">{desc}</p>
            <p class="status">{status}</p>
          </article>""")
    return head(t, lang, "Trima", canonical or t["home"], t["description"], index=index, extra=extra_head) + header(t) + f"""
  <main>{intro}
    <div class="hero">
      <div class="wrap hero-grid">
        <div class="hero-text">
          <p class="eyebrow" data-reveal><span class="rule"></span>{t['eyebrow']}</p>
          <h1 data-words>{t['h1']}</h1>
          <p class="lead" data-reveal style="--d: .5s">{t['lead']}</p>
          <div class="actions" data-reveal style="--d: .65s">
            <a class="btn btn-primary" href="#{t['id_contact']}">{t['cta_contact']}</a>
            <a class="btn btn-secondary" href="#{t['id_companies']}">{t['cta_companies']}</a>
          </div>
        </div>
        <figure class="hero-art" data-reveal style="--d: .2s">
          <div class="frame">
            <picture>
              <source srcset="/assets/img/justitia.webp" type="image/webp">
              <img src="/assets/img/justitia.jpg" alt="{t['art_alt']}" width="800" height="778">
            </picture>
            <span class="light" aria-hidden="true"></span>
          </div>
        </figure>
      </div>
    </div>

    <div class="wrap">
      <dl class="facts" data-reveal>
{facts}
      </dl>
    </div>

    <section id="{t['id_companies']}">
      <div class="wrap">
        <div class="section-head" data-reveal>
          <div>
            <p class="eyebrow">{t['companies_eyebrow']}</p>
            <h2>{t['companies_h2']}</h2>
          </div>
          <p>{t['companies_intro']}</p>
        </div>
        <div class="companies">
{chr(10).join(cards)}
        </div>
      </div>
    </section>

    <section id="{t['id_contact']}">
      <div class="wrap">
        <div class="contact-panel" data-reveal data-spot>
          <div>
            <p class="eyebrow">{t['contact_eyebrow']}</p>
            <h2>{t['contact_h2']}</h2>
            <p>{t['contact_text']}</p>
          </div>
          <div class="mail-box">
            <a class="mail" href="mailto:contact@trima.ae">contact@trima.ae</a>
            <a class="btn btn-primary" href="mailto:contact@trima.ae">{t['contact_button']}</a>
          </div>
        </div>
      </div>
    </section>
  </main>
""" + footer(t, lang)


def simple(lang, title, canonical, body):
    t = T[lang]
    return head(t, lang, f"{title} – Trima", canonical, index=False) + header(t, on_home=False) + f"""
  <main class="wrap">
    <div class="page">
{body}
    </div>
  </main>
""" + footer(t, lang)


# ---------- Intro previews (not linked, noindex) ----------
LINES_DE = [("Eine Dachgesellschaft.", .16, .86), ("Drei Firmen.", .32, .86), ("<em>Echte Lösungen.</em>", .48, .86)]


def lines_html():
    return "\n".join(f'          <p class="line" style="--a: {a}; --b: {b}">{txt}</p>' for txt, a, b in LINES_DE)


INTROS = {
    "a": ("Bühne", "Justitia bildschirmfüllend, TRIMA wischt sich auf. Beim Scrollen dreht sie sich leicht, "
                   "Licht wandert über die Bronze, drei Zeilen erscheinen, dann rückt sie nach rechts.", f"""
    <section class="scene intro-a" data-scene aria-label="Intro">
      <div class="stage">
        <div class="figure">
          <img src="/assets/img/justitia-hi.webp" alt="Justitia mit Waage – das Trima-Zeichen" width="1065" height="1035">
          <span class="glow" aria-hidden="true"></span>
        </div>
        <img class="wordmark wordmark-wipe" src="/assets/img/trima-wordmark-hi.webp" alt="Trima" width="960" height="190">
        <div class="lines">
{lines_html()}
        </div>
        <div class="scroll-hint">Scrollen</div>
      </div>
    </section>"""),
    "b": ("Medaille", "Justitia als Bronze-Münze. Beim Scrollen dreht sie sich um (Rückseite TRIMA) und fliegt "
                      "am Ende nach oben links, wo das Logo sitzt.", """
    <section class="scene intro-b" data-scene aria-label="Intro">
      <div class="stage">
        <div class="coin">
""" + "\n".join(f'          <span class="rim" style="--z: {-z}px" aria-hidden="true"></span>' for z in range(1, 9)) + f"""
          <div class="face front"><img src="/assets/img/justitia-coin.webp" alt="Justitia mit Waage – das Trima-Zeichen" width="720" height="720"></div>
          <div class="face back" style="transform: rotateY(180deg) translateZ(9px)"><b>TRIMA</b><span>DUBAI</span></div>
        </div>
        <div class="lines">
{lines_html()}
        </div>
        <div class="scroll-hint">Scrollen</div>
      </div>
    </section>"""),
    "c": ("Schriftzug", "Ein riesiges TRIMA. Beim Scrollen gehen die Buchstaben auseinander und Justitia steigt "
                        "dahinter auf, dann erscheinen die drei Zeilen.", """
    <section class="scene intro-c" data-scene aria-label="Intro">
      <div class="stage">
        <div class="figure">
          <img src="/assets/img/justitia-hi.webp" alt="Justitia mit Waage – das Trima-Zeichen" width="1065" height="1035">
        </div>
        <div class="letters" aria-label="Trima">""" + "".join(
            f'<span class="ltr" style="--k: {i - 2}" aria-hidden="true"><span style="--i: {i}">{c}</span></span>'
            for i, c in enumerate("TRIMA")) + f"""</div>
        <div class="lines">
{lines_html()}
        </div>
        <div class="scroll-hint">Scrollen</div>
      </div>
    </section>"""),
}

INTRO_HEAD = """
  <link rel="stylesheet" href="/assets/css/intro.css">
  <script src="/assets/js/intro.js" defer></script>"""


def preview_index():
    t = T["de"]
    cards = "\n".join(f"""          <a class="company" href="/vorschau/{k}/" style="text-decoration: none; --accent: var(--bronze)">
            <div class="top"><span class="num">{k.upper()}</span></div>
            <h3>{name}</h3>
            <p class="desc">{desc}</p>
            <p class="status">Ansehen</p>
          </a>""" for k, (name, desc, _) in INTROS.items())
    body = f"""      <h1>Vorschau: Intro-Varianten</h1>
      <p>Nicht verlinkt und nicht für Suchmaschinen. Jede Variante zeigt das Intro vor der bisherigen Startseite. Die echte Drehung der Figur (3D-Modell oder KI-Video) kommt später auf dem eigenen Server dazu – hier ist sie nur angedeutet.</p>
      <div class="companies" style="grid-template-columns: 1fr; margin-top: 32px">
{cards}
          <a class="company" href="/de/" style="text-decoration: none; --accent: var(--bronze)">
            <div class="top"><span class="num">LIVE</span></div>
            <h3>Aktuelle Seite</h3>
            <p class="desc">Zum Vergleich: die Startseite, wie sie jetzt online ist.</p>
            <p class="status">Ansehen</p>
          </a>
      </div>"""
    return simple("de", "Vorschau", "/vorschau/", body)


NOT_FOUND = """      <h1>Page not found</h1>
      <p>This page does not exist. <a href="/">Back to trima.ae</a> · <a href="/de/" lang="de">Zur Startseite</a></p>"""

PAGES = {
    "index.html": home("en"),
    "de/index.html": home("de"),
    "legal/index.html": simple("en", T["en"]["legal_title"], "/legal/", T["en"]["legal_body"]),
    "de/impressum/index.html": simple("de", T["de"]["legal_title"], "/de/impressum/", T["de"]["legal_body"]),
    "404.html": simple("en", "Page not found", "/404.html", NOT_FOUND),
    "vorschau/index.html": preview_index(),
}
for k, (_, _, html) in INTROS.items():
    PAGES[f"vorschau/{k}/index.html"] = home("de", intro=html, extra_head=INTRO_HEAD, index=False,
                                             canonical=f"/vorschau/{k}/")

for rel, html in PAGES.items():
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html)
    print("wrote", rel)
