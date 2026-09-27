# Dinami-K · Documents web per a les famílies (26/27)

Guia per construir documents web responsive per a l'**Escola d'Atletisme Dinami-K** (Vilanova i la Geltrú), pensats per enviar a les famílies. Idioma dels documents: **català**.

## Objectiu del projecte
Convertir documents A4/PDF (fets al Claude Design) en **pàgines web responsive** que es llegeixin bé al mòbil. Previst:
1. **Les millores** — ✅ fet (aquest repo: `web-millores-dinamik-26-27.html`).
2. **Nova estructura de quotes** — pendent.
3. **Horaris** — pendent.
4. **Pàgina central (hub)** — pendent: portada amb enllaços als 3 documents.

**Estructura decidida: TOT EN UN MATEIX SITE** (una sola desplegament a Vercel), amb rutes netes:
- `/` → hub (portada amb 3 targetes)
- `/millores/` → Les millores (aquest document)
- `/quotes/` → Nova estructura de quotes
- `/horaris/` → Horaris

Implementació estàtica a Vercel: carpetes amb `index.html` a cadascuna →
`index.html` (hub), `millores/index.html`, `quotes/index.html`, `horaris/index.html`.
⚠️ Ara mateix `index.html` = document Millores; en muntar el hub, moure Millores a `millores/index.html` i posar el hub a `index.html`.

