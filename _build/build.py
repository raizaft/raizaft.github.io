"""Gera index.html e as páginas de projeto a partir de projects.py.
Uso: python3 _build/build.py  (na raiz do repositório)"""
import html, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from projects import PROJECTS, FEATURED, MORE

ROOT = pathlib.Path(__file__).resolve().parent.parent
EMAIL = "ftraiza@gmail.com"
WHATS = "https://wa.me/5583996488531"
MEDIUM = "https://medium.com/@raizaft"

FONT = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
        '<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,100..900&display=swap" rel="stylesheet">')


def head(title, desc, prefix, image=None):
    og = f'<meta property="og:image" content="{prefix}assets/img/{image}">' if image else ""
    return f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
{og}
<link rel="icon" href="{prefix}assets/favicon.svg" type="image/svg+xml">
{FONT}
<link rel="stylesheet" href="{prefix}assets/css/style.css">
</head>
<body>
<a class="skip" href="#conteudo">Pular para o conteúdo</a>
<header class="nav"><div class="wrap">
  <a class="nav__name" href="{prefix}index.html">Raiza <span>Tomazoni</span></a>
  <nav aria-label="Principal"><ul>
    <li><a href="{prefix}index.html#projetos">Projetos</a></li>
    <li><a href="{prefix}index.html#sobre">Sobre</a></li>
    <li><a href="{prefix}index.html#contato">Contato</a></li>
  </ul></nav>
</div></header>
<main id="conteudo">
"""


def foot():
    return """</main>
<footer class="foot"><div class="wrap">
  <span>© <span id="ano">2026</span> Raiza Tomazoni</span>
  <span>Desenhado e construído em João Pessoa, PB</span>
</div></footer>
<script>document.getElementById('ano').textContent=new Date().getFullYear();</script>
</body>
</html>
"""


def tags(items):
    return '<ul class="tags">' + "".join(f"<li>{html.escape(t)}</li>" for t in items) + "</ul>"


def build_index():
    p = PROJECTS
    feats = []
    for slug in FEATURED:
        d = p[slug]
        feats.append(f"""
    <a class="feature" href="projetos/{slug}.html">
      <div class="feature__media"><img src="assets/img/{d['cover']}" alt="{html.escape(d['cover_alt'])}" width="1600" height="900" loading="lazy"></div>
      <div>
        <p class="feature__client">{html.escape(d['client'])}</p>
        <h3 class="feature__title">{html.escape(d['title'])}</h3>
        <p class="feature__text">{html.escape(d['summary'])}</p>
        {tags(d['tags'])}
        <span class="feature__more">Ver estudo de caso</span>
      </div>
    </a>""")
    cards = []
    for slug in MORE:
        d = p[slug]
        if d.get("cover"):
            media = f'<div class="card__media"><img src="assets/img/{d["cover"]}" alt="{html.escape(d["cover_alt"])}" width="1600" height="900" loading="lazy"></div>'
        else:
            media = f'<div class="card__media card__media--type"><div><strong>{html.escape(d["title"])}</strong><span>{html.escape(d["type_line"])}</span></div></div>'
        href = f'projetos/{slug}.html' if d.get("page", True) else None
        tag_open = f'<a class="card" href="{href}">' if href else '<div class="card">'
        tag_close = "</a>" if href else "</div>"
        cards.append(f"""
      {tag_open}
        {media}
        <h3>{html.escape(d['title'])}</h3>
        <p>{html.escape(d['card_line'])}</p>
      {tag_close}""")

    out = head("Raiza Tomazoni — UX/UI e Product Designer",
               "Portfólio de Raiza Tomazoni, designer de produto e UX com formação em Arquitetura e Urbanismo. Projetos para a Secretaria Nacional de Periferias, SUDEMA-PB e outros.",
               "", "cover-nos-perifericos.webp")
    out += f"""
