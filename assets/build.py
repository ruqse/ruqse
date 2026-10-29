#!/usr/bin/env python3
"""Render the images in the profile README.

    pip install playwright pillow && python3 -m playwright install chromium
    python3 assets/build.py

Writes assets/hero-{light,dark}.png and assets/plates/<slug>-{light,dark}.png.
Each plate is a real figure from the project's repository (sources in
assets/src/) with a short caption. To add a project, put its figure in
assets/src/ and add an entry to PLATES. The build stops if a caption is
too long for its space.

Font: IBM Plex Sans, SIL Open Font License (assets/fonts/).
"""
import html
import pathlib

from PIL import Image
from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).resolve().parent

HERO_BYLINE = "Faruk Dube, bioinformatician"
HERO = ("I study microbiomes and how parasitic nematodes respond to drugs, "
        "and build tools that make research easier.")

# figure: a file in assets/src/, or "dag:<name>" for a pipeline diagram below.
# *asterisks* mark italics.
PLATES = [
    dict(slug="vaginal-virbench", figure="vaginal-virbench.png",
         title="Vaginal VirBench",
         text="Benchmark of 14 virus identification tools on vaginal metagenomes. "
              "Shown: attention-based (purple) versus feature-based (green) tools as fragment length grows.",
         venue="First-author preprint, *bioRxiv* 2026"),
    dict(slug="mitch", figure="mitch.png",
         title="MiTCH",
         text="Multi-omics of bacterial vaginosis in 111 women. "
              "Shown: taxon and metabolite correlations, cut-off r = 0.5.",
         venue="Co-first author, *npj Women’s Health* 2026"),
    dict(slug="parascaris-betatubulin", figure="parascaris-betatubulin.png",
         title="*Parascaris* β-tubulin",
         text="243 haplotypes of seven β-tubulin genes from a benzimidazole-resistant "
              "and a susceptible farm. Shown: share of reads from each gene’s dominant haplotype.",
         venue="Submitted to *PLOS ONE*"),
    dict(slug="parascaris-networks", figure="parascaris-networks.png",
         title="*Parascaris* gene networks",
         text="Tissue-specific response of *P. univalens* to ivermectin. "
              "Shown: *gegf-1* links 71 genes across four co-expression modules.",
         venue="First author, *PLOS ONE* 2024"),
    dict(slug="plague", figure="dag:plague",
         title="PLAGUE",
         text="Recovers and validates plasmids from assembled bacterial genomes. "
              "Shown: the pipeline’s steps.",
         venue="Second-author preprint, *bioRxiv* 2026"),
    dict(slug="hpc-digest", figure="hpc-digest.png",
         title="hpc-digest",
         text="Weekly Slack charts of a research group’s compute and storage use. "
              "Shown: example chart, made from fake data.",
         venue="Python, self-resubmitting Slurm jobs"),
]

THEMES = {
    "light": dict(ink="#1f2328", muted="#59636e", rule="#d1d9e0"),
    "dark": dict(ink="#f0f6fc", muted="#9198a1", rule="#3d444d"),
}


def rich(s):
    out, ital = [], False
    for i, part in enumerate(s.split("*")):
        out.append(("<i>" if i % 2 else "") + html.escape(part) + ("</i>" if i % 2 else ""))
    return "".join(out)


def dag_plague():
    """PLAGUE's documented workflow: MOB-suite, Abricate, SeqKit, then validation
    (Circlator; BBMap and SAMtools when reads are given), filtering, final table."""
    ink, edge = "#1f2328", "#8c959f"
    nodes = {  # name: (x, y, kind, label position)
        "assemblies": (34, 104, "io", "below"), "MOB-suite": (94, 104, "p", "below"),
        "Abricate": (152, 104, "p", "below"), "SeqKit": (208, 104, "p", "below"),
        "Circlator": (268, 54, "p", "above"), "BBMap + SAMtools": (268, 158, "p", "below"),
        "reads": (150, 206, "io", "left"), "filter": (322, 104, "p", "below"),
        "table": (362, 104, "io", "below"),
    }
    edges = [("assemblies", "MOB-suite"), ("MOB-suite", "Abricate"), ("Abricate", "SeqKit"),
             ("SeqKit", "Circlator"), ("SeqKit", "BBMap + SAMtools"),
             ("reads", "BBMap + SAMtools"), ("Circlator", "filter"),
             ("BBMap + SAMtools", "filter"), ("filter", "table")]
    parts = ['<defs><marker id="a" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="6" '
             f'markerHeight="6" orient="auto"><path d="M0 0L8 4L0 8z" fill="{edge}"/></marker></defs>']
    for a, b in edges:
        (x1, y1, *_), (x2, y2, *_) = nodes[a], nodes[b]
        x1, x2 = x1 + 7, x2 - 9
        mx = (x1 + x2) / 2
        parts.append(f'<path d="M{x1} {y1}C{mx} {y1} {mx} {y2} {x2} {y2}" fill="none" '
                     f'stroke="{edge}" stroke-width="1.3" marker-end="url(#a)"/>')
    for name, (x, y, kind, pos) in nodes.items():
        if kind == "io":
            parts.append(f'<circle cx="{x}" cy="{y}" r="5" fill="#fff" stroke="{ink}" stroke-width="1.6"/>')
        else:
            parts.append(f'<circle cx="{x}" cy="{y}" r="5.5" fill="{ink}"/>')
        tx, ty, anchor = {"below": (x, y + 22, "middle"), "above": (x, y - 13, "middle"),
                          "right": (x + 11, y + 4, "start"),
                          "left": (x - 11, y + 4, "end")}[pos]
        parts.append(f'<text x="{tx}" y="{ty}" text-anchor="{anchor}">{html.escape(name)}</text>')
    return ('<svg viewBox="0 0 386 226" width="386" height="226" '
            'style="font:400 11px Plex;fill:#1f2328">' + "".join(parts) + "</svg>")


