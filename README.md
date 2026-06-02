#  EchatonGaze v2.0
> **Passive OSINT & Metadata Reconnaissance Tool**

O **EchatonGaze** é uma ferramenta de reconhecimento passivo desenvolvida para auxiliar em investigações de fontes abertas (OSINT). O foco principal é a extração de informações públicas que muitas vezes passam despercebidas em perfis e repositórios.

---

##  Funcionalidades Principais

* **Busca por E-mails Ocultos:** Analisa eventos de commits públicos para extrair e-mails reais de usuários.
* **Mapeamento de Repositórios:** Identifica branches, linguagens e padrões de desenvolvimento.
* **Scanner de Metadados:** Estrutura base para análise de arquivos e extração de informações sensíveis.
* **Interface Terminal-First:** Otimizado para o terminal do Kali Linux.

---

##  Como Executar

### Instalação e Ambiente Virtual
Para evitar conflitos de dependências no Kali, recomenda-se o uso de um ambiente virtual (venv):

```bash
# Clonar o repositório
git clone [https://github.com/AlariPWN/EchatonGaze.git](https://github.com/AlariPWN/EchatonGaze.git)
cd EchatonGaze

# Criar e ativar o ambiente virtual
python3 -m venv venv
source venv/bin/activate

# Instalar dependências dentro do venv
pip install requests pillow

Com o ambiente virtual ativado:
python3 echatongaze.py <github_username>

##  Detalhes do Projeto
Desenvolvedora: Larissa Cristina
Grupo de Investigação: Echatonkiros
Status: v2.0 (Fase de Implementação)

##  Aviso Legal (Legal Disclaimer)
Este software foi criado para fins educacionais e de pesquisa em segurança cibernética. O uso desta ferramenta para coletar dados sem autorização prévia em sistemas que não permitem tal prática é de inteira responsabilidade do usuário final. Não utilize para fins maliciosos.

---
Developed with ☕ and Kali Linux
