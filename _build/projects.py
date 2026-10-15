"""Conteúdo dos projetos. Edite aqui e rode `python3 _build/build.py`."""

FEATURED = ["nos-perifericos", "rangout", "cte"]
MORE = ["sudema-mais", "mapa-das-periferias", "labrua", "supcard"]

PROJECTS = {

# ————————————————————————————————————————————————————————————————
"nos-perifericos": {
    "title": "Nós Periféricos e Busca CEP",
    "client": "Secretaria Nacional de Periferias, Ministério das Cidades",
    "summary": "Plataforma criada do zero para iniciativas das periferias encontrarem editais, cursos e oportunidades do governo federal, e a busca que leva o CEP do programa CEP para Todos a quem mora em favelas e comunidades.",
    "lede": "Uma plataforma federal criada do zero para que iniciativas das periferias encontrem editais, cursos e oportunidades, e uma busca que entrega o CEP oficial de favelas e comunidades a partir do nome do lugar onde a pessoa mora.",
    "tags": ["UX Research", "UX/UI Design", "Governo", "Web e mobile"],
    "cover": "cover-nos-perifericos.webp",
    "cover_alt": "Tela da Busca CEP para TODOS na plataforma Nós Periféricos, com filtros de UF, município e comunidade e tabela de resultados",
    "meta": [
        ("Papel", "UX/UI Designer"),
        ("Cliente", "Secretaria Nacional de Periferias"),
        ("Período", "2024 – hoje"),
        ("No ar", '<a href="https://mapadasperiferias.cidades.gov.br" target="_blank" rel="noopener">mapadasperiferias.cidades.gov.br</a>'),
    ],
    "blocks": [
        {"title": "Contexto", "html": """
<p>A Secretaria Nacional de Periferias (SNP) mantém programas, editais, cursos e ações voltados a favelas e comunidades urbanas de todo o país. Faltava um lugar único onde as iniciativas pudessem encontrar o que se aplica à sua realidade.</p>
<p>O Nós Periféricos nasceu para ser o espaço digital dessas iniciativas: um lugar para se cadastrar, acompanhar oportunidades, participar de cursos e do Mapeamento Popular.</p>
"""},
        {"title": "Meu papel", "html": """
<p>Criei a plataforma do zero, da arquitetura de informação às telas finais, e conduzi pesquisas de usabilidade com pessoas usuárias ao longo do processo. Também desenhei a área de gestão usada pela equipe da SNP e as versões para celular.</p>
"""},
        {"title": "O que desenhei", "html": """
<h3>Uma área para cada iniciativa</h3>
<p>Ao entrar, a pessoa vê as oportunidades abertas, acessa a página da sua iniciativa, os cursos em que está inscrita e o Mapeamento Popular. A navegação lateral mantém essas áreas sempre a um toque.</p>
<h3>Mural de oportunidades</h3>
<p>Editais, cursos e atividades ficam num só mural, com filtros simples e o status de inscrição em destaque em cada cartão (em breve, aberta, encerrada), que é a primeira coisa que a pessoa quer saber.</p>
<h3>Espaços temáticos</h3>
<p>Temas como adaptação climática e geração cidadã de dados ganharam páginas próprias, que explicam como participar em três passos e reúnem projetos e oportunidades daquele tema.</p>
<h3>Área de gestão</h3>
<p>Para a equipe da SNP, uma área separada para gerenciar permissões, publicar oportunidades e acompanhar as iniciativas cadastradas.</p>
""",
         "media": [
            ("img", "np-mural.webp", "Mural de oportunidades com filtros e cartões de editais com o status de inscrição", "Mural de oportunidades: o status de inscrição aparece primeiro em cada cartão."),
            ("img", "np-espacos.webp", "Página de Espaços Temáticos com vídeo, temas e o passo a passo de como participar", "Espaços temáticos explicam como participar antes de pedir qualquer ação."),
            ("phones", [("np-mobile-home.webp", "Início da área do usuário no celular, com oportunidades e atalhos para cursos, editais e publicações")], "No celular, o início prioriza a oportunidade em aberto e o que falta no cadastro."),
         ]},
        {"title": "Busca CEP para Todos", "html": """
<p>O CEP para Todos é uma iniciativa da SNP com os Correios que leva endereço postal formal a favelas e comunidades urbanas do Brasil. Ter CEP muda coisas básicas: receber correspondência, comprovar residência, fazer compras on-line.</p>
<p>O desafio era que as pessoas não sabem o CEP novo, mas sabem o nome da comunidade onde moram. Por isso desenhei uma busca que começa pelo que a pessoa já conhece:</p>
<ul>
  <li>Filtro por estado e município, e depois pelo nome ou parte do nome da comunidade.</li>
  <li>Os nomes seguem os registros oficiais do IBGE para Favelas e Comunidades Urbanas, e um aviso no topo explica isso para evitar buscas frustradas.</li>
  <li>O CEP fica numa coluna destacada, com botão para copiar, porque o próximo passo da pessoa quase sempre é colar o CEP em outro lugar.</li>
  <li>Quando não há resultado, a tela indica o WhatsApp da equipe em vez de terminar num beco sem saída.</li>
</ul>
""",
         "media": [
            ("img", "np-cep.webp", "Resultado da Busca CEP para TODOS: três comunidades de João Pessoa com seus CEPs e botão de copiar", "A coluna do CEP é destacada e tem atalho para copiar."),
         ]},
    ],
},

# ————————————————————————————————————————————————————————————————
"rangout": {
    "title": "Rangout",
    "client": "Startup social, trabalho voluntário",
    "summary": "Rede social para pessoas com restrições alimentares trocarem informação confiável, experiências e indicações de lugares seguros para comer. Da pesquisa ao protótipo de alta fidelidade e à identidade visual.",
    "lede": "Uma rede social para pessoas com restrições alimentares encontrarem informação confiável, lugares seguros para comer e outras pessoas que passam pelo mesmo.",
    "tags": ["UX Research", "UX/UI Design", "Branding", "App"],
    "cover": "cover-rangout.webp",
    "cover_alt": "Três telas do app Rangout: feed, publicação com comentários e mensagens",
    "meta": [
        ("Papel", "UX/UI Designer e design gráfico"),
        ("Equipe", "Gabriela Cavalcante, fundadora e CEO"),
        ("Ano", "2024"),
        ("Plataforma", "App mobile"),
    ],
    "blocks": [
        {"title": "O problema", "html": """
<p>Pessoas com restrições alimentares, seja por saúde, ética, motivos sociais ou religiosos, enfrentam o mesmo conjunto de dificuldades: informação pouco confiável sobre o que é seguro comer, poucos restaurantes e mercados com opções adequadas, dificuldade de achar profissionais com experiência no assunto e, muitas vezes, isolamento.</p>
<p>A pergunta que guiou o projeto foi: como garantir acesso a informação confiável e ampliar o conhecimento sobre restrições alimentares?</p>
"""},
        {"title": "Pesquisa", "html": """
<p>Comecei organizando o que o time já sabia com o Business Model Canvas, o Canvas de Proposta de Valor e uma Matriz CSD de certezas, suposições e dúvidas. As dúvidas viraram perguntas de uma pesquisa quantitativa com pessoas diagnosticadas.</p>
<div class="stats">
  <div class="stat"><b>78%</b><span>buscaram informação sobre dieta e alimentação nos últimos 12 meses</span></div>
  <div class="stat"><b>76%</b><span>considerariam entrar numa comunidade on-line sobre o tema</span></div>
  <div class="stat"><b>50%</b><span>estariam dispostos a compartilhar experiências e dicas</span></div>
  <div class="stat"><b>58%</b><span>conhecem restaurantes com opções adequadas</span></div>
  <div class="stat"><b>26%</b><span>acham fácil encontrar profissionais especializados</span></div>
  <div class="stat"><b>12%</b><span>conhecem alguma plataforma ou comunidade de apoio</span></div>
</div>
<p>As maiores frustrações foram a falta de opções e a dificuldade de encontrar lugares adequados para comer fora. Quase sempre, a raiz era falta de informação.</p>
<p>Um dado orientou várias decisões: o interesse em participar de uma comunidade (76%) era bem maior que a disposição de compartilhar (50%). A rede precisava ser útil para quem só quer ler, e tornar fácil a participação de quem quer contribuir.</p>
"""},
        {"title": "Quem usa", "html": """
<p>O público vai de 14 a 65 anos, com a maioria entre 18 e 54. O perfil típico é um adulto jovem que descobriu há pouco uma restrição, como intolerância ao glúten ou à lactose, e procura informação e apoio.</p>
<p>Duas personas guiaram o projeto: Eduarda, mestranda com alergia ao glúten que não consegue achar comida e restaurantes seguros, e Marcos, pai de uma criança com múltiplas alergias que lida com lancheira escolar e desinformação na escola.</p>
"""},
        {"title": "Ideação e teste", "html": """
<p>Transformei os achados em perguntas “Como poderíamos” e priorizei as ideias numa matriz de impacto e esforço, para começar pelo que entregava mais valor com menos custo. Crazy 8's e rabiscoframes viraram wireframes e um fluxo de navegação.</p>
<p>Testei um protótipo de baixa fidelidade no Marvel com duas tarefas: ver as informações de um restaurante e criar uma publicação. O principal achado foi que a tela Explorar confundia, porque não tinha títulos de seção. Esse achado orientou a revisão da tela na versão em alta fidelidade.</p>
"""},
        {"title": "Solução", "html": """
<p>Um cadastro em etapas monta o perfil alimentar da pessoa, com histórico de saúde e outras dietas, e personaliza o que ela vê. Depois disso, o app reúne feed com publicações e indicações, mensagens diretas, conteúdo informativo e sugestões de lugares próximos.</p>
<h3>Identidade visual</h3>
<p>Criei o logo e uma paleta inspirada na natureza, para remeter a alimentação natural e saudável. A tipografia é a Quicksand, escolhida pela geometria simples, boa leitura e tom amigável.</p>
""",
         "media": [
            ("phones", [
                ("rangout-splash.webp", "Tela de abertura com o logo do Rangout em fundo verde-limão"),
                ("rangout-saude.webp", "Cadastro em etapas: histórico de saúde"),
                ("rangout-feed.webp", "Feed com abas Para você, Trending e Seguindo"),
                ("rangout-post.webp", "Publicação com curtidas, comentários e respostas"),
                ("rangout-opcoes.webp", "Menu de opções da publicação, com controle do que aparece no feed"),
                ("rangout-mensagens.webp", "Lista de mensagens diretas"),
            ], "Da abertura ao feed: cadastro em etapas, publicações, controle do feed e mensagens."),
         ]},
        {"title": "Aprendizados", "html": """
<p>As personas e os dados da pesquisa foram o que destravou as discussões quando o time tinha dúvidas. A diferença entre querer participar e querer compartilhar me ensinou a desenhar para quem só observa, sem tratar essa pessoa como usuária de segunda classe.</p>
<p>O produto segue em desenvolvimento, com novas rodadas de teste de usabilidade previstas.</p>
<p><a href="https://medium.com/@raizaft/rangout-conectando-pessoas-com-restri%C3%A7%C3%B5es-alimentares-a33272f07f71" target="_blank" rel="noopener">Ler o estudo completo no Medium</a></p>
"""},
    ],
},

# ————————————————————————————————————————————————————————————————
"cte": {
    "title": "Cadastro Técnico Estadual",
    "client": "SUDEMA, Governo da Paraíba",
    "summary": "Sistema para empreendedores, consultores e técnicos da SUDEMA registrarem e acompanharem atividades licenciadas, com fluxos pensados para três perfis muito diferentes.",
    "lede": "Um sistema do governo da Paraíba onde empreendedores registram suas atividades potencialmente poluidoras, vinculam consultores ambientais e emitem o certificado de regularidade, e onde técnicos da SUDEMA acompanham tudo.",
    "tags": ["UX/UI Design", "Governo", "Sistema web", "Responsivo"],
    "cover": "cover-cte.webp",
    "cover_alt": "Página inicial do Cadastro Técnico Estadual sobre uma foto da caatinga paraibana",
    "meta": [
        ("Papel", "UX/UI Designer"),
        ("Cliente", "SUDEMA-PB"),
        ("Ano", "2024 – 2025"),
        ("No ar", '<a href="https://cte.sigma.pb.gov.br" target="_blank" rel="noopener">cte.sigma.pb.gov.br</a>'),
    ],
    "blocks": [
        {"title": "O problema", "html": """
<p>Quem exerce atividade potencialmente poluidora na Paraíba precisa estar inscrito no Cadastro Técnico Estadual. Na prática, empreendedores tinham dificuldade para registrar suas atividades e para gerenciar os consultores ambientais vinculados à sua conta, e a SUDEMA precisava de mais controle sobre os dados e as ações de cada perfil.</p>
"""},
        {"title": "Três perfis, três jornadas", "html": """
<p>O sistema atende pessoas com objetivos e familiaridade com tecnologia muito diferentes. Escrevi personas e histórias de usuário para cada uma:</p>
<ul>
  <li><b>Empreendedora</b>: registra atividades para obter o certificado de regularidade, aceita ou recusa pedidos de vínculo de consultores e acompanha o histórico da conta, inclusive o que o consultor fez em seu nome.</li>
  <li><b>Consultor</b>: pede vínculo com empreendedores, cadastra atividades por eles e gera certificados.</li>
  <li><b>Técnico da SUDEMA</b>: gerencia contas, vínculos e permissões, e audita o histórico de qualquer empreendedor.</li>
</ul>
"""},
        {"title": "Decisões de design", "html": """
<h3>Confiança no vínculo</h3>
<p>Antes de aceitar um consultor, a empreendedora vê os documentos dele. Ninguém age em nome de outra pessoa sem consentimento explícito.</p>
<h3>Histórico auditável</h3>
<p>Toda ação fica registrada: o que foi feito, quando e por quem. Se um técnico exclui uma atividade, a justificativa fica visível para quem consultar o histórico.</p>
<h3>Formulários que explicam</h3>
<p>Campos com descrição, exemplos e validação em tempo real. Quando uma ação depende de outro sistema, como o PBdoc, a tela diz isso e leva até lá, em vez de deixar a pessoa procurar.</p>
<h3>Um padrão para tudo</h3>
<p>Navegação hierárquica com menu lateral fixo, botões e links com comportamento consistente, cores e ícones para status e retorno imediato a cada ação. A mesma estrutura funciona no computador, no tablet e no celular.</p>
""",
         "media": [
            ("img", "cte-inicio.webp", "Página inicial com explicação do que é o CTE, quem precisa se cadastrar e botões para acessar, criar conta e consultar", "O início explica o que é o cadastro e quem precisa dele antes de pedir login."),
            ("img", "cte-atividades.webp", "Lista de atividades do empreendedor com filtros por licença, atividade e status", "Atividades com filtros e um aviso que evita cadastros antes da licença."),
            ("img", "cte-acoes.webp", "Modal Outras ações listando solicitações que devem ser feitas pelo PBdoc", "Quando a ação é em outro sistema, a tela diz qual e leva até ele."),
            ("img", "cte-justificativa.webp", "Modal de justificativa no histórico, mostrando qual técnico excluiu a atividade e por quê", "Histórico auditável: quem fez, quando e por quê."),
            ("phones", [("cte-mobile.webp", "Lista de atividades no celular com status por cor")], "Versão para celular com a mesma estrutura."),
         ]},
        {"title": "Fluxos principais", "html": """
<ul>
  <li><b>Cadastrar atividade</b>: entrar, escolher nova atividade, informar o número da licença, revisar e confirmar.</li>
  <li><b>Emitir certificado</b>: abrir os detalhes da atividade, conferir as informações e gerar o certificado para impressão.</li>
  <li><b>Vincular consultor</b>: o consultor envia o pedido, a empreendedora analisa os documentos e aceita ou recusa.</li>
</ul>
<p><a href="https://medium.com/@raizaft/cadastro-t%C3%A9cnico-estadual-cte-sudema-pb-e11445055f71" target="_blank" rel="noopener">Ler a documentação completa no Medium</a></p>
"""},
    ],
},

# ————————————————————————————————————————————————————————————————
"sudema-mais": {
    "title": "Sudema+",
    "client": "SUDEMA, Governo da Paraíba",
    "card_line": "App que reúne notícias, balneabilidade das praias e o acompanhamento de processos de licenciamento ambiental da SUDEMA.",
    "summary": "App mobile que reúne notícias, consulta de balneabilidade e acompanhamento de processos de licenciamento ambiental da SUDEMA.",
    "lede": "Um app que junta num só lugar o que a população e os empreendedores mais procuram na SUDEMA: notícias, se a praia está própria para banho e em que pé está um processo de licenciamento.",
    "tags": ["UX/UI Design", "App", "Governo"],
    "cover": "cover-sudema.webp",
    "cover_alt": "Três telas do app Sudema+: início, mapa de balneabilidade e área de consulta SIGMA",
    "meta": [
        ("Papel", "UX/UI Designer"),
        ("Cliente", "SUDEMA-PB"),
        ("Plataforma", "App mobile"),
        ("Foco", "Organização da informação"),
    ],
    "blocks": [
        {"title": "Contexto", "html": """
<p>A SUDEMA atende dois públicos com necessidades bem diferentes: a população, que quer saber se uma praia está própria para banho ou fazer uma denúncia ambiental, e os empreendedores, que acompanham processos de licenciamento no SIGMA. O app centraliza esses serviços num só lugar.</p>
"""},
        {"title": "O que desenhei", "html": """
<p>Um app com quatro áreas fixas na barra inferior: início, notícias, balneabilidade e SIGMA. A prioridade foi organizar a informação com clareza e dar acesso rápido aos serviços principais.</p>
<h3>Balneabilidade no mapa</h3>
<p>Os trechos monitorados aparecem no mapa com ícones de próprio e impróprio para banho, com filtro por município e trecho e a opção de mostrar só os impróprios. Um toque no ícone mostra o local, a estação de coleta e o resultado.</p>
<h3>Processos no bolso</h3>
<p>A área SIGMA resume solicitações e processos em análise, destaca notificações não respondidas e lista as últimas movimentações. O detalhe de cada processo traz dados, licença para baixar e despachos. Um aviso deixa claro que o app é para consulta e indica o site para novas solicitações.</p>
<h3>Denúncias com contexto</h3>
<p>Antes do botão de denunciar, a tela explica por que denunciar, o que acontece depois e o que conta como infração ambiental.</p>
""",
         "media": [
            ("phones", [
                ("sudema-home.webp", "Início com destaques, serviços e últimas notícias"),
                ("sudema-balneabilidade.webp", "Mapa de balneabilidade com detalhe de um trecho próprio para banho"),
                ("sudema-denuncias.webp", "Tela de denúncias com explicações antes do botão"),
                ("sudema-menu.webp", "Menu lateral com notícias, balneabilidade, contato e SIGMA"),
                ("sudema-sigma.webp", "Área SIGMA com solicitações, processos e últimas movimentações"),
                ("sudema-processo.webp", "Detalhes de um processo com licença para baixar e despachos"),
            ], "Início, balneabilidade, denúncias, menu e a área de consulta de processos."),
         ]},
    ],
},

# ————————————————————————————————————————————————————————————————
"mapa-das-periferias": {
    "title": "Mapa das Periferias",
    "client": "Secretaria Nacional de Periferias, Ministério das Cidades",
    "card_line": "Homepage do portal que reúne investimentos federais, ações e iniciativas nas periferias do Brasil.",
    "summary": "Homepage do portal que reúne dados sobre as periferias urbanas do Brasil, com foco em clareza visual, navegação e estrutura modular.",
    "lede": "A porta de entrada de um portal que reúne investimentos federais, ações da Secretaria e iniciativas das próprias periferias brasileiras.",
    "tags": ["UI Design", "Governo", "Site"],
    "cover": "cover-mapa.webp",
    "cover_alt": "Homepage do Mapa das Periferias com banner do programa Periferia Sem Risco",
    "meta": [
        ("Papel", "UI Designer"),
        ("Cliente", "Secretaria Nacional de Periferias"),
        ("Ano", "2025"),
        ("No ar", '<a href="https://mapadasperiferias.cidades.gov.br" target="_blank" rel="noopener">mapadasperiferias.cidades.gov.br</a>'),
    ],
    "blocks": [
        {"title": "Contexto", "html": """
<p>O Mapa das Periferias reúne dados sobre as áreas periféricas do país: investimentos e obras do Governo Federal, ações feitas pelos próprios territórios, iniciativas reconhecidas pelo Prêmio Periferia Viva e informações coletadas pelo Mapeamento Popular. O portal soma mais de 3 mil iniciativas periféricas cadastradas.</p>
<p>Com tanto conteúdo, a homepage precisava ajudar cada pessoa a achar o seu caminho sem se perder.</p>
"""},
        {"title": "Decisões", "html": """
<ul>
  <li><b>Estrutura modular</b>: blocos independentes para programas, notícias, ações e publicações, cada um com uma função clara.</li>
  <li><b>Contraste e hierarquia</b>: fundo preto no topo e no bloco de ações, tipografia forte nos títulos e uma faixa de cores da identidade do programa como separador.</li>
  <li><b>Navegação direta</b>: a busca e o mapa interativo ficam fixos no topo, sempre à mão.</li>
  <li><b>Dados em linguagem simples</b>: números como os mais de R$ 8 bilhões investidos aparecem com uma frase que explica o que significam.</li>
</ul>
""",
         "media": [
            ("img", "mapa-home.webp", "Topo da homepage com busca, mapa interativo e banner de programa", ""),
            ("scroll", "mapa-periferia-viva.webp", "Homepage completa do Mapa das Periferias", "Role dentro do quadro para ver a página inteira."),
         ]},
    ],
},

# ————————————————————————————————————————————————————————————————
"labrua": {
    "title": "Site do LabRua",
    "client": "Laboratório de Rua",
    "card_line": "Site para uma associação de planejamento urbano, com a paleta vibrante da identidade da marca.",
    "summary": "Site institucional para o Laboratório de Rua, associação de planejamento urbano, usando a paleta vibrante da identidade para reforçar a personalidade da marca.",
    "lede": "Site institucional para uma associação sem fins lucrativos dedicada ao planejamento urbano e regional, ao desenho urbano e à pesquisa, com mais de dez anos de atuação em cidades brasileiras.",
    "tags": ["UI Design", "Site", "Responsivo"],
    "cover": "cover-labrua.webp",
    "cover_alt": "Topo do site do LabRua com a frase A rua como laboratório sobre fundo amarelo",
    "meta": [
        ("Papel", "UI Designer"),
        ("Desenvolvimento", "Joan Vitor"),
        ("Ano", "2025"),
        ("Páginas", "Início, Nós, Serviços, Portfólio"),
    ],
    "blocks": [
        {"title": "Contexto", "html": """
<p>O LabRua trabalha com planejamento urbano, desenho urbano e regularização fundiária (REURB). O site precisava apresentar uma lista grande de serviços técnicos para prefeituras e comunidades sem perder a energia da marca.</p>
<p>Esse é um projeto próximo da minha formação em Arquitetura e Urbanismo, o que ajudou a organizar os serviços pela forma como os clientes pensam neles.</p>
"""},
        {"title": "Decisões", "html": """
<ul>
  <li><b>A paleta como estrutura</b>: amarelo, azul, rosa e roxo da identidade marcam cada seção, o que deixa claro onde uma termina e a outra começa.</li>
  <li><b>Três eixos de atuação</b>: os serviços foram agrupados em Planejamento Urbano e Regional, Desenho Urbano e REURB, cada um com foto e descrição curta.</li>
  <li><b>Fotos reais das cidades</b>: vistas aéreas e trabalho de campo mostram o que o laboratório faz, sem precisar de ilustração.</li>
  <li><b>Contato visível</b>: formulário e canais de contato aparecem junto ao bloco de diferenciais, antes do rodapé.</li>
</ul>
""",
         "media": [
            ("scroll", "labrua-home.webp", "Página inicial completa do site do LabRua", "Página inicial completa. Role dentro do quadro para ver tudo."),
            ("img", "labrua-servicos.webp", "Página de eixos de atuação, alternando azul e roxo com vídeo e descrição", "Página de serviços: cada eixo com vídeo e texto, alternando cores."),
            ("phones", [("labrua-mobile.webp", "Início do site do LabRua no celular")], "Versão para celular."),
         ]},
    ],
},

# ————————————————————————————————————————————————————————————————
"supcard": {
    "title": "Site da SUPCard",
    "client": "SUPCard",
    "card_line": "Site institucional para uma empresa de cartões de crédito de marca própria para o varejo.",
    "summary": "Site institucional para uma empresa que ajuda varejistas a emitir e gerir cartões de crédito com a própria marca.",
    "lede": "Site institucional para uma empresa que ajuda varejistas de pequeno, médio e grande porte a emitir e gerir cartões de crédito com a própria marca.",
    "tags": ["UI Design", "Site", "Responsivo"],
    "cover": "cover-supcard.webp",
    "cover_alt": "Topo do site da SUPCard com a chamada Cartões de crédito de marca própria para o varejo brasileiro",
    "meta": [
        ("Papel", "UI Designer"),
        ("Cliente", "SUPCard"),
        ("Plataforma", "Site responsivo"),
        ("Páginas", "Início, Sobre, Serviços, Suporte, Revenda"),
    ],
    "blocks": [
        {"title": "Contexto", "html": """
<p>A SUPCard oferece a estrutura para lojas terem seu próprio cartão de crédito, além de cashback, programa de pontos e gestão pelo app. O site precisava falar com donos de lojas, explicar produtos parecidos entre si e levar ao contato comercial.</p>
"""},
        {"title": "Decisões", "html": """
<ul>
  <li><b>Proposta clara no topo</b>: o que a empresa faz e para quem, com um único botão de ação, em banners que mostram o benefício para o lojista.</li>
  <li><b>Produtos lado a lado</b>: cartões private label, convênio e recarga aparecem como opções comparáveis já na primeira dobra.</li>
  <li><b>Prova social</b>: depoimentos e cartões de clientes reais, com a região onde atuam.</li>
  <li><b>Contato curto</b>: um formulário com só e-mail e telefone, e WhatsApp como alternativa.</li>
</ul>
""",
         "media": [
            ("img", "supcard-banners.webp", "Dois banners da SUPCard: Acabe com o fiado desorganizado e A potência de um cartão com a sua identidade", "Banners de topo com mensagens para o lojista."),
            ("scroll", "supcard-home.webp", "Página inicial completa da SUPCard", "Página inicial completa. Role dentro do quadro para ver tudo."),
            ("img", "supcard-servicos.webp", "Página de serviços com cartões para cada produto", "Página de serviços."),
            ("phones", [("supcard-mobile.webp", "Início do site no celular")], "Versão para celular."),
         ]},
    ],
},
}