DAGS = {"plague": dag_plague}

CSS = """
@font-face{font-family:Plex;font-weight:400;src:url(FONTS/IBMPlexSans-Regular.ttf)}
@font-face{font-family:Plex;font-weight:400;font-style:italic;src:url(FONTS/IBMPlexSans-Italic.ttf)}
@font-face{font-family:Plex;font-weight:500;src:url(FONTS/IBMPlexSans-Medium.ttf)}
@font-face{font-family:Plex;font-weight:500;font-style:italic;src:url(FONTS/IBMPlexSans-MediumItalic.ttf)}
*{margin:0;box-sizing:border-box}
body{background:transparent;font-family:Plex;-webkit-font-smoothing:antialiased}
.plate{width:410px;padding:1px}
.fig{height:250px;background:#fff;border:1px solid var(--rule);border-radius:8px;
  display:flex;align-items:center;justify-content:center;padding:14px;overflow:hidden}
.fig img{max-width:100%;max-height:100%;display:block}
.cap{height:122px;padding:14px 2px 0;overflow:hidden}
.t{font-weight:500;font-size:15.5px;line-height:1.3;color:var(--ink)}
.d{font-size:13px;line-height:1.45;color:var(--muted);margin-top:5px}
.v{font-size:12.5px;line-height:1.4;color:var(--ink);margin-top:7px}
.hero{width:840px;padding:8px 2px 18px}
.by{font-size:15px;color:var(--muted);letter-spacing:.01em}
.hero h1{font-weight:500;font-size:35px;line-height:1.17;letter-spacing:-.012em;
  color:var(--ink);margin-top:14px;max-width:780px}
"""


def page(theme, body):
    t = THEMES[theme]
    css = CSS.replace("FONTS", (HERE / "fonts").as_uri())
    return (f"<!doctype html><html><head><meta charset='utf-8'><style>{css}"
            f":root{{--ink:{t['ink']};--muted:{t['muted']};--rule:{t['rule']}}}</style>"
            f"</head><body>{body}</body></html>")


def plate_html(p):
    if p["figure"].startswith("dag:"):
        fig = DAGS[p["figure"][4:]]()
    else:
        fig = f'<img src="{(HERE / "src" / p["figure"]).as_uri()}">'
    return (f'<div class="plate" id="el"><div class="fig">{fig}</div><div class="cap">'
            f'<div class="t">{rich(p["title"])}</div><div class="d">{rich(p["text"])}</div>'
            f'<div class="v">{rich(p["venue"])}</div></div></div>')


def shoot(pg, theme, body, out, check=None):
    tmp = HERE / ".render.html"  # a file page, so it may load local fonts and figures
    tmp.write_text(page(theme, body), encoding="utf-8")
    pg.goto(tmp.as_uri())
    pg.wait_for_load_state("networkidle")
    tmp.unlink()
    pg.evaluate("document.fonts.ready")
    if check:
        over = pg.evaluate("s => { const c = document.querySelector(s); "
                           "return c.scrollHeight - c.clientHeight; }", check)
        if over > 0:
            raise SystemExit(f"{out.name}: caption overflows by {over}px; shorten it")
    pg.locator("#el").screenshot(path=str(out), omit_background=True)
    # 256-colour palette keeps the figures sharp at a fraction of the size
    img = Image.open(out)
    img.quantize(256, method=Image.Quantize.FASTOCTREE, dither=Image.Dither.NONE).save(
        out, optimize=True)


def main():
    (HERE / "plates").mkdir(exist_ok=True)
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        pg = browser.new_page(device_scale_factor=2, viewport={"width": 900, "height": 600})
        for theme in THEMES:
            hero = (f'<div class="hero" id="el"><div class="by">{html.escape(HERO_BYLINE)}</div>'
                    f"<h1>{html.escape(HERO)}</h1></div>")
            shoot(pg, theme, hero, HERE / f"hero-{theme}.png")
            for p in PLATES:
                shoot(pg, theme, plate_html(p), HERE / "plates" / f"{p['slug']}-{theme}.png",
                      check=".cap")
        browser.close()
    print(f"Wrote {2 * (len(PLATES) + 1)} images")


if __name__ == "__main__":
    main()
