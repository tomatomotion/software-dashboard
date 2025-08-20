import requests
from bs4 import BeautifulSoup

# Caminho do arquivo HTML do dashboard
HTML_FILE = "index.html"

# Funções para buscar os links atualizados
def get_latest_handbrake():
    url = "https://github.com/HandBrake/HandBrake/releases/latest"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    tag = soup.find("a", {"href": lambda x: x and x.endswith("x86_64-Win_GUI.exe")})
    return "https://github.com" + tag["href"] if tag else None

def get_latest_obs():
    url = "https://obsproject.com/pt-br/download"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    tag = soup.find("a", {"class": "downloadButton"})
    return tag["href"] if tag else None

def get_latest_anydesk():
    return "https://download.anydesk.com/AnyDesk.exe"

def get_latest_geforce():
    return "https://us.download.nvidia.com/GFE/GFEClient/3.27.0.147/GeForce_Experience_v3.27.0.147.exe"

def get_latest_adobe_cc():
    return "https://www.adobe.com/download/creative-cloud?promoid=GVTYXZK9&mv=other"

def get_latest_maxon_one():
    return "https://www.maxon.net/en/downloads"

def get_latest_k_lite():
    return "https://www.codecguide.com/download_k-lite_codec_pack_mega.htm"

def get_latest_monday():
    return "https://monday.com/download"

def get_latest_teams():
    return "https://aka.ms/teamsdownload"

def get_latest_wacom():
    return "https://cdn.wacom.com/WacomTabletDriverInstaller.exe"

def get_latest_blackmagic():
    return "https://www.blackmagicdesign.com/support/family/davinci-resolve-and-fusion"

# Função para SharePoint ou links fixos
def sharepoint_link(url):
    return url

# Mapeamento de softwares e links
softwares = {
    "CreativeCloud": get_latest_adobe_cc(),
    "Maxon One": get_latest_maxon_one(),
    "GeForce Experience": get_latest_geforce(),
    "HandBrake": get_latest_handbrake(),
    "K-Lite Mega Codec Pack": get_latest_k_lite(),
    "AnyDesk": get_latest_anydesk(),
    "Monday": get_latest_monday(),
    "Microsoft Teams": get_latest_teams(),
    "OBS Studio": get_latest_obs(),
    "Wacom Tablet Drivers": get_latest_wacom(),
    "EXR-IO": sharepoint_link("https://hypermarcas-my.sharepoint.com/:u:/g/personal/israel_a_filho_hypera_com_br/EeqYyirJpJlGr5e-PRD3sC8BvyiCOzRk5gc7f4X38UXCpw?e=sWSr52"),
    "HapEncoder": sharepoint_link("https://hypermarcas-my.sharepoint.com/:u:/g/personal/israel_a_filho_hypera_com_br/Eb49XDuBkVVPkGfBM0EP6CEBOj1fUbr3kN77NmfKrxzfnA?e=638wxd"),
    "Insta 360 Studio": sharepoint_link("https://hypermarcas-my.sharepoint.com/:u:/g/personal/israel_a_filho_hypera_com_br/ERxLuOn8gtJEnvCBTFVBZkIB9Nmy1HRjtXrrvhhHW1HChA?e=4krAYc"),
    "PSD Codec": sharepoint_link("https://hypermarcas-my.sharepoint.com/:u:/g/personal/israel_a_filho_hypera_com_br/ETBjeIonjYhKtsCuYSODIVwBe-JW2irprVVkLFwy2pBHBQ?e=AFSm57"),
    "RSMB": sharepoint_link("https://hypermarcas-my.sharepoint.com/:u:/g/personal/israel_a_filho_hypera_com_br/EQlHicO91EtDskVNjUyDX8cB3uRhAt6vx0_l51L0o4l71A?e=eCd6vc"),
    "Overlord": sharepoint_link("https://hypermarcas-my.sharepoint.com/:u:/g/personal/israel_a_filho_hypera_com_br/EeFJ2tNCBuxEinwg6-f91KEBiUAEFrhKZG9YSIf7tC85Xw?e=wwxmb4"),
    "FX Console": sharepoint_link("https://hypermarcas-my.sharepoint.com/:u:/g/personal/israel_a_filho_hypera_com_br/EWzBU-HiaipMmoCpyaNzR84Be4eDO5oHHVHMUTFBcwlWaQ?e=qegdHU"),
    "SABER": sharepoint_link("https://hypermarcas-my.sharepoint.com/:u:/g/personal/israel_a_filho_hypera_com_br/EQ52e7h8mSBPmfnUbubZZsUBRqKsq0ArhfokOzGcOMG2Aw?e=oawO5v"),
    "Element 3D": sharepoint_link("https://hypermarcas-my.sharepoint.com/:u:/g/personal/israel_a_filho_hypera_com_br/ESdydWf3oSZJnr0A3H8bTmIBVUib1KJBPZw8DLbOwL9YPA?e=biEfVr"),
    "Brack Light": sharepoint_link("https://hypermarcas-my.sharepoint.com/:u:/g/personal/israel_a_filho_hypera_com_br/EXSm5zTvqtREnfXaYxmIqd0Bh37shma8LotB_I86tI7Pjw?e=ReHUyv"),
    "DaVinci Resolve / Studio": get_latest_blackmagic(),
    "BRAW Studio - Autokroma (AfterCodecs)": sharepoint_link("https://hypermarcas-my.sharepoint.com/:u:/g/personal/israel_a_filho_hypera_com_br/Ef6RUyiOlh5NgWQlHP_E4K4B1_LH51K3i8pxHr20nHApEA?e=Oc2vwe"),
    "BRAW Studio - Codec Visualização": sharepoint_link("https://hypermarcas-my.sharepoint.com/:u:/g/personal/israel_a_filho_hypera_com_br/EfmPOJLYn5NLiTjpWuJFEtsB21HbCGxOcELEpZ3BTteJTQ?e=5ZVOjC")
}

# Atualiza o HTML
def update_html():
    with open(HTML_FILE, "r", encoding="utf-8") as f:
        html = f.read()

    for software, link in softwares.items():
        html = html.replace(
            f'href="{link}"',  # Se o link já estiver atualizado, ignora
            f'href="{link}" target="_blank"'
        )
    with open(HTML_FILE, "w", encoding="utf-8") as f:
        f.write(html)
    print("HTML atualizado com os links mais recentes!")

if __name__ == "__main__":
    update_html()
