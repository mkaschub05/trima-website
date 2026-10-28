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
        "companies": [
            ("virentio", "VIRENTIO", "Content &amp; distribution",
             "Video editing for social media: streams, podcasts and videos cut into Reels, TikToks and Shorts "
             "– for creators and companies.",
             '<a href="https://virentio.app/" rel="noopener">virentio.app</a>', 49),
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
        "companies": [
            ("virentio", "VIRENTIO", "Content &amp; Verbreitung",
             "Videoschnitt für Social Media: Streams, Podcasts und Videos werden zu Reels, TikToks und Shorts "
             "– für Creator und Firmen.",
             '<a href="https://virentio.app/" rel="noopener">virentio.app</a>', 49),
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
    },
}


def head(t, lang, title, canonical, description=None, index=True):
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
  <link rel="icon" type="image/png" sizes="32x32" href="/assets/img/favicon-32.png">
  <link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">
  <link rel="stylesheet" href="/assets/css/site.css">
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
        items.append(f'<li><a href="https://virentio.app/" rel="noopener">{name}</a></li>' if key == "virentio"
                     else f"<li>{name}</li>")
    return f"""
  <footer class="site-footer">
    <div class="wrap">
      <div class="footer-grid">
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


def home(lang):
    t = T[lang]
    facts = "\n".join(f'      <div class="fact"><dt>{k}</dt><dd>{v}</dd></div>' for k, v in t["facts"])
    cards = []
    for i, (key, name, field, desc, status, h) in enumerate(t["companies"], 1):
        cards.append(f"""          <article class="company {key}">
            <div class="top"><img src="/assets/img/{key}.png" alt="" width="44" height="{round(44 * h / 56)}"><span class="num">0{i}</span></div>
            <h3>{name}</h3>
            <p class="field">{field}</p>
            <p class="desc">{desc}</p>
            <p class="status">{status}</p>
          </article>""")
    return head(t, lang, "Trima", t["home"], t["description"]) + header(t) + f"""
  <main>
    <div class="hero">
      <div class="wrap">
        <p class="eyebrow">{t['eyebrow']}</p>
        <h1>{t['h1']}</h1>
        <p class="lead">{t['lead']}</p>
        <div class="actions">
          <a class="btn btn-primary" href="#{t['id_contact']}">{t['cta_contact']}</a>
          <a class="btn btn-secondary" href="#{t['id_companies']}">{t['cta_companies']}</a>
        </div>
      </div>
    </div>

    <div class="wrap">
      <dl class="facts">
{facts}
      </dl>
    </div>

    <section id="{t['id_companies']}">
      <div class="wrap">
        <div class="section-head">
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
        <div class="contact-panel">
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


NOT_FOUND = """      <h1>Page not found</h1>
      <p>This page does not exist. <a href="/">Back to trima.ae</a> · <a href="/de/" lang="de">Zur Startseite</a></p>"""

PAGES = {
    "index.html": home("en"),
    "de/index.html": home("de"),
    "legal/index.html": simple("en", T["en"]["legal_title"], "/legal/", T["en"]["legal_body"]),
    "de/impressum/index.html": simple("de", T["de"]["legal_title"], "/de/impressum/", T["de"]["legal_body"]),
    "404.html": simple("en", "Page not found", "/404.html", NOT_FOUND),
}

for rel, html in PAGES.items():
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html)
    print("wrote", rel)
