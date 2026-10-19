"""Gera index.html e as páginas de projeto a partir de projects.py.
Uso: python3 _build/build.py  (na raiz do repositório)"""
import html, pathlib, sys, time
V = str(int(time.time()))
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from projects import PROJECTS, FEATURED, MORE

ROOT = pathlib.Path(__file__).resolve().parent.parent
EMAIL = "ftraiza@gmail.com"
WHATS = "https://wa.me/5583996488531"
MEDIUM = "https://medium.com/@raizaft"

FONT = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
        '<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wdth,wght@12..96,75..100,200..800'
        '&family=Inter:opsz,wght@14..32,400..700&family=Quicksand:wght@400..700&family=Lato:wght@400;700&display=swap" rel="stylesheet">')

MARQUEE = ["Design System", "Design de interfaces", "Pesquisa com usuários", "Design acessível", "Branding"]

e = html.escape

import hashlib, re as _re
def bust(page):
    """Acrescenta ?v=<hash do arquivo> nas imagens, para o navegador baixar a versão nova quando a imagem mudar."""
    def rep(m):
        path, ext = m.group(1), m.group(2)
        f = ROOT / ("assets/img/" + path + ext)
        if not f.exists():
            return m.group(0)
        h = hashlib.md5(f.read_bytes()).hexdigest()[:8]
        return f"assets/img/{path}{ext}?v={h}"
    return _re.sub(r'assets/img/([\w\-/]+)(\.(?:webp|png|jpg|svg))(?![?\w])', rep, page)


def head(title, desc, prefix, image=None, progress=False):
    og = f'<meta property="og:image" content="{prefix}assets/img/{image}">' if image else ""
    bar = '<div class="progress" aria-hidden="true"></div>' if progress else ""
    return f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
{og}
<meta name="theme-color" content="#f3f4f5">
<link rel="icon" href="{prefix}assets/favicon.svg" type="image/svg+xml">
{FONT}
<link rel="stylesheet" href="{prefix}assets/css/style.css?v={V}">
<script>document.documentElement.classList.add('js')</script>
</head>
<body>
{bar}
<a class="skip" href="#conteudo">Pular para o conteúdo</a>
<header class="nav"><div class="wrap">
  <a class="nav__name" href="{prefix}index.html">Raiza Tomazoni</a>
  <nav aria-label="Principal"><ul>
    <li><a class="u" href="{prefix}index.html#projetos">Projetos</a></li>
    <li><a class="u" href="{prefix}index.html#sobre">Sobre</a></li>
    <li><a class="u" href="{prefix}index.html#contato">Contato</a></li>
  </ul></nav>
</div></header>
<main id="conteudo">
"""


def foot(prefix):
    return f"""</main>
<footer class="foot"><div class="wrap">
  <span>© <span id="ano">2026</span> Raiza Tomazoni</span>
  <a class="u" href="https://www.linkedin.com/in/raizatomazoni/" target="_blank" rel="noopener">linkedin.com/in/raizatomazoni</a>
</div></footer>
<script src="{prefix}assets/js/main.js?v={V}" defer></script>
</body>
</html>
"""


def tags(items):
    return '<ul class="tags">' + "".join(f"<li>{e(t)}</li>" for t in items) + "</ul>"


def build_index():
    p = PROJECTS
    feats = []
    for slug in FEATURED:
        d = p[slug]
        feats.append(f"""
    <a class="feature" href="projetos/{slug}.html">
      <div class="feature__media" data-reveal="clip" data-cursor="Ver estudo de caso"><img src="assets/img/{d['cover']}" alt="{e(d['cover_alt'])}" width="1600" height="900" loading="lazy"></div>
      <div data-reveal>
        <h3 class="feature__title">{e(d['title'])}</h3>
        <p class="feature__text">{e(d['summary'])}</p>
        {tags(d['tags'])}
        <span class="feature__more">Ver estudo de caso <i aria-hidden="true"></i></span>
      </div>
    </a>""")
    cards = []
    for slug in MORE:
        d = p[slug]
        cards.append(f"""
      <a class="card" href="projetos/{slug}.html" data-reveal>
        <div class="card__media" data-cursor="Ver projeto"><img src="assets/img/{d['cover']}" alt="{e(d['cover_alt'])}" width="1600" height="900" loading="lazy"></div>
        <h3>{e(d['title'])}</h3>
        <p>{e(d['card_line'])}</p>
      </a>""")
    words = "".join(f"<span>{e(w)}</span>" for w in MARQUEE)

    out = head("Raiza Tomazoni — UX/UI e Product Designer",
               "Portfólio de Raiza Tomazoni, designer de produto e UX com formação em Arquitetura e Urbanismo. Projetos para a Secretaria Nacional de Periferias, SUDEMA-PB e outros.",
               "", "cover-nos-perifericos.webp")
    out += f"""
