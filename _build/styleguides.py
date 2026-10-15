"""Guias de estilo montados em HTML a partir dos tokens do Figma."""


def _sw(name, hexv, role, dark_text=False):
    return (f'<div class="sg-sw"><i style="background:{hexv}"></i>'
            f'<b>{name}</b><span>{hexv}</span><small>{role}</small></div>')


STYLE_GUIDE_RANGOUT = f"""
<div class="sg" style="--sg-green:#70AE6E;--sg-orange:#F4743B;--sg-teal:#3C6E71;--sg-title:#2E3E4B;--sg-text:#303030;--sg-border:#D1D1D1;--sg-field:#F2F5FD;--sg-soft:#F5F5F5">

  <section class="sg-sec">
    <h3 class="sg-h">Cores</h3>
    <p class="sg-sub">Primárias</p>
    <div class="sg-swatches">
      {_sw("Verde", "#70AE6E", "Botões principais, ações e estados de sucesso")}
      {_sw("Tangerina", "#F4743B", "Destaques, etiquetas selecionadas e interações")}
      {_sw("Azul", "#3C6E71", "Ações secundárias e links")}
    </div>
    <p class="sg-sub">Marca</p>
    <div class="sg-swatches">
      {_sw("Petróleo", "#016E74", "Logotipo")}
      {_sw("Limão", "#BEED62", "Tela de abertura")}
    </div>
    <p class="sg-sub">Neutras</p>
    <div class="sg-swatches sg-swatches--small">
      {_sw("Títulos", "#2E3E4B", "Títulos de tela")}
      {_sw("Cinza", "#303030", "Textos e labels")}
      {_sw("Borda", "#D1D1D1", "Contornos de campos")}
      {_sw("Branco gelo", "#F2F5FD", "Fundo dos campos")}
      {_sw("Branco gelo 2", "#F5F5F5", "Fundos de apoio")}
      {_sw("Branco", "#FFFFFF", "Fundo das telas")}
    </div>
  </section>

  <section class="sg-sec">
    <h3 class="sg-h">Tipografia</h3>
    <div class="sg-type">
      <div class="sg-type__hero">
        <span class="sg-aa" aria-hidden="true">Aa</span>
        <div><b>Quicksand</b><span>Regular 400, Medium 500, SemiBold 600</span></div>
      </div>
      <dl class="sg-scale">
        <div><dt>H1<small>SemiBold, 30 px</small></dt><dd style="font-size:30px;font-weight:600;color:var(--sg-title)">Temas de Interesse</dd></div>
        <div><dt>Botão<small>Medium, 16 px</small></dt><dd style="font-size:16px;font-weight:500">Próximo</dd></div>
        <div><dt>Etiquetas<small>Regular, 14 px</small></dt><dd style="font-size:14px">Por quais temas você se interessa?</dd></div>
        <div><dt>Labels<small>Regular, 12 px</small></dt><dd style="font-size:12px">Insira seu e-mail ou nome de usuário</dd></div>
      </dl>
    </div>
  </section>

  <section class="sg-sec">
    <h3 class="sg-h">Componentes</h3>
    <div class="sg-comp">

      <div class="sg-card">
        <p class="sg-sub">Botões</p>
        <div class="sg-stack">
          <span class="sg-btn">Próximo</span>
          <span class="sg-btn sg-btn--outline">Recuperar conta</span>
          <div class="sg-row"><span class="sg-btn sg-btn--sm">Trocar endereço</span><span class="sg-btn sg-btn--sm">+ Ver mais</span><span class="sg-follow">+ seguir</span></div>
        </div>
      </div>

      <div class="sg-card">
        <p class="sg-sub">Campos</p>
        <div class="sg-stack">
          <label class="sg-field"><span>E-mail ou nome de usuário</span><i>Insira seu e-mail ou nome de usuário</i></label>
          <label class="sg-field sg-field--select"><span>Perfil</span><i>Selecione</i></label>
          <div class="sg-field sg-field--search"><i>Pesquisar</i><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#303030" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-4-4"/></svg></div>
        </div>
      </div>

      <div class="sg-card">
        <p class="sg-sub">Etiquetas de interesse</p>
        <div class="sg-chips">
          <span class="sg-chip is-on">Veganismo</span><span class="sg-chip">Lactovegetarianismo</span>
          <span class="sg-chip">Ética animal</span><span class="sg-chip is-on">Alergia a glúten</span>
          <span class="sg-chip">Produtos sem glúten</span><span class="sg-chip is-on">APLV</span>
        </div>
      </div>

      <div class="sg-card">
        <p class="sg-sub">Progresso do cadastro e seleção</p>
        <div class="sg-steps" aria-label="Etapa 3 de 5">
          <span class="is-done">1</span><span class="is-done">2</span><span class="is-now">3</span><span>4</span><span>5</span>
        </div>
        <div class="sg-radios"><span class="sg-radio">Sim</span><span class="sg-radio is-on">Não</span></div>
      </div>

      <div class="sg-card sg-card--wide">
        <p class="sg-sub">Publicação e barra de navegação</p>
        <div class="sg-post">
          <img src="../assets/img/rangout-sg-post.webp" alt="Componente de publicação com autor, texto, prévia de link e ações de curtir, comentar, compartilhar e salvar" loading="lazy">
          <img src="../assets/img/rangout-sg-nav.webp" alt="Barra de navegação com ícones de início, buscar, publicar, informações e perfil" loading="lazy">
        </div>
      </div>

    </div>
  </section>
</div>
"""