Tots han de compartir **el mateix sistema visual** (el d'aquest document). En crear-ne un de nou, copia els tokens i els components d'aquí.

## Fitxers
- `web-millores-dinamik-26-27.html` — **font editable** (fonts via Google Fonts CDN, logo a `assets/lockup_light.png`, icones de disciplina incrustades com a data-URI). Edita AQUÍ.
- `artifact-millores-dinamik.html` / `index.html` — **versió autònoma** generada (fonts + logo incrustats, zero dependències externes). És la que es publica/desplega. NO editar a mà: es regenera des de la font.
- `assets/lockup_light.png` — logo blanc (per a fons foscos). `uploads/Dinami-k New Logo H Black transparente.png` — logo negre (per a fons clars).
- `icons/*.png` — pictogrames de disciplines (64px, extrets dels SVG de marca).

## Sistema de disseny (copia'l tal qual als altres docs)
Tokens CSS a `:root`:
```
--green:#89CD24; --green-d:#4D7515; --green-ink:#3C5A12;
--black:#0A0A0A; --ink:#1c1c1c; --paper:#F4F4F0; --paper-2:#EAEAE4;
--grey:#6A6A6A; --grey-2:#9A9A96; --line:#dcdcd6;
--amber:#B8860B; --amber-bg:#F6ECCF; --green-bg:#EAF4D6;
--f-display:"Saira Condensed"  (títols: italic, weight 900, UPPERCASE)
--f-meta:"Oswald"              (etiquetes/kickers: UPPERCASE, letter-spacing)
--f-body:"Manrope"             (text corregut)
--wrap:820px                   (columna de lectura centrada)
```
Regles: tipografia fluida amb `clamp()`; columna de lectura `max-width:var(--wrap)`; capçalera fixa negra amb logo blanc + "MILLORES · TEMPORADA 2026/27"; res de saltos de página A4.

## Catàleg de components (classes ja existents al CSS)
- **Portada**: `.cover` + `.kicker` + `.bar` + `h1` + `.sub`; `.lead` per al primer paràgraf.
- **Seccions**: `<h2 id="sNN"><span class="n">0N</span>Títol</h2>` (numerador amb contorn verd).
- **Estadístiques**: `.stats` › `.tile` (`.num`/`.lbl`).
- **Callouts**: `.callout` + variants `.dark` `.amber` `.light` `.big` (`.ct` = etiqueta, `p` = text).
- **Targetes**: `.cards3`/`.card`; `.fronts`/`.front` (+`.tech` verd fosc); `.bens`/`.ben`.
- **Timeline**: `.tl` (numerada); `.kit` (checklist 2-col); `.sched`.
- **Blocs esportius**: `.sblocks`/`.sblock`; `.chips`/`.chip` (+`.k` negre).
- **Nota al peu**: `.footnote` (cursiva Manrope + filet verd) — per a text legal/aclariments (NO fer servir `.meta` per a paràgrafs llargs: és UPPERCASE i es llegeix malament).
- **Canals / beneficis**: `.chans`/`.chan`; `.signoff` (comiat).
- **Índex (TOC)**: `.toc` amb `.toc-list` de targetes clicables (badge de número + fletxa + hover). Pista: "Toca una secció…".
- **Navegació flotant**: `.navfab` (botó ☰ fix, avall-dreta) + `.navpanel` (menú "Salta a…"). Toggle amb checkbox `#navtoggle` (hack CSS `:checked ~`) + un `<script>` mínim que tanca el panel en clicar. Cal `h2{scroll-margin-top:68px}` perquè l'àncora no quedi sota la capçalera fixa.

### Maquetes de la plataforma "Athria" (natives, sense captures)
Es reconstrueixen en HTML/CSS (les captures reals pesen massa). Dos formats:
- **Mòbil** (`.phone` marc de mòbil + `.amk` UI interna): pantalles estretes.
- **Finestra d'app ampla** (`.awrap` + barra `.wtop` estil navegador + `.awk`): pantalles d'escriptori. Subcomponents: `.ahead` (capçalera atleta), `.stat4` (4 targetes stat), `.tabs`, `.provas` (xips scroll), `.mret` (mètriques), `.chart` (SVG evolució/percentil), `.twocol`/`.drow` (detall), `.cvrow` (llistat convocatòries), `.dash` (dashboard 2 col del panell família), `.fbgrid`+`.fbopt` (feedback: preguntes en 2 columnes amb píndoles Molt/A vegades/Poc), `.dcal` (calendari).
- Totes reflueixen a 1 columna al mòbil via `@media (max-width:680px)`.
- Dades d'exemple coherents entre pantalles: atleta **Èric Bonet Prat** (Sub-12, grup Dimarts i Dijous), stats i marques reals de les captures de l'usuari. UI en **català**.

## Flux de treball (build, preview, publish)
**Generar la versió autònoma** (des de la font):
- Regenera `fonts.css` (només si no existeix): baixa el CSS de Google Fonts amb User-Agent de navegador, quedar-se només amb el subset `latin` (el català hi cap), baixar cada woff2, base64 → `@font-face`. (Fitxer a l'scratchpad de la sessió.)
- Script d'assemblatge: extreu `<style>` + `<body>` de la font, inline `fonts.css` + logo (`assets/lockup_light.png` → data-URI), escriu `artifact-millores-dinamik.html`.
**Icones de disciplina**: els SVG de marca són PNG de 512px dins d'un `<image>`. Extreure el base64 → `sips -Z 64 in.png --out out.png` → inline com a data-URI. `longitud.png` es mostra a 20px (classe `.lj`), la resta a 23px (té menys marge intern).
**Preview**: `python3 -m http.server 8765` i obrir al Browser pane. ⚠️ El pane NO repinta amb scroll per JS; per verificar una secció concreta, genera una pàgina mínima amb aquella secció a dalt de tot i fes screenshot.
**Publicar**:
- Artifact (enllaç per a famílies): `Artifact` amb el mateix `file_path` → manté la URL. Actual: https://claude.ai/code/artifact/6affa43c-c0da-4b64-8f2d-ed680d927b87
- Claude Design project `99c97f4c-52a9-4164-9d38-ecb087c35468`: `DesignSync write_files` a `Web Millores del Club Dinami-K 26-27 (CAT).html`.
**Desplegar**: `index.html` (autònom) → repo git (`main`, ja inicialitzat) → GitHub → Vercel (estàtic, sense build).

## Per fer un document NOU (quotes / horaris) amb la mateixa estructura
1. Parteix del `<head>`/`<style>` de la font actual (mateixos tokens i components).
2. Copia el shell: capçalera fixa + `.wrap` + TOC + navegació flotant + footer.
3. Escriu el contingut amb els components existents (callouts, cards, taules/estructura de quotes o graella d'horaris).
4. Reflow mòbil a `@media (max-width:680px)`.
5. Genera la versió autònoma i publica com els altres.
6. Per al **hub**: portada simple amb 3 targetes (estil `.toc`/`.card`) enllaçant els 3 documents desplegats.

## Estat del site (fet)
Site únic desplegable ja muntat i pujat a GitHub (`dinamik-ca/docs_t26_27`, branca `main`):
- `index.html` = hub (des de `web-hub-dinamik-26-27.html`, enllaços relatius `millores/` `quotes/` `horaris/`).
- `millores/index.html`, `quotes/index.html`, `horaris/index.html` = versions autònomes.
- Falta: connectar el repo a Vercel perquè desplegui i cada `push` actualitzi.

## Restriccions apreses
- ⚠️ **Charset**: els fitxers autònoms en format Artifact (comencen amb `<title>`) NO porten `<meta charset>` ni `<!DOCTYPE>`; l'embolcall de l'Artifact els afegeix, però **servits directes (Vercel/http.server) donen mojibake** amb accents/·. Per a desplegament cal anteposar `<!DOCTYPE html>` + `<meta charset="UTF-8">` + viewport a cada `index.html`.
- `DesignSync get_file` talla a 256 KiB (captures a alta resolució arriben incompletes; però la sortida es persisteix a disc i es pot processar amb python).
- Artifacts: CSP bloqueja fonts/imatges externes → cal incrustar-ho tot (per això la versió autònoma).
- Quan es fan servir pronoms per a algú, usar they/them si no se sap.