<section class="hero"><div class="wrap">
  <div class="hero__top">
  <h1 class="hero__name" data-load aria-label="Raiza Tomazoni"><span class="line" aria-hidden="true"><span>Raiza</span></span><span class="line" aria-hidden="true"><span>Tomazoni</span></span></h1>
  <figure class="hero__photo" data-load><svg class="orbit orbit--back" viewBox="-75 -75 150 150" aria-hidden="true"><g class="orbit__g" transform="rotate(-16)"><ellipse rx="70" ry="20"/></g></svg><img src="assets/img/raiza.webp" alt="Retrato em preto e branco de Raiza Tomazoni, sorrindo, com cabelo cacheado" width="800" height="800"><svg class="orbit orbit--front" viewBox="-75 -75 150 150" aria-hidden="true"><defs><clipPath id="orbit-low" clipPathUnits="userSpaceOnUse"><rect x="-80" y="0" width="160" height="80"/></clipPath></defs><g class="orbit__g" transform="rotate(-16)"><ellipse rx="70" ry="20" clip-path="url(#orbit-low)"/></g></svg></figure>
  </div>
  <div class="hero__grid">
    <p class="hero__lede" data-reveal>UX/UI e Product Designer. Transformo necessidades reais em produtos digitais simples de usar.</p>
    <div data-reveal>
      <p class="hero__now"><strong>4+ anos de experiência</strong> unificando três áreas: design, arquitetura e tecnologia.</p>
      <div class="hero__cta">
        <a class="btn" href="#contato">Falar comigo</a>
      </div>
    </div>
  </div>
  <a class="hero__scroll" href="#projetos"><span>Role para ver os projetos</span><span class="hero__scroll-arrow" aria-hidden="true">↓</span></a>
</div></section>

<div class="marquee" aria-hidden="true"><div class="marquee__track">{words}{words}{words}{words}</div></div>

<section class="section" id="projetos"><div class="wrap">
  <div class="section__head" data-reveal>
    <h2 class="section__title">Projetos</h2>
    <p class="section__note">Estudos de caso completos, com processo, pesquisa e decisões de design.</p>
  </div>
  {''.join(feats)}
</div></section>

<section class="section"><div class="wrap">
  <div class="section__head" data-reveal>
    <h2 class="section__title">Mais trabalhos</h2>
  </div>
  <div class="grid">{''.join(cards)}
  </div>
</div></section>

