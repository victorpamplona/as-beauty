"""Verificações rápidas do site AS Beauty Center.

Uso: python scripts/verificar-site.py   (a partir da raiz do repositório)
Sai com código 1 se algo falhar.
"""
import glob
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
NUMERO = "5548988430101"
NUMERO_ANTIGO = "554888430101"
IDS_HOME = ["inicio", "resultados", "tratamentos", "diferenciais",
            "dra-aline", "depoimentos", "duvidas", "contato"]

erros = []


def checar(cond, msg):
    if not cond:
        erros.append(msg)


paginas = [RAIZ / "index.html"] + [Path(p) for p in sorted(glob.glob(str(RAIZ / "tratamentos" / "*" / "index.html")))]

for pagina in paginas:
    nome = pagina.relative_to(RAIZ).as_posix()
    html = pagina.read_text(encoding="utf-8")
    checar(NUMERO_ANTIGO not in html, f"{nome}: ainda usa o número antigo {NUMERO_ANTIGO}")
    for link in re.findall(r'href="([^"]*(?:wa\.me|whatsapp)[^"]*)"', html):
        checar(NUMERO in link, f"{nome}: link de WhatsApp sem o número correto -> {link[:70]}")
    checar("Agendar avaliação" not in html, f"{nome}: usa 'Agendar avaliação' (o termo é 'consulta')")
    ids = set(re.findall(r'\bid="([^"]+)"', html))
    for alvo in re.findall(r'href="#([^"]+)"', html):
        checar(alvo in ids, f"{nome}: âncora #{alvo} não existe")

home = (RAIZ / "index.html").read_text(encoding="utf-8")
ids_home = set(re.findall(r'\bid="([^"]+)"', home))
for pagina in paginas[1:]:
    for alvo in re.findall(r'href="/#([^"]+)"', pagina.read_text(encoding="utf-8")):
        checar(alvo in ids_home, f"{pagina.relative_to(RAIZ).as_posix()}: link /#{alvo} não existe na home")
checar("cdn.tailwindcss.com" not in home, "index.html: ainda carrega Tailwind via CDN")
checar(home.count("<main") == 1, "index.html: precisa de exatamente um <main>")
for i in IDS_HOME:
    checar(f'id="{i}"' in home, f"index.html: falta a seção #{i}")

if erros:
    print("FALHOU:")
    for e in erros:
        print(" -", e)
    sys.exit(1)
print(f"OK — {len(paginas)} páginas verificadas.")