<section class="hero"><div class="wrap">
  <h1 class="hero__name" aria-label="Raiza Tomazoni"><span>Raiza</span><span>Tomazoni</span></h1>
  <div class="cota" aria-hidden="true"><i></i><i></i><b>da arquitetura ao produto digital</b></div>
  <div class="hero__grid">
    <p class="hero__lede">Designer de produto e UX. Desenho serviços públicos e produtos digitais que as pessoas conseguem usar sem precisar pedir ajuda.</p>
    <div>
      <p class="hero__now">Hoje no <strong>Ministério das Cidades</strong>, na Secretaria Nacional de Periferias, e na <strong>SUDEMA-PB</strong>. Formada em Arquitetura e Urbanismo pela UFCG.</p>
      <div class="hero__cta">
        <a class="btn btn--solid" href="#projetos">Ver projetos</a>
        <a class="btn" href="#contato">Falar comigo</a>
      </div>
    </div>
  </div>
</div></section>

<section class="section" id="projetos"><div class="wrap">
  <div class="section__head">
    <h2 class="section__title">Projetos</h2>
    <p class="section__note">Estudos de caso completos, com processo, pesquisa e decisões de design.</p>
  </div>
  {''.join(feats)}
</div></section>

<section class="section"><div class="wrap">
  <div class="section__head">
    <h2 class="section__title">Mais trabalhos</h2>
    <p class="section__note">Sites e interfaces, com foco em UI e identidade visual.</p>
  </div>
  <div class="grid">{''.join(cards)}
  </div>
</div></section>

<section class="section" id="sobre"><div class="wrap about">
  <div class="about__bio">
    <h2 class="section__title" style="margin-bottom:28px">Sobre</h2>
    <p>Sou UX/UI Designer e estudante de Sistemas para Internet no IFPB, com formação em Arquitetura e Urbanismo.</p>
    <p>Da arquitetura trouxe o hábito de começar pelo uso: quem vai passar por ali, com que pressa, com que dúvida. Hoje aplico isso a sistemas de governo e produtos digitais, com pesquisa, prototipação e design systems, e com base de front-end para conversar bem com quem desenvolve.</p>
    <blockquote class="quote">Há um gosto de vitória e encanto na condição de ser simples. Não é preciso muito para ser muito.<cite>Lina Bo Bardi</cite></blockquote>
  </div>
  <div class="timeline">
    <h3>Experiência</h3>
    <ol>
      <li><time>2024 – hoje</time><div><b>UX Designer</b><span>Secretaria Nacional de Periferias, Ministério das Cidades</span></div></li>
      <li><time>2022 – hoje</time><div><b>UX Designer</b><span>SUDEMA, Superintendência de Administração do Meio Ambiente da Paraíba</span></div></li>
      <li><time>2021 – 2022</time><div><b>Arquiteta e Urbanista</b><span>NODA Arquitetura</span></div></li>
      <li><time>2019 – 2022</time><div><b>Arquiteta e Urbanista</b><span>Oficina Espacial</span></div></li>
    </ol>
    <h3>Formação</h3>
    <ol>
      <li><time>2026</time><div><b>Sistemas para Internet</b><span>IFPB, Instituto Federal da Paraíba</span></div></li>
      <li><time>2024</time><div><b>UX/UI/Product Design</b><span>UX Unicórnio</span></div></li>
      <li><time>2019</time><div><b>Arquitetura e Urbanismo</b><span>UFCG, com intercâmbio na Sheffield Hallam University</span></div></li>
    </ol>
    <h3>O que eu faço</h3>
    <ul class="skills">
      <li>Design de produto</li><li>UX Research</li><li>Testes de usabilidade</li><li>Design de interface</li>
      <li>Design systems</li><li>Prototipação</li><li>Identidade visual</li><li>HTML, CSS e JavaScript</li><li>Figma</li>
    </ul>
  </div>
</div></section>

