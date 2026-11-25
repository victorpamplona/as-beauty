# Home simplificada — AS Beauty Center (design curto)

Data: 2026-11-25 · Branch: `redesign/home-simplificada`

## Intenção
A cliente achou a V2 confusa: bonita, mas com blocos demais, mensagem repetida
("tudo começa por uma consulta individualizada"), criomodelagem sem destaque e
sem antes/depois. Objetivo: o visitante entende em segundos o que a clínica faz,
vê resultado e chama no WhatsApp. "Não precisamos colocar mais coisas, precisamos
organizar melhor o que já temos."

## Metas / não-metas / antimetas
- Meta: home em 8 blocos, na ordem pedida pela cliente; WhatsApp visível o tempo todo.
- Meta: manter a identidade sofisticada (serifada + sans, tons nude/caramelo das referências).
- Não-meta: reescrever as 6 páginas de tratamento (só alinhar cabeçalho/CTA/número).
- Antimeta: copiar dados falsos das referências de IA (telefones, nota 4,9, depoimentos inventados).
- Antimeta: pedir muita coisa à Dra. Aline. Onde faltar, espaço reservado visível e marcado.

## Estrutura (ordem da cliente)
1. **Topo** — "Criomodelagem: reduza medidas e valorize suas curvas", subtítulo curto, 3 benefícios, CTA WhatsApp, par Antes/Depois (reservado), foto da Dra. Aline (hero-aline.webp).
2. **Resultados** — 3 pares de criomodelagem + linha "outros procedimentos" (reservados).
3. **Tratamentos** — 6 cards curtos (corpo/face/capilar/laser/drenagem/flacidez) → páginas existentes.
4. **Diferenciais** — "Por que a AS Beauty Center": 4 itens + foto da clínica (junta método, experiência e galeria).
5. **Dra. Aline** — retrato, 2 frases, números já publicados (+2.000 alunas, 26,7k), link Instagram.
6. **Depoimentos** — 3 depoimentos reais + selo Google 5,0 (137).
7. **Dúvidas frequentes** — 4–5 perguntas; respostas da crio reservadas até a Aline responder.
8. **Chamada final + contato** — CTA WhatsApp, endereço, horário, mapa em link; rodapé enxuto.

Sai: seletor de preocupações, faixa assinatura, citação solta, "Em dúvida?", bloco Instagram/autoridade, jornada em 4 passos, galeria separada.

## Decisões
- Termo: **"consulta"** nos CTAs (não "avaliação"). Fácil de trocar se a cliente pedir.
- WhatsApp: (48) 98843-0101 confirmado → links `wa.me/5548988430101` com mensagem pronta.
- Técnica (minha decisão): HTML estático + CSS próprio inline (sai o Tailwind via CDN), `<main>`, JS mínimo (menu mobile, acordeão nativo `<details>`). `noindex` continua até a aprovação.
- Espaço reservado: moldura tracejada com "Antes"/"Depois" e "Foto em breve"; texto marcado `[aguardando Dra. Aline]`, fácil de localizar por busca.

## Pendente com a Aline (enviado à parte)
Antes/depois (2–3 casos de crio, outros se tiver), lista de tratamentos, consulta paga ou não, endereço/horário, respostas do FAQ.
