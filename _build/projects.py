"""Conteúdo dos projetos. Edite aqui e rode `python3 _build/build.py`."""

from styleguides import STYLE_GUIDE_RANGOUT

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
    "lede": "Uso do Design de Experiência do Usuário para identificar as necessidades de pessoas com restrições alimentares e criar uma rede social para compartilhar informações seguras e trocar experiências.",
    "tags": ["UX Research", "UX/UI Design", "Branding", "App"],
    "cover": "cover-rangout.webp",
    "cover_alt": "Três celulares com as telas de login, abertura e feed do Rangout, ao lado do logotipo",
    "case_cover": "rangout-mockup.webp",
    "case_cover_alt": "Três celulares com as telas de login, abertura e feed do Rangout, ao lado do logotipo",
    "meta": [
        ("Papel", "UX Designer e designer gráfica"),
        ("Equipe", '<a href="https://www.linkedin.com/in/gabrielacvcnt" target="_blank" rel="noopener">Gabriela Cavalcante</a>, fundadora e CEO'),
        ("Ano", "2024"),
        ("Plataforma", "App mobile"),
    ],
    "blocks": [
        {"title": "Cenário atual", "html": """
<p>Atualmente, pessoas com restrições alimentares enfrentam diversos desafios no dia a dia. Desde encontrar informações confiáveis sobre alimentos seguros até lidar com o aspecto emocional e social das suas condições, essas pessoas muitas vezes se veem isoladas e desamparadas. A falta de acesso a uma comunidade de apoio e a recursos relevantes dificulta ainda mais a gestão das suas dietas.</p>
<p>Além disso, há uma considerável dificuldade em encontrar restaurantes ou mercados que ofereçam opções adequadas às suas restrições, o que muitas vezes limita suas escolhas e experiências gastronômicas. A busca por profissionais experientes, como médicos, nutricionistas e chefs especializados, também é desafiadora, o que torna ainda mais difícil conseguir orientação e suporte.</p>
<blockquote>Como podemos garantir o acesso a informações confiáveis e ampliar o conhecimento sobre restrições alimentares para atender às necessidades das pessoas que convivem com essas condições?</blockquote>
"""},
        {"title": "Introdução e objetivos", "html": """
<p>A proposta do Rangout é desenvolver uma rede social voltada para pessoas que enfrentam restrições alimentares. O projeto visa criar um ambiente seguro e informativo, com uma plataforma interativa que conecta pessoas que lidam com restrições de diversas naturezas. Seja por questões de saúde, escolhas éticas, sociais ou práticas religiosas, o objetivo é estabelecer um espaço que promova o compartilhamento de experiências, informações e apoio entre os usuários.</p>
<h3>Objetivos</h3>
<ul>
  <li>Desenvolver uma plataforma amigável e de fácil acesso que permita aos usuários compartilhar suas experiências, oferecer dicas e encontrar apoio relacionado às suas restrições alimentares.</li>
  <li>Incorporar recursos interativos, como fóruns e mensagens diretas, para facilitar a comunicação entre os membros da comunidade e promover um ambiente colaborativo e solidário.</li>
  <li>Criar um espaço acolhedor e educativo onde os usuários possam aprender e compartilhar conhecimentos sobre restrições alimentares, aumentando a conscientização e promovendo um estilo de vida mais saudável.</li>
</ul>
"""},
        {"title": "Modelo de negócio", "html": """
<p>Para compreender e estruturar melhor o negócio, focamos no público-alvo. Para isso, usamos o Business Model Canvas.</p>
<p>Em seguida, detalhamos as propostas de valor com o Value Proposition Canvas, uma ferramenta estratégica que ajuda a alinhar o produto às necessidades e desejos dos clientes.</p>
""",
         "media": [
            ("img", "rangout-bmc.webp", "Business Model Canvas do Rangout com parcerias, atividades, recursos, proposta de valor, relacionamento, canais, segmentos, custos e receitas", "Business Model Canvas."),
            ("img", "rangout-vpc.webp", "Value Proposition Canvas relacionando a proposta de valor do Rangout ao perfil do cliente", "Value Proposition Canvas."),
         ]},
        {"title": "Usuários", "html": """
<p>Com base nos dados coletados na pesquisa, identificamos que os possíveis usuários do Rangout são pessoas de todos os gêneros, com idades entre 14 e 65 anos, que lidam com restrições alimentares diversas. A maioria dos entrevistados está na faixa entre 18 e 54 anos.</p>
<h3>Perfil e contexto</h3>
<p>O usuário típico é uma pessoa jovem, entre 18 e 44 anos, que descobriu recentemente uma restrição alimentar, como alergia ao glúten ou intolerância à lactose. Ela busca informações confiáveis e apoio para lidar com a condição de forma eficaz e, por isso, está aberta a novas tecnologias e comunidades on-line que ofereçam suporte e orientação.</p>
"""},
        {"title": "Persona: Eduarda", "html": """
<p>Estudante de mestrado de 25 anos que começou a perceber sintomas desconfortáveis depois de consumir alimentos com glúten. Seus desafios são a adaptação à nova dieta, o isolamento social e a falta de suporte especializado.</p>
<h3>Storytelling</h3>
<ol class="story">
  <li><b>Era uma vez</b><span>Eduarda, estudante de mestrado diagnosticada com alergia ao glúten.</span></li>
  <li><b>Todo dia</b><span>ela precisa comprar comida ou criar receitas que não causem nenhum problema de saúde.</span></li>
  <li><b>Um dia</b><span>ela não conseguiu cozinhar nem encontrar um restaurante que oferecesse comida para pessoas com restrições alimentares.</span></li>
  <li><b>Por causa disso</b><span>ela procurou ajuda na internet.</span></li>
  <li><b>Por causa disso</b><span>ela encontrou a indicação de uma rede social voltada para pessoas como ela.</span></li>
  <li><b>Até que finalmente</b><span>encontrou indicações de restaurantes próximos de casa logo depois de preencher seu perfil no aplicativo, e conseguiu almoçar.</span></li>
</ol>
""",
         "media": [
            ("img", "rangout-persona-eduarda.webp", "Persona Eduarda Siqueira, estudante de mestrado, com descrição, desafios e objetivos", "Persona Eduarda Siqueira."),
            ("img", "rangout-jornada-eduarda.webp", "Jornada da Eduarda em três fases: descobre a restrição, busca por suporte e empoderamento, com ações, pensamentos, emoções e oportunidades", "Jornada da Eduarda: da descoberta da restrição ao empoderamento."),
         ]},
        {"title": "Persona: Marcos", "html": """
<p>Analista de sistemas de 35 anos, pai de um menino de 6 anos diagnosticado há poucos meses com alergia a vários alimentos, entre eles glúten, laticínios e amendoim. Desde então, enfrenta desafios para garantir que o filho tenha uma dieta segura e adequada.</p>
<h3>Storytelling</h3>
<ol class="story">
  <li><b>Era uma vez</b><span>Marcos, pai de uma criança com alergia a vários alimentos.</span></li>
  <li><b>Todo dia</b><span>ele precisa preparar a lancheira do filho e lidar com a desinformação de professores e outros profissionais da escola.</span></li>
  <li><b>Um dia</b><span>o filho passou mal por comer algo que um colega ofereceu.</span></li>
  <li><b>Por causa disso</b><span>ele desabafou com um amigo, sem saber como conduzir a situação com a direção e os professores.</span></li>
  <li><b>Por causa disso</b><span>o amigo indicou uma rede social de que tinha ouvido falar, feita para pessoas na mesma situação.</span></li>
  <li><b>Até que finalmente</b><span>ele encontrou uma comunidade de outros pais que passaram pelo mesmo problema e puderam dar dicas sobre como lidar.</span></li>
</ol>
""",
         "media": [
            ("img", "rangout-persona-marcos.webp", "Persona Marcos Cipriano, analista de sistemas, com descrição, desafios e objetivos", "Persona Marcos Cipriano."),
            ("img", "rangout-jornada-marcos.webp", "Jornada do Marcos em três fases: descobre a restrição, busca por suporte e compreensão", "Jornada do Marcos: da descoberta da restrição à compreensão."),
         ]},
        {"title": "Matriz CSD", "html": """
<p>Na primeira etapa de validação, usamos a Matriz CSD para separar nossas certezas, suposições e dúvidas. Foi ela que deu origem às perguntas da pesquisa quantitativa.</p>
""",
         "media": [
            ("img", "rangout-csd.webp", "Matriz CSD com certezas, suposições e dúvidas sobre pessoas com restrições alimentares", "Matriz CSD."),
         ]},
        {"title": "Pesquisa quantitativa", "html": """
<p>Com base na Matriz CSD, formulamos o questionário da pesquisa e extraímos alguns dados importantes para o desenvolvimento do aplicativo.</p>
<div class="stats">
  <div class="stat"><b>78%</b><span>das pessoas com restrições diagnosticadas procuraram informações sobre dietas e alimentação saudável nos últimos 12 meses</span></div>
  <div class="stat"><b>100%</b><span>acreditam que a tecnologia pode ajudar pessoas com restrições alimentares a se conectarem melhor</span></div>
  <div class="stat"><b>76%</b><span>considerariam participar de uma comunidade on-line dedicada a pessoas com restrições alimentares</span></div>
  <div class="stat"><b>50%</b><span>estariam dispostas a compartilhar suas experiências e dicas com outras pessoas</span></div>
  <div class="stat"><b>58%</b><span>conhecem restaurantes que oferecem opções para pessoas com restrições alimentares</span></div>
  <div class="stat"><b>26%</b><span>acham fácil encontrar profissionais especializados que entendam suas restrições</span></div>
  <div class="stat"><b>12%</b><span>conhecem plataformas de suporte e comunidades on-line para pessoas com restrições alimentares</span></div>
</div>
<p>As duas maiores frustrações em relação à disponibilidade de alimentos seguros e às opções de refeição fora de casa são as limitações de escolha e a dificuldade de encontrar locais adequados.</p>
<p><a href="https://forms.gle/6nq54NkQm34dTUeQ9" target="_blank" rel="noopener">Ver o formulário da pesquisa quantitativa</a></p>
<h3>Aprendizados</h3>
<ul>
  <li>A maioria das pessoas com restrições alimentares busca informações seguras.</li>
  <li>Embora todas achem que a tecnologia pode ajudá-las e 76% digam que fariam parte de uma comunidade on-line, apenas 50% aceitariam compartilhar experiências.</li>
  <li>Embora a maioria conheça restaurantes que oferecem esse tipo de alimentação, apenas 12% conhecem plataformas on-line para esse público.</li>
  <li>As maiores frustrações com a disponibilidade de alimentos seguros e de opções para comer fora são causadas pela falta de informação.</li>
</ul>
"""},
        {"title": "Alternativas de solução", "html": """
<p>Nessa etapa, usamos a metodologia “How Might We” (Como poderíamos) para identificar oportunidades de inovação e responder a desafios específicos de pessoas com restrições alimentares. A abordagem transforma problemas em perguntas abertas e incentiva a equipe a explorar diferentes perspectivas e gerar ideias criativas.</p>
<p>A partir dessas perguntas, montamos uma Matriz de Impacto x Esforço para identificar as soluções com maior impacto e menor esforço e selecionar as mais adequadas para a primeira implementação. Ficaram em destaque conectar pessoas a uma comunidade de apoio, incentivar o compartilhamento de experiências, criar um sistema de recomendações personalizado, usar geolocalização para encontrar opções seguras por perto e reunir avaliações de restaurantes e produtos.</p>
""",
         "media": [
            ("img", "rangout-impacto-esforco.webp", "Matriz de Impacto x Esforço com perguntas Como podemos, destacando as de alto impacto e baixo esforço", "Matriz de Impacto x Esforço. Em destaque, as soluções escolhidas para a primeira versão."),
         ]},
        {"title": "Desenhos iniciais", "html": """
<p>Usamos as técnicas Crazy 8's e rabiscoframes para entender melhor como a solução funcionaria no aplicativo e preparar o primeiro teste de usabilidade.</p>
""",
         "media": [
            ("img", "rangout-crazy8.webp", "Esboços à mão das telas Explorar, página do restaurante com avaliações e menu Publicar", "Crazy 8's."),
            ("img", "rangout-rabiscoframes.webp", "Folhas com rabiscoframes de login, feed, explorar, mensagens, cadastro, perfil e histórico de saúde", "Rabiscoframes."),
         ]},
        {"title": "Guia de estilo", "html": """
<p>Para manter as telas consistentes, organizei os estilos e componentes do protótipo num guia: cores, tipografia e os componentes mais usados no app.</p>
<p>A paleta parte da natureza, para remeter a uma alimentação saudável e natural. A tipografia é a Quicksand, de geometria simples e curvas suaves, que deixa o app legível e amigável.</p>
""",
         "media": [("html", STYLE_GUIDE_RANGOUT)]},
        {"title": "Protótipo de alta fidelidade", "html": """
<p>No protótipo final, o cadastro em etapas monta o perfil da pessoa, com histórico de saúde, outras dietas e temas de interesse, e personaliza o que ela vê. O app reúne feed com publicações e indicações, explorar com pessoas, restaurantes próximos e notícias, mensagens diretas e criação de publicações, recomendações, receitas e artigos.</p>
<p>A tela Explorar ganhou títulos para cada seção, corrigindo o ponto de confusão encontrado no teste de usabilidade com o protótipo de baixa fidelidade.</p>
""",
         "media": [
            ("img", "rangout-telas.webp", "Dezoito telas do protótipo de alta fidelidade do Rangout, do login ao feed, explorar, perfil e mensagens", "Telas do protótipo de alta fidelidade."),
            ("phones", [
                ("rangout-saude.webp", "Cadastro em etapas: histórico de saúde"),
                ("rangout-feed.webp", "Feed com abas Para você, Trending e Seguindo"),
                ("rangout-post.webp", "Publicação com curtidas, comentários e respostas"),
                ("rangout-opcoes.webp", "Menu de opções da publicação, com controle do que aparece no feed"),
                ("rangout-mensagens.webp", "Lista de mensagens diretas"),
            ], "Algumas telas em detalhe. Arraste para o lado para ver todas."),
         ]},
        {"title": "Aprendizados e próximos passos", "html": """
<p>Estamos muito felizes com o resultado do processo de criação do Rangout e entendemos que o produto não está completo: melhorias e novos testes de usabilidade ainda serão aplicados.</p>
<p>Neste projeto, o objetivo foi melhorar a experiência de pessoas com restrições alimentares ao buscar informações, apoio e produtos seguros. Por isso, apresentamos as ações mais importantes de forma clara, prática, simples e funcional.</p>
<p>A criação das personas e as pesquisas foram de grande valor nessa jornada, porque nos fizeram compreender melhor as dores do público e questionar quais seriam as melhores alternativas de solução. Elas também ajudaram a equipe em momentos de dúvida sobre as funcionalidades do produto, mostrando que a busca por apoio, informações e produtos adequados pode ser rápida e eficiente.</p>
<p>Seguimos animadas para continuar aprimorando o Rangout, oferecendo cada vez mais valor aos usuários e ajudando-os a viver melhor com suas restrições alimentares.</p>
<h3>Equipe</h3>
<ul>
  <li><a href="https://www.linkedin.com/in/gabrielacvcnt" target="_blank" rel="noopener">Gabriela Cavalcante</a>, fundadora e CEO do Rangout</li>
  <li><a href="https://www.linkedin.com/in/raizatomazoni/" target="_blank" rel="noopener">Raiza Tomazoni</a>, UX Designer e designer gráfica</li>
</ul>
"""},
    ],
},