<section class="section contact" id="contato"><div class="wrap">
  <h2 class="section__title" style="margin-bottom:28px">Vamos conversar</h2>
  <div class="contact__row">
    <a class="contact__mail" href="mailto:{EMAIL}">{EMAIL}</a>
    <button class="copy" type="button" data-copy="{EMAIL}">Copiar e-mail</button>
  </div>
  <div class="contact__links">
    <a class="btn" href="{WHATS}" target="_blank" rel="noopener">WhatsApp</a>
    <a class="btn" href="{MEDIUM}" target="_blank" rel="noopener">Medium</a>
  </div>
</div></section>
<script>
document.querySelectorAll('[data-copy]').forEach(function(b){{
  b.addEventListener('click',function(){{
    var t=b.getAttribute('data-copy');
    (navigator.clipboard?navigator.clipboard.writeText(t):Promise.reject()).then(function(){{b.textContent='E-mail copiado';setTimeout(function(){{b.textContent='Copiar e-mail'}},2200)}}).catch(function(){{window.location.href='mailto:'+t}});
  }});
}});
</script>
"""
    out += foot()
    (ROOT / "index.html").write_text(out, encoding="utf-8")


def render_media(m):
    kind = m[0]
    if kind == "img":
        _, src, alt, cap = m
        c = f"<figcaption>{html.escape(cap)}</figcaption>" if cap else ""
        return f'<figure class="figure"><img src="../assets/img/{src}" alt="{html.escape(alt)}" loading="lazy">{c}</figure>'
    if kind == "scroll":
        _, src, alt, cap = m
        return (f'<figure class="figure"><div class="scrollframe" tabindex="0" role="region" aria-label="{html.escape(alt)}, role para ver a página inteira">'
                f'<img src="../assets/img/{src}" alt="{html.escape(alt)}" loading="lazy"></div><figcaption>{html.escape(cap)}</figcaption></figure>')
    if kind == "phones":
        _, items, cap = m
        imgs = "".join(f'<img src="../assets/img/{s}" alt="{html.escape(a)}" loading="lazy">' for s, a in items)
        return f'<figure class="figure"><div class="phones">{imgs}</div><figcaption>{html.escape(cap)}</figcaption></figure>'
    raise ValueError(kind)


def build_case(slug, nxt):
    d = PROJECTS[slug]
    meta = "".join(f"<div><dt>{html.escape(k)}</dt><dd>{v}</dd></div>" for k, v in d["meta"])
    blocks = []
    for b in d["blocks"]:
        body = b["html"]
        media = "".join(render_media(m) for m in b.get("media", []))
        blocks.append(f'<section class="block"><h2>{html.escape(b["title"])}</h2><div class="block__body">{body}</div></section>{media}')
    n = PROJECTS[nxt]
    out = head(f"{d['title']} — Raiza Tomazoni", d["summary"], "../", d.get("cover"))
    cover = (f'<div class="wrap case-cover"><img src="../assets/img/{d["cover"]}" alt="{html.escape(d["cover_alt"])}" width="1600" height="900"></div>'
             if d.get("cover") else "")
    out += f"""
<section class="case-hero"><div class="wrap">
  <a class="back" href="../index.html#projetos">Voltar para projetos</a>
  <h1>{html.escape(d['title'])}</h1>
  <p class="lede">{html.escape(d['lede'])}</p>
  <dl class="meta">{meta}</dl>
</div></section>
{cover}
<div class="wrap">
{''.join(blocks)}
<a class="next" href="{nxt}.html"><span>Próximo projeto</span><strong>{html.escape(n['title'])}</strong></a>
</div>
"""
    out += foot()
    (ROOT / "projetos").mkdir(exist_ok=True)
    (ROOT / "projetos" / f"{slug}.html").write_text(out, encoding="utf-8")


if __name__ == "__main__":
    build_index()
    order = [s for s in FEATURED + MORE if PROJECTS[s].get("page", True)]
    for i, s in enumerate(order):
        build_case(s, order[(i + 1) % len(order)])
    print("ok:", ", ".join(order))