<section class="section" id="sobre"><div class="wrap about">
  <div class="about__bio" data-reveal>
    <h2 class="section__title" style="margin-bottom:32px">Sobre</h2>
    <p>Sou UX/UI e Product Designer em João Pessoa, na Paraíba, e trabalho com produtos digitais desde 2022.</p>
    <p>Sou formada em Arquitetura e Urbanismo e trago na bagagem do curso o hábito de começar pelo uso: quem vai passar por ali, com que pressa, com que dúvida. Hoje curso Sistemas para Internet e, com isso, tenho o olhar de quem constrói: entendo como uma interface vira código, desenho soluções que cabem no que o time consegue entregar e converso com quem desenvolve na mesma língua.</p>
    <p>No dia a dia, trabalho com pesquisa com usuários, testes de usabilidade, prototipagem de alta fidelidade e design systems, tanto em produtos novos quanto em produtos que já existem e precisam crescer.</p>
    <dl class="facts">
      <div><dt>4</dt><dd>anos de experiência em design de produto</dd></div>
      <div><dt>2</dt><dd>esferas de governo, federal e estadual</dd></div>
      <div><dt>3</dt><dd>áreas: arquitetura, tecnologia e design</dd></div>
    </dl>
    <blockquote class="quote">Há um gosto de vitória e encanto na condição de ser simples. Não é preciso muito para ser muito.<cite>Lina Bo Bardi</cite></blockquote>
  </div>
  <div class="timeline" data-reveal>
    <h3>Experiência</h3>
    <ol>
      <li><time>2025 – hoje</time><div><b>UX/UI e Product Designer</b><span>Secretaria Nacional de Periferias, Ministério das Cidades</span><em>Design system, prototipação, UX research e testes de usabilidade</em></div></li>
      <li><time>2022 – hoje</time><div><b>UX/UI e Product Designer</b><span>SUDEMA, Superintendência de Administração do Meio Ambiente da Paraíba</span><em>Design system, prototipação, UX research e testes de usabilidade</em></div></li>
      <li><time>2021 – 2022</time><div><b>Arquiteta e Urbanista</b><span>Noda Arquitetura</span><em>Projeto de arquitetura e design de interiores</em></div></li>
      <li><time>2020 – 2022</time><div><b>Arquiteta e Urbanista</b><span>Oficina Espacial</span><em>Gestão de projeto e projeto de arquitetura</em></div></li>
      <li><time>2019 – 2020</time><div><b>Designer Gráfica</b><span>Maquinaria</span><em>Direção de arte, conteúdo para redes sociais e mídias físicas</em></div></li>
    </ol>
    <h3>Monitorias no IFPB</h3>
    <ol>
      <li><time>2025</time><div><b>Programação para Web II</b><span>Instituto Federal da Paraíba</span></div></li>
      <li><time>2024</time><div><b>Linguagem de Marcação</b><span>Instituto Federal da Paraíba</span></div></li>
      <li><time>2023</time><div><b>Interação Humano-Máquina</b><span>Instituto Federal da Paraíba</span></div></li>
    </ol>
    <h3>Formação</h3>
    <ol>
      <li><time>2023 – hoje</time><div><b>Tecnólogo em Sistemas para Internet</b><span>IFPB, Instituto Federal da Paraíba</span></div></li>
      <li><time>2024</time><div><b>Especialização em UX, UI e Design de Produto</b><span>UX Unicórnio</span></div></li>
      <li><time>2014 – 2015</time><div><b>Intercâmbio em Architectural and Environmental Design</b><span>Sheffield Hallam University, Reino Unido</span></div></li>
      <li><time>2011 – 2019</time><div><b>Bacharelado em Arquitetura e Urbanismo</b><span>UFCG, Universidade Federal de Campina Grande</span></div></li>
    </ol>
    <h3>O que eu faço</h3>
    <ul class="skills">
      <li>Design de produto</li><li>Design system</li><li>UX Research</li><li>Testes de usabilidade</li>
      <li>Prototipação</li><li>Design de interfaces</li><li>Identidade visual</li>
    </ul>
    <h3 class="timeline__h">Ferramentas</h3>
    <ul class="skills skills--tools">
      <li>Figma</li><li>Framer</li><li>Adobe XD</li><li>Balsamiq</li><li>Maze</li><li>Miro</li><li>Illustrator</li><li>Photoshop</li>
      <li>HTML, CSS e JavaScript</li><li>Bootstrap</li><li>SQL</li><li>Git</li><li>Claude Code</li>
      <li>Notion</li><li>Jira</li><li>Confluence</li><li>Trello</li><li>ClickUp</li><li>Teams</li>
    </ul>
    <h3 class="timeline__h">Como trabalho</h3>
    <p class="soft">Empatia, pensamento crítico, atenção aos detalhes, curiosidade e colaboração. Gosto de resolver problemas em equipe, com organização, comunicação clara e liderança quando o projeto pede.</p>
  </div>
</div></section>

<section class="section contact" id="contato"><div class="wrap">
  <h2 class="section__title" data-reveal>Vamos conversar</h2>
  <div class="contact__row" data-reveal>
    <a class="contact__mail" href="mailto:{EMAIL}">{EMAIL}</a>
    <button class="copy" type="button" data-copy="{EMAIL}">Copiar e-mail</button>
  </div>
  <div class="contact__links" data-reveal>
    <a class="btn" href="https://www.linkedin.com/in/raizatomazoni/" target="_blank" rel="noopener">LinkedIn</a>
    <a class="btn" href="{WHATS}" target="_blank" rel="noopener">WhatsApp</a>
  </div>
