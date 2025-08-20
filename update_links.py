# Gera o HTML atualizado com os links oficiais dos softwares

softwares = {
    "AnyDesk": "https://anydesk.com/pt/downloads/windows",
    "DaVinci Resolve / Studio": "https://www.blackmagicdesign.com/products/davinciresolve/",
    "GeForce Experience": "https://www.nvidia.com/pt-br/geforce/geforce-experience/download/",
    "HandBrake": "https://handbrake.fr/downloads.php",
    "K-Lite Mega Codec Pack": "https://codecguide.com/download_kl.htm",
    "Maxon One": "https://www.maxon.net/en/downloads",
    "Monday": "https://monday.com/download",
    "Teams": "https://www.microsoft.com/pt-br/microsoft-teams/download-app",
    "OBS": "https://obsproject.com/download",
    "Wacom Tablet": "https://www.wacom.com/pt-br/support/product-support/drivers",
    "AE Scripts": "https://aescripts.com/downloadable/",
    "FX Console - Video Copilot": "https://www.videocopilot.net/blog/2016/05/new-fx-console-plug-in-for-after-effects/",
    "SABER - Video Copilot": "https://www.videocopilot.net/blog/2016/06/new-plug-in-saber-now-available/",
    "Mister Horse": "https://misterhorse.com/products/animation-composer",
    "Resolume": "https://resolume.com/download/",
    "RSMB": "https://revisionfx.com/products/rsmb/",
    "Overlord": "https://battleaxe.co/overlord"
}

html_head = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Dashboard de Softwares</title>
  <style>
    body { font-family: Arial, sans-serif; background: #f4f4f9; margin: 0; padding: 20px; }
    h1 { text-align: center; margin-bottom: 20px; }
    .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: 15px; }
    .card { background: white; padding: 20px; border-radius: 12px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); text-align: center; }
    .btn { display: inline-block; margin-top: 10px; padding: 10px 15px; background: #007BFF; color: white; text-decoration: none; border-radius: 8px; }
    .btn:hover { background: #0056b3; }
  </style>
</head>
<body>
  <h1>Dashboard de Atualização de Softwares</h1>
  <div class="grid">
"""

html_footer = """  </div>
</body>
</html>"""

cards = ""
for name, link in softwares.items():
    cards += f"""
    <div class="card">
      <h3>{name}</h3>
      <a class="btn" href="{link}" target="_blank">Baixar</a>
    </div>
    """

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_head + cards + html_footer)
