import re, json, html, pathlib, markdown
R = pathlib.Path(__file__).parent
DOM = "https://weslopes-eng.github.io/cozyworldpress"
AMZ = "https://www.amazon.com/dp/B0HMPD1G3W"; PIN = "https://www.pinterest.com/cozyworldpress/"
E = html.escape
CSS = """:root{--bg:#fffaf3;--fg:#2b2a33;--mu:#6b6878;--ac:#b5452f;--card:#fff}*{box-sizing:border-box}body{margin:0;font:18px/1.65 Georgia,serif;background:var(--bg);color:var(--fg)}
.wrap{max-width:760px;margin:0 auto;padding:0 20px}header{border-bottom:1px solid #eadfce;padding:14px 0}nav{display:flex;gap:18px;align-items:center;font-family:system-ui,sans-serif;font-size:15px}
nav .logo{font-weight:700;font-size:19px;color:var(--ac);margin-right:auto;text-decoration:none}a{color:var(--ac)}h1{line-height:1.2;font-size:34px}h2{margin-top:2em}
table{border-collapse:collapse;width:100%;font-size:16px}td,th{border:1px solid #eadfce;padding:8px;text-align:left}blockquote{margin:0;padding:10px 16px;background:#f6ecdd;border-left:4px solid var(--ac)}
.btn{display:inline-block;background:var(--ac);color:#fff;padding:10px 18px;border-radius:8px;text-decoration:none;font-family:system-ui,sans-serif}.card{background:var(--card);border:1px solid #eadfce;border-radius:12px;padding:18px 20px;margin:18px 0}
footer{border-top:1px solid #eadfce;margin-top:50px;padding:24px 0;color:var(--mu);font-size:14px;font-family:system-ui,sans-serif}main{padding:10px 0 20px}"""
def shell(title, desc, path, body, ld=None, typ="website"):
    url = f"{DOM}/{path}"
    j = f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False).replace("</","<\\/")}</script>' if ld else ""
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(title)}</title><meta name="description" content="{E(desc)}"><link rel="canonical" href="{url}">
<meta property="og:type" content="{typ}"><meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}"><meta property="og:url" content="{url}"><meta property="og:site_name" content="Cozy World Press">
<link rel="stylesheet" href="{DOM}/style.css">{j}</head><body><header><div class="wrap"><nav><a class="logo" href="{DOM}/">Cozy World Press</a><a href="{DOM}/guides/cozy-christmas-coloring-books-for-adults/">Guides</a><a href="{DOM}/about/">About</a><a href="{PIN}" rel="noopener">Pinterest</a></nav></div></header>
<main class="wrap">{body}</main><footer><div class="wrap">© 2026 Cozy World Press · Coloring books by Lily Atwood · <a href="{PIN}">Pinterest @cozyworldpress</a></div></footer></body></html>"""
pages = []
def write(path, content, lastmod):
    out = R/path/"index.html" if path else R/"index.html"
    out.parent.mkdir(parents=True, exist_ok=True); out.write_text(content); pages.append((path, lastmod))
PUB = {"@type":"Organization","name":"Cozy World Press","url":DOM+"/"}
# Article
src = (R/"content/cozy-christmas-coloring-books-for-adults.md").read_text()
src = re.sub(r"^---.*?---\n", "", src, flags=re.S); src = re.sub(r"<!--.*?-->", "", src, flags=re.S).strip()
title = "Cozy Christmas Coloring Books for Adults: Bold & Easy Picks for 2026"
desc = "Want a relaxing Christmas coloring book you can finish? Pick bold & easy designs on single-sided pages. Our 2026 picks, what to check before buying, and FAQ."
faq = []
for q, a in re.findall(r"^### (.+?)\n(.+?)(?=\n### |\n---|\Z)", src.split("## FAQ",1)[1], flags=re.S|re.M):
    faq.append({"@type":"Question","name":q.strip(),"acceptedAnswer":{"@type":"Answer","text":re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", a.strip())}})
path = "guides/cozy-christmas-coloring-books-for-adults/"
ld = {"@context":"https://schema.org","@graph":[{"@type":"Article","headline":title,"description":desc,"inLanguage":"en-US","datePublished":"2026-10-29","dateModified":"2026-10-29","mainEntityOfPage":DOM+"/"+path,"author":{"@type":"Person","name":"Lily Atwood"},"publisher":PUB},{"@type":"FAQPage","mainEntity":faq}]}
write(path, shell(title, desc, path, markdown.markdown(src, extensions=["tables"]), ld, "article"), "2026-10-29")
# Home
home = f"""<h1>Cozy coloring for adults and teens</h1><p>Cozy World Press makes bold &amp; easy coloring books with warm, cozy scenes from around the world, made to finish in one relaxing evening.</p>
<div class="card"><h2 style="margin-top:0">Cozy Christmas Around the World</h2><p>By Lily Atwood. 50 bold &amp; easy festive scenes from every corner of the globe, single-sided pages, large 8.5 x 8.5 in format.</p><p><a class="btn" href="{AMZ}" rel="noopener">See it on Amazon</a></p></div>
<div class="card"><h2 style="margin-top:0">Cozy Winter Around the World</h2><p>Coming soon: 50 snowy scenes from around the globe.</p></div>
<h2>Guides</h2><ul><li><a href="{DOM}/{path}">Cozy Christmas Coloring Books for Adults: Bold &amp; Easy Picks for 2026</a></li></ul>
<p>See finished pages and color ideas on <a href="{PIN}">Pinterest @cozyworldpress</a>.</p>"""
write("", shell("Cozy World Press | Bold & Easy Cozy Coloring Books for Adults", "Bold & easy cozy coloring books for adults and teens by Lily Atwood, plus guides to choosing and enjoying holiday coloring books.", "", home, {"@context":"https://schema.org","@type":"WebSite","name":"Cozy World Press","url":DOM+"/","inLanguage":"en-US"}), "2026-10-29")
about = f"""<h1>About Cozy World Press</h1><p>Cozy World Press is a small independent imprint of bold &amp; easy coloring books for adults and teens. Our books are illustrated collections published under the pen name <b>Lily Atwood</b>.</p>
<p>Our guides are written by Lily Atwood. Every fact links to its source. When we mention one of our own books, we say so.</p><p>Follow along on <a href="{PIN}">Pinterest @cozyworldpress</a>.</p>"""
write("about/", shell("About | Cozy World Press", "About Cozy World Press, an independent imprint of bold & easy coloring books by Lily Atwood.", "about/", about), None)
(R/"style.css").write_text(CSS)
(R/"robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {DOM}/sitemap.xml\n")
(R/"sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+"".join(f"<url><loc>{DOM}/{p}</loc>"+(f"<lastmod>{d}</lastmod>" if d else "")+"</url>" for p,d in pages)+"</urlset>\n")
(R/".nojekyll").write_text("")
print("built", len(pages), "pages")
