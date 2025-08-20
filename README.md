# 📊 Dashboard de Softwares

Este repositório contém um **dashboard online** para facilitar o download e atualização dos softwares utilizados pela equipe.  

🔗 **Acesse aqui:** (https://tomatomotion.github.io/software-dashboard/)  

---

## 🚀 Como funciona
- A página lista todos os softwares principais da equipe.  
- Cada card possui um botão **Baixar**, que leva diretamente ao site oficial da última versão do software.  
- O dashboard é atualizado **automaticamente 1 vez por mês** (todo dia **1º**) através do **GitHub Actions**.  
- Caso seja necessário, é possível rodar a atualização manualmente.  

---

## 🖥️ Softwares incluídos
- AnyDesk  
- DaVinci Resolve / Studio  
- GeForce Experience  
- HandBrake  
- K-Lite Mega Codec Pack  
- Maxon One  
- Monday  
- Microsoft Teams  
- OBS Studio  
- Wacom Tablet Drivers  
- AE Scripts  
- FX Console (Video Copilot)  
- SABER (Video Copilot)  
- Mister Horse (Animation Composer)  
- Resolume  
- RSMB  
- Overlord  

---

## 🔄 Atualização automática
- O GitHub Actions roda um script Python que **regera o `index.html`** com os links oficiais.  
- Frequência: **mensal (todo dia 1º)**.  
- Também pode ser rodado manualmente em **Actions → Run workflow**.  

---

## 📥 Como contribuir
Se você precisar adicionar novos softwares ou ajustar algum link:  
1. Edite o arquivo `update_links.py` e adicione o novo software no dicionário `softwares`.  
2. Faça um commit com a alteração.  
3. Rode o workflow manualmente em **Actions** ou aguarde a execução automática do próximo mês.  

---

## 👨‍💻 Autor
Criado e mantido por **Israel Filho (Tomate)**. 