# ————————————————————————————————————————————————————————————————
"cte": {
    "title": "Cadastro Técnico Estadual",
    "client": "SUDEMA, Governo da Paraíba",
    "summary": "Sistema para empreendedores, consultores e técnicos da SUDEMA registrarem e acompanharem atividades licenciadas, com fluxos pensados para três perfis muito diferentes.",
    "lede": "Documentação da experiência do usuário no Cadastro Técnico Estadual: as interações, interfaces e fluxos do sistema, pensados para garantir usabilidade, eficiência e satisfação de quem o usa.",
    "tags": ["UX/UI Design", "Governo", "Sistema web", "Responsivo"],
    "cover": "cover-cte.webp",
    "cover_alt": "Notebook sobre a mesa exibindo a página inicial do Cadastro Técnico Estadual, com foto da caatinga paraibana ao fundo",
    "case_cover": "cte-mockup.webp",
    "case_cover_alt": "Notebook sobre a mesa exibindo a página inicial do Cadastro Técnico Estadual",
    "meta": [
        ("Papel", "UX/UI Designer"),
        ("Cliente", "SUDEMA-PB"),
        ("Ano", "2023"),
        ("No ar", '<a href="https://cte.sigma.pb.gov.br" target="_blank" rel="noopener">cte.sigma.pb.gov.br</a>'),
    ],
    "blocks": [
        {"title": "Introdução", "html": """
<p>Esta documentação tem como foco a experiência do usuário no Cadastro Técnico Estadual (CTE). O objetivo é detalhar as interações, interfaces e fluxos de usuários do sistema, garantindo a usabilidade, a eficiência e a satisfação dos usuários finais.</p>
"""},
        {"title": "Problema a ser resolvido", "html": """
<p>O principal problema é a dificuldade enfrentada pelos empreendedores para cadastrar suas atividades junto à SUDEMA e gerenciar os consultores vinculados à sua conta. Além disso, era preciso melhorar a eficiência do gerenciamento de dados e das interações entre os usuários do sistema.</p>
"""},
        {"title": "Solução", "html": """
<p>A solução proposta é uma plataforma on-line integrada e intuitiva, que facilita o cadastro de atividades pelos empreendedores, simplifica a busca e o vínculo com consultores ambientais qualificados e oferece ferramentas de gerenciamento eficazes para todos os perfis de usuário.</p>
"""},
        {"title": "Visão geral da experiência", "html": """
<p>O CTE foi pensado e desenvolvido com uma abordagem centrada no usuário, priorizando a facilidade de uso, a clareza das informações e a eficiência nas interações.</p>
<h3>Princípios de design</h3>
<ul>
  <li><b>Usabilidade:</b> o sistema foi projetado para ser intuitivo e fácil de usar, independentemente da familiaridade da pessoa com tecnologia. As interfaces foram simplificadas e organizadas de forma lógica, para que todos naveguem com confiança e sem esforço excessivo.</li>
  <li><b>Clareza de informações:</b> um dos principais objetivos do CTE é oferecer informações claras e relevantes em todos os momentos. Da página inicial aos formulários de cadastro e gerenciamento, cada elemento da interface foi pensado para comunicar de forma concisa e compreensível.</li>
  <li><b>Consistência:</b> as interfaces seguem um conjunto consistente de padrões de design, o que facilita a familiarização e a navegação em todo o sistema.</li>
  <li><b>Feedback:</b> o sistema responde de forma clara e imediata a cada ação, para que o usuário saiba sempre o status das operações.</li>
  <li><b>Suporte:</b> páginas de ajuda e formulários de dúvidas facilitam a comunicação entre usuários e equipe técnica.</li>
</ul>
""",
         "media": [
            ("img", "cte-inicio.webp", "Página inicial com explicação do que é o CTE, quem precisa se cadastrar e botões para acessar, criar conta e consultar", "Página inicial: o que é o cadastro e quem precisa dele vêm antes do login."),
         ]},
        {"title": "Componentes de interface", "html": """
<ul>
  <li><b>Navegação intuitiva:</b> estrutura clara e hierárquica, que facilita encontrar e acessar as diferentes funcionalidades.</li>
  <li><b>Formulários amigáveis:</b> projetados com atenção especial à usabilidade, com descrições, exemplos, validação em tempo real e feedback para orientar o preenchimento.</li>
  <li><b>Controles interativos:</b> botões, links e outros elementos interativos com destaque visual e comportamento consistente.</li>
  <li><b>Feedback visual:</b> cores e ícones comunicam informações importantes e orientam o usuário em suas ações.</li>
</ul>
<h3>Responsividade</h3>
<p>O sistema tem design responsivo e se adapta automaticamente a diferentes dispositivos e tamanhos de tela, garantindo uma experiência consistente no computador, no tablet e no celular.</p>
""",
         "media": [
            ("img", "cte-atividades.webp", "Lista de atividades do empreendedor com filtros por licença, atividade e status e menu lateral fixo", "Área do empreendedor: menu lateral fixo, filtros e um aviso que evita cadastros antes da licença."),
            ("phones", [("cte-mobile.webp", "Lista de atividades no celular com status por cor")], "No celular, a mesma lista com status identificados por cor."),
         ]},
        {"title": "Personas", "html": """
<p>O CTE atende três perfis com objetivos e rotinas bem diferentes: a empreendedora que precisa se regularizar, o consultor que faz isso por vários clientes e o técnico que administra o sistema.</p>
""",
         "media": [
            ("img", "cte-personas.webp", "Personas Ana Silva, empreendedora de 43 anos de Campina Grande; Pedro Oliveira, engenheiro ambiental de 34 anos de João Pessoa; e João Santos, técnico ambiental de 56 anos de João Pessoa, com descrição e objetivos", "Personas: Ana Silva (empreendedora), Pedro Oliveira (consultor) e João Santos (técnico)."),
         ]},
        {"title": "Histórias de usuário", "html": """
<h3>Para a empreendedora</h3>
<ul>
  <li>Como Ana Silva, quero cadastrar novas atividades no CTE para obter certificados de regularidade.</li>
  <li>Como Ana Silva, quero visualizar meus dados cadastrais e atualizar meus dados de acesso e contato.</li>
  <li>Como Ana Silva, quero ver o histórico de todas as ações realizadas na minha conta, incluindo as que meu consultor realizou.</li>
  <li>Como Ana Silva, quero aceitar ou recusar solicitações de vínculo de consultores para receber assistência na regularização ambiental.</li>
</ul>
<h3>Para o consultor</h3>
<ul>
  <li>Como Pedro Oliveira, quero solicitar vínculo com empreendedores para ajudá-los no processo de regularização ambiental.</li>
  <li>Como Pedro Oliveira, quero cadastrar e visualizar atividades dos empreendedores vinculados para garantir sua regularidade.</li>
  <li>Como Pedro Oliveira, quero visualizar meus dados cadastrais e atualizar meus dados de acesso e contato.</li>
  <li>Como Pedro Oliveira, quero ver o histórico das ações dos empreendedores com quem tenho vínculo.</li>
</ul>
<h3>Para o técnico</h3>
<ul>
  <li>Como João Santos, quero visualizar, atualizar e excluir qualquer conta de usuário para garantir a integridade do sistema.</li>
  <li>Como João Santos, quero visualizar e excluir atividades dos empreendedores para corrigir informações incorretas ou desatualizadas.</li>
  <li>Como João Santos, quero gerenciar os vínculos de consultores, podendo aceitar, recusar ou remover vínculos conforme necessário.</li>
  <li>Como João Santos, quero atribuir permissões a outros técnicos para auxiliar na administração do CTE.</li>
  <li>Como João Santos, quero ver o histórico das ações de todos os empreendedores do sistema.</li>
</ul>
"""},
        {"title": "Fluxos dos usuários", "html": """
<p>Cada fluxo descreve o caminho de uma persona para cumprir uma tarefa. Abra cada um para ver os passos.</p>

<h3>Empreendedora: Ana Silva</h3>
<details class="flow"><summary>Cadastro de nova atividade</summary><ol>
  <li>Ana acessa o CTE e entra na sua conta.</li>
  <li>Na área do empreendedor, seleciona a opção de cadastrar nova atividade.</li>
  <li>Preenche o número da licença da atividade.</li>
  <li>Depois de revisar as informações, confirma o cadastro.</li>
</ol></details>
<details class="flow"><summary>Gerar certificado de regularidade</summary><ol>
  <li>Ana acessa o menu de cadastros.</li>
  <li>Seleciona a opção de ver os detalhes da atividade.</li>
  <li>Confere as informações e gera o certificado de regularidade para impressão.</li>
</ol></details>
<details class="flow"><summary>Gerenciamento de dados cadastrais</summary><ol>
  <li>Ana decide atualizar seu endereço de e-mail.</li>
  <li>Acessa os dados cadastrais da conta e seleciona a opção de alterar dados de acesso e de contato.</li>
  <li>Atualiza o e-mail e confirma a alteração.</li>
</ol></details>
<details class="flow"><summary>Gerenciamento de vínculos com consultores</summary><ol>
  <li>Ana recebe uma solicitação de vínculo de um consultor.</li>
  <li>Acessa a área de gestão de vínculos e visualiza os documentos do consultor.</li>
  <li>Decide aceitar ou recusar o vínculo.</li>
</ol></details>
<details class="flow"><summary>Histórico de ações na conta</summary><ol>
  <li>Ana acessa o menu de histórico.</li>
  <li>Visualiza quais ações foram realizadas na sua conta e quem as realizou.</li>
</ol></details>

<h3>Consultor: Pedro Oliveira</h3>
<details class="flow"><summary>Solicitação de vínculo com empreendedores</summary><ol>
  <li>Pedro acessa o CTE e entra na sua conta de consultor.</li>
  <li>Procura empreendedores que possam precisar de assistência na regularização ambiental.</li>
  <li>Envia solicitações de vínculo para os empreendedores selecionados.</li>
</ol></details>
<details class="flow"><summary>Cadastro de atividades</summary><ol>
  <li>Pedro visualiza as atividades dos empreendedores vinculados à sua conta.</li>
  <li>Adiciona novas atividades conforme necessário.</li>
</ol></details>
<details class="flow"><summary>Gerar certificado de regularidade</summary><ol>
  <li>Pedro visualiza os detalhes das atividades dos empreendedores vinculados.</li>
  <li>Confere as informações e gera o certificado de regularidade para impressão.</li>
</ol></details>
<details class="flow"><summary>Gerenciamento de dados cadastrais</summary><ol>
  <li>Pedro decide alterar sua senha.</li>
  <li>Acessa os dados cadastrais da conta e seleciona a opção de alterar dados de acesso e de contato.</li>
  <li>Atualiza a senha e confirma a alteração.</li>
</ol></details>
<details class="flow"><summary>Histórico de ações dos empreendedores</summary><ol>
  <li>Pedro precisa conferir quem alterou o e-mail na conta de um empreendedor.</li>
  <li>Acessa o histórico desse empreendedor.</li>
  <li>Visualiza quais ações foram realizadas, quando e por quem.</li>
</ol></details>

<h3>Técnico: João Santos</h3>
<details class="flow"><summary>Gerenciamento de contas de usuário</summary><ol>
  <li>João precisa alterar o telefone de um consultor.</li>
  <li>Acessa o painel de gerenciamento de contas e visualiza os dados cadastrais da conta.</li>
  <li>Atualiza o número de telefone e confirma a ação.</li>
</ol></details>
<details class="flow"><summary>Visualização e exclusão de atividades</summary><ol>
  <li>João visualiza os detalhes de todas as atividades dos empreendedores do CTE.</li>
  <li>Tem permissão para excluir atividades dos empreendedores.</li>
</ol></details>
<details class="flow"><summary>Gerenciamento de vínculos de consultores</summary><ol>
  <li>João revisa os vínculos entre consultores e empreendedores.</li>
  <li>Aceita, recusa ou remove vínculos conforme necessário.</li>
</ol></details>
<details class="flow"><summary>Atribuição de permissões a outros técnicos</summary><ol>
  <li>João precisa configurar o perfil de um novo técnico.</li>
  <li>Entra no painel de perfis e permissões e atribui ao novo técnico autorizações de edição e/ou exclusão.</li>
</ol></details>
<details class="flow"><summary>Histórico de ações dos empreendedores</summary><ol>
  <li>João quer saber por que uma atividade foi excluída.</li>
  <li>Acessa o histórico do empreendedor que tinha a atividade.</li>
  <li>Visualiza qual técnico fez a exclusão e qual foi a justificativa.</li>
</ol></details>
""",
         "media": [
            ("img", "cte-acoes.webp", "Modal Outras ações listando solicitações que devem ser feitas pelo PBdoc", "Quando uma ação depende de outro sistema, a tela diz qual é e leva até ele."),
            ("img", "cte-justificativa.webp", "Modal de justificativa no histórico, mostrando qual técnico excluiu a atividade e por quê", "Histórico: o técnico vê quem excluiu uma atividade e a justificativa."),
         ]},
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
