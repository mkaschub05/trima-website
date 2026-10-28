# trima.ae

Static website of Trima (parent company of VIRENTIO, LOCENTIO, EXEMPTIO). Plain HTML/CSS, no cookies,
no analytics, no external resources.

All pages are generated from one template: edit the texts in `tools/build.py`, then run
`python3 tools/build.py` and commit the generated HTML. Hosting serves the files as they are.

| Path | Content |
|---|---|
| `index.html` | English home page |
| `de/index.html` | German home page |
| `legal/`, `de/impressum/` | Legal notice – placeholder until the IFZA licence is issued |
| `assets/` | CSS and logos. Emblem, wordmark and icons are cut from Maddox's Justitia logo (Lanczos scaling + unsharp mask) |
| `tools/build.py` | Page generator (EN + DE texts) |
| `tools/socialcard.swift` | Share image `assets/img/trima-share.jpg` (1200×630) for WhatsApp/LinkedIn/X |
| `tools/sharpen.swift` | Crops/sharpens logo parts with macOS Core Image (`swiftc -O tools/sharpen.swift -o sharpen`) |
| `assets/css/intro.css`, `assets/js/intro.js` | Scroll intro on both home pages: engraving drawn on load, bronze cast on scroll; line art from `tools/lineart.swift` |
| `assets/js/site.js` | Motion: word reveal, scroll reveal, light on the Justitia bronze (pointer/scroll), card light, header; off with reduced motion |
| `CNAME` | Custom domain for GitHub Pages |

## Local preview

```bash
python3 -m http.server 8765 --bind 127.0.0.1
```

## Hosting

GitHub Pages from branch `main`, folder `/`, custom domain `trima.ae`, HTTPS enforced.

DNS is at Dynadot. Website records (only add these – the iCloud mail records MX, TXT apple-domain/SPF,
CNAME `sig1._domainkey`, TXT `_dmarc` stay untouched):

| Host | Type | Value |
|---|---|---|
| `@` | A | 185.199.108.153 |
| `@` | A | 185.199.109.153 |
| `@` | A | 185.199.110.153 |
| `@` | A | 185.199.111.153 |
| `@` | AAAA | 2606:50c0:8000::153 |
| `@` | AAAA | 2606:50c0:8001::153 |
| `@` | AAAA | 2606:50c0:8002::153 |
| `@` | AAAA | 2606:50c0:8003::153 |
| `www` | CNAME | mkaschub05.github.io |

## Open

- Legal notice / Impressum and privacy policy: real company data and legally reviewed texts after the IFZA licence.
