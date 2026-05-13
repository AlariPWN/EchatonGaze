# 👁️ EchatonGaze v2.0
> **Passive OSINT & Metadata Reconnaissance Tool**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Kali Linux](https://img.shields.io/badge/Kali_Linux-557C94?style=for-the-badge&logo=kali-linux&logoColor=white)
![OSINT](https://img.shields.io/badge/Security-OSINT-red?style=for-the-badge)

O **EchatonGaze** é uma ferramenta de reconhecimento passivo desenvolvida para auxiliar em investigações de fontes abertas (OSINT). O foco principal é a extração de informações públicas que muitas vezes passam despercebidas em perfis e repositórios.

---

## 🛠️ Funcionalidades Principais

*   **Busca por E-mails Ocultos:** Analisa eventos de commits públicos para extrair e-mails reais de usuários, ignorando as configurações de privacidade do perfil.
*   **Mapeamento de Repositórios:** Identifica branches, linguagens predominantes e padrões de desenvolvimento.
*   **Scanner de Metadados:** Estrutura base para análise de arquivos e extração de informações sensíveis (Passive Scraper).
*   **Interface Terminal-First:** Otimizado para o terminal do Kali Linux com saída colorida e legível.

## 🚀 Como Executar

### Pré-requisitos
Certifique-se de ter o Python 3 instalado e as bibliotecas necessárias:
```bash
pip install requests pillow

Instalação:
git clone [https://github.com/AlariPWN/EchatonGaze.git](https://github.com/AlariPWN/EchatonGaze.git)
cd EchatonGaze

Uso:
python3 echatongaze.py <github_username>

📋 Detalhes do Projeto
Desenvolvedora: Larissa Cristina

Instituição: Faculdade Fadergs (Segurança da Informação)

Grupo de Investigação: Echatonkiros

Status: v2.0 (Fase de Implementação para TCC)

⚠️ Aviso Legal (Legal Disclaimer)
Este software foi criado para fins educacionais e de pesquisa em segurança cibernética. O uso desta ferramenta para coletar dados sem autorização prévia em sistemas que não permitem tal prática é de inteira responsabilidade do usuário final. Não utilize para fins maliciosos.

Developed with ☕ and Kali Linux