</div></section>
"""
    out += foot("")
    (ROOT / "index.html").write_text(bust(out), encoding="utf-8")


def render_media(m):
    kind = m[0]
    if kind == "html":
        return f'<div class="figure" data-reveal>{m[1]}</div>'
    if kind == "img":
        _, src, alt, cap = m
        c = f"<figcaption>{e(cap)}</figcaption>" if cap else ""
        return f'<figure class="figure" data-reveal><a class="figure__frame" href="../assets/img/{src}" target="_blank" rel="noopener" data-cursor="Ampliar"><img src="../assets/img/{src}" alt="{e(alt)}" loading="lazy"></a>{c}</figure>'
    if kind == "scroll":
        _, src, alt, cap = m
        return (f'<figure class="figure" data-reveal><div class="scrollframe" tabindex="0" role="region" aria-label="{e(alt)}, role para ver a página inteira">'
                f'<img src="../assets/img/{src}" alt="{e(alt)}" loading="lazy"></div><figcaption>{e(cap)}</figcaption></figure>')
    if kind == "phones":
        _, items, cap = m
        imgs = "".join(f'<img src="../assets/img/{s}" alt="{e(a)}" loading="lazy">' for s, a in items)
        return f'<figure class="figure" data-reveal><div class="phones">{imgs}</div><figcaption>{e(cap)}</figcaption></figure>'
    if kind == "pair":
        _, items, cap = m
        imgs = "".join(f'<a class="figure__frame" href="../assets/img/{s}" target="_blank" rel="noopener" data-cursor="Ampliar"><img src="../assets/img/{s}" alt="{e(a)}" loading="lazy"></a>' for s, a in items)
        c = f"<figcaption>{e(cap)}</figcaption>" if cap else ""
        return f'<figure class="figure" data-reveal><div class="pair">{imgs}</div>{c}</figure>'
    raise ValueError(kind)


def live_html(d):
    if not d.get("live"):
        return ""
    url, label = d["live"]
    return (f'<div class="live" data-reveal><span class="live__label">{e(d.get("live_label", "Veja o projeto no ar"))}</span>'
            f'<a class="live__link" href="{url}" target="_blank" rel="noopener">{e(label)} <span aria-hidden="true">↗</span></a></div>')


def build_case(slug, nxt):
    d = PROJECTS[slug]
    meta = "".join(f"<div><dt>{e(k)}</dt><dd>{v}</dd></div>" for k, v in d["meta"])
    blocks = []
    for b in d["blocks"]:
        media = "".join(render_media(m) for m in b.get("media", []))
        if b.get("sticky_img"):
            src, alt = b["sticky_img"]
            blocks.append(f'<section class="pin"><div class="pin__text"><h2>{e(b["title"])}</h2><div class="block__body">{b["html"]}</div></div>'
                          f'<figure class="pin__media"><img src="../assets/img/{src}" alt="{e(alt)}" loading="lazy"></figure></section>{media}')
            continue
        blocks.append(f'<section class="block"><h2 data-reveal>{e(b["title"])}</h2><div class="block__body" data-reveal>{b["html"]}</div></section>{media}')
    n = PROJECTS[nxt]
    out = head(f"{d['title']} — Raiza Tomazoni", d["summary"], "../", d.get("cover"), progress=True)
    out += f"""
<section class="case-hero"><div class="wrap">
  <a class="back" href="../index.html#projetos"><span aria-hidden="true">←</span> Voltar para projetos</a>
  <h1 data-load><span class="line"><span>{e(d['title'])}</span></span></h1>
  <p class="lede" data-reveal>{e(d['lede'])}</p>
  <dl class="meta" data-reveal>{meta}</dl>
</div></section>
<div class="wrap case-cover"><div class="case-cover__frame" data-reveal="clip"><img src="../assets/img/{d.get('case_cover', d['cover'])}" alt="{e(d.get('case_cover_alt', d['cover_alt']))}"></div></div>
<div class="wrap">
{''.join(blocks)}
{live_html(d)}
<a class="next" href="{nxt}.html"><span class="next__in"><span><span class="next__label">Próximo projeto</span><span class="next__name">{e(n['title'])}</span></span><span class="next__arrow" aria-hidden="true">→</span></span></a>
</div>
"""
    out += foot("../")
    (ROOT / "projetos").mkdir(exist_ok=True)
    (ROOT / "projetos" / f"{slug}.html").write_text(bust(out), encoding="utf-8")


if __name__ == "__main__":
    build_index()
    order = FEATURED + MORE
    for i, s in enumerate(order):
        build_case(s, order[(i + 1) % len(order)])
    print("ok:", ", ".join(order))
