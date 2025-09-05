# 🤖 Tutor de Python com IA - Assistente Pessoal de Programação

Um assistente inteligente de programação Python construído com Streamlit e alimentado pela API LLM do Groq. Esta aplicação foi desenvolvida para ajudar desenvolvedores iniciantes a aprender programação Python através de conversas interativas, exemplos de código e explicações abrangentes.

## 🌟 Funcionalidades

- **Interface de Chat Interativa**: Interface web limpa e amigável construída com Streamlit
- **Especialização em Python**: Assistente de IA dedicado exclusivamente a questões de programação Python
- **Aprendizado Estruturado**: Respostas incluem explicações conceituais, exemplos de código e análises detalhadas
- **Links para Documentação Oficial**: Cada resposta inclui referências relevantes da documentação Python
- **Respostas em Tempo Real**: Respostas rápidas alimentadas por IA usando a infraestrutura otimizada do Groq
- **Memória de Sessão**: Mantém o histórico da conversa durante toda a sessão
- **Destaque de Sintaxe**: Exemplos de código formatados adequadamente e com comentários

## 🎯 Com o que o Assistente Pode Ajudar

- **Fundamentos Python**: Variáveis, tipos de dados, estruturas de controle, funções
- **Programação Orientada a Objetos**: Classes, herança, polimorfismo
- **Estruturas de Dados**: Listas, dicionários, conjuntos, tuplas
- **Algoritmos**: Ordenação, busca, recursão
- **Bibliotecas e Frameworks**: NumPy, Pandas, Flask, Django e muito mais
- **Boas Práticas**: Organização de código, tratamento de erros, debugging
- **Resolução de Problemas**: Design e implementação de algoritmos

## 🛠️ Stack Tecnológico

- **Frontend**: Streamlit
- **Provedor de IA**: API Groq
- **Linguagem**: Python 3.x
- **Modelo**: OpenAI GPT-OSS-20B (via Groq)

## 📋 Pré-requisitos

- Python 3.7 ou superior
- Chave de API Groq (gratuita em [console.groq.com](https://console.groq.com))
- Conexão com a internet para chamadas da API

## 🚀 Instalação e Configuração

### 1. Clone o Repositório
```bash
git clone <url-do-seu-repositorio>
cd dsa_AI_assistant
```

### 2. Crie um Ambiente Virtual (Recomendado)
```bash
# Usando conda (se você tiver Anaconda/Miniconda)
conda create -n ai_python_coder_assistant python=3.9
conda activate ai_python_coder_assistant

# Ou usando venv
python -m venv ai_python_coder_assistant
# No Windows:
ai_python_coder_assistant\Scripts\activate
# No macOS/Linux:
source ai_python_coder_assistant/bin/activate
```

### 3. Instale as Dependências
```bash
pip install streamlit groq
```

### 4. Obtenha sua Chave de API Groq
1. Visite [console.groq.com](https://console.groq.com)
2. Cadastre-se para uma conta gratuita
3. Gere sua chave de API
4. Mantenha-a segura - você irá inseri-la na barra lateral do app

### 5. Execute a Aplicação
```bash
streamlit run AI_python_Assistant.py
```

A aplicação abrirá no seu navegador padrão em `http://localhost:8501`

## 🎮 Como Usar

1. **Insira a Chave da API**: Na barra lateral, cole sua chave de API Groq
2. **Faça Perguntas**: Digite suas dúvidas sobre programação Python no campo de chat
3. **Receba Respostas Estruturadas**: Receba respostas detalhadas com:
   - Explicações conceituais claras
   - Exemplos de código funcionais com comentários
   - Análises passo a passo do código
   - Links para documentação oficial do Python
4. **Continue Aprendendo**: Construa sobre perguntas anteriores na mesma sessão

### Exemplos de Perguntas para Experimentar:
- "Como criar uma lista em Python?"
- "Explique a diferença entre os métodos append() e extend()"
- "Como posso ler um arquivo CSV usando pandas?"
- "O que são decorators em Python e como usá-los?"
- "Como fazer tratamento de exceções em Python?"

## 🔧 Configuração

O assistente está configurado com regras específicas de comportamento:

- **Foco no Domínio**: Responde apenas a questões relacionadas à programação
- **Estrutura de Resposta**: Sempre inclui explicação → código → análise → documentação
- **Temperatura**: Definida em 0.7 para equilibrar criatividade e precisão
- **Max Tokens**: Limitado a 2048 para respostas abrangentes mas focadas

## 📁 Estrutura do Projeto

```
dsa_AI_assistant/
├── AI_python_Assistant.py    # Arquivo principal da aplicação
├── requerements.txt          # Dependências (export do conda)
├── requirements.txt          # Dependências essenciais
├── .vscode/
│   └── settings.json         # Configuração do VS Code
├── README.md                 # Documentação em inglês
└── README_pt-BR.md          # Este arquivo (português)
```

## 🎓 Foco Educacional

Este projeto foi desenvolvido como parte do curso de programação Python da **Data Science Academy (DSA)**. Foi projetado para:

- Apoiar iniciantes no aprendizado de Python
- Fornecer ajuda imediata com dúvidas de programação
- Incentivar boas práticas em programação Python
- Fazer a ponte entre teoria e implementação prática

## 🤝 Contribuindo

Este é um projeto educacional, mas contribuições são bem-vindas! Aqui estão maneiras de ajudar:

- Reportar bugs ou problemas
- Sugerir novas funcionalidades
- Melhorar a documentação
- Adicionar novas perguntas de exemplo
- Otimizar performance do código

## ⚠️ Notas Importantes

- **Custos da API**: Embora o Groq ofereça acesso gratuito, monitore seu uso
- **Limitações da IA**: Sempre verifique sugestões de código e explicações
- **Ferramenta de Aprendizado**: Use como complemento, não substituto do aprendizado estruturado
- **Internet Necessária**: A aplicação precisa de conectividade para chamadas da API

## 🔮 Melhorias Futuras

Potenciais melhorias para versões futuras:

- [ ] Sandbox para execução de código e teste de exemplos
- [ ] Suporte para múltiplas linguagens de programação
- [ ] Exportar histórico de conversas
- [ ] Integração com IDEs Python populares
- [ ] Modo offline com modelos locais
- [ ] Trilhas de aprendizado personalizadas e tutoriais

## 📚 Recursos de Aprendizado Recomendados

- [Curso Python da Data Science Academy](https://www.datascienceacademy.com.br/course/fundamentos-de-linguagem-python-do-basico-a-aplicacoes-de-ia)
- [Documentação Oficial Python](https://docs.python.org/)
- [Tutorial Python.org](https://docs.python.org/3/tutorial/)
- [Real Python](https://realpython.com/)
- [Python Brasil](https://python.org.br/)

## 📄 Licença

Este projeto foi criado para fins educacionais. Sinta-se livre para usar e modificar em sua jornada de aprendizado.

## 🙏 Agradecimentos

- **Data Science Academy** pelo curso abrangente de Python
- **Groq** por fornecer infraestrutura de IA rápida e confiável
- **Streamlit** pelo excelente framework web
- A comunidade Python brasileira pelos recursos contínuos de aprendizado

---

**Bom Aprendizado! 🐍✨**

*Lembre-se: A melhor forma de aprender programação é escrevendo código. Use este assistente como seu companheiro de programação, mas sempre pratique escrevendo e executando código você mesmo!*

## 🌐 Versões de Idioma

- [🇺🇸 English Version](README.md)
- [🇧🇷 Versão Português](README_pt-BR.md)
