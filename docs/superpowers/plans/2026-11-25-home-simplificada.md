# Home simplificada Implementation Plan

> **For agentic workers:** executado em modo nativo nesta sessão (o usuário pediu para começar direto).

**Goal:** Substituir a home de 14 blocos por uma home de 8 blocos centrada na criomodelagem, com WhatsApp sempre visível.

**Architecture:** `index.html` reescrito como HTML estático com CSS próprio em `assets/home.css` e JS mínimo inline. Páginas de tratamento só recebem número de WhatsApp corrigido e CTA alinhado.

**Tech Stack:** HTML, CSS, JS puro; Google Fonts (Cormorant Garamond + Montserrat). Verificação com `scripts/verificar-site.py` (Python stdlib).

**Spec:** `docs/superpowers/specs/2026-11-25-home-simplificada-design.md`

## Global Constraints
- WhatsApp: `https://wa.me/5548988430101?text=...` em todos os links; número exibido `(48) 98843-0101`.
- Termo de CTA: "consulta" (nunca "Agendar avaliação"). "avaliações" só para Google.
- Dados reais: Google 5,0 (137 avaliações); depoimentos de Patricia Santos, Maria Vogado, Karoline Castro; endereço Av. João Theodoro da Silva, 243 — Sala 03, Roçado, São José — SC; Instagram @alinefarmaceutica.
- Conteúdo faltante marcado com `data-pendente` e texto visível "Foto em breve" / "[aguardando Dra. Aline]".
- Manter `<meta name="robots" content="noindex, nofollow">`.

## Review Focus
- Celular 360–390 px: sem rolagem horizontal; CTA do topo e botão flutuante não se sobrepõem a conteúdo essencial.
- Link de WhatsApp com número antigo (`554888430101`) esquecido em alguma página.
- Âncoras do menu apontando para ids que não existem mais.
- Menu mobile: abrir, fechar ao clicar em link, fechar com Esc.
- Espaços reservados parecendo "quebrados" em vez de intencionais.

---

### Task 1: Script de verificação
**Files:** Create `scripts/verificar-site.py`
- [ ] Checa em `index.html` + `tratamentos/*/index.html`: nenhum `554888430101`; todo link WhatsApp contém `5548988430101`; nenhuma ocorrência de `cdn.tailwindcss.com` na home; home tem exatamente um `<main>`; ids `inicio,resultados,tratamentos,diferenciais,dra-aline,depoimentos,duvidas,contato` existem; todo `href="#x"` aponta para id existente; nenhum texto "Agendar avaliação".
- [ ] Rodar contra a versão atual → FALHA (número antigo, Tailwind, sem `<main>`).

### Task 2: Nova home
**Files:** Rewrite `index.html`; Create `assets/home.css`
- [ ] Header fixo (logo, 5 âncoras, CTA "Agendar consulta"), menu mobile.
- [ ] 8 seções na ordem do spec, com ids da Task 1.
- [ ] Botão flutuante do WhatsApp.
- [ ] `python scripts/verificar-site.py` → home OK.

### Task 3: Páginas de tratamento
**Files:** Modify `tratamentos/*/index.html`
- [ ] Trocar número antigo pelo novo em todos os links.
- [ ] Rodar verificação → tudo OK.

### Task 4: Verificação visual e commit
- [ ] Servir localmente, conferir desktop (1440) e celular (375) no navegador, corrigir.
- [ ] Commit na branch `redesign/home-simplificada`.
