# modulo para interagir com o sistema operacional
import os

# biblioteca streamlit pra criar a interface web
import streamlit as st

# importa classe Groq para se conectar à API da plataforma Groq e acessar o LLM escolhido
from groq import Groq

# Configura a pag streamlit com os elementos básicos: titulo, icone, layout, e sidebar
st.set_page_config(
    page_title="Python AI Coder",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
    )


# Define um prompt de sistema que descreve as regras e comportamento do assistente de IA
CUSTOM_PROMPT = """
Você é um assistente de IA especialista em programação, com foco principal em python. Sua missão aqui nessa terra
será ajudar desenvolvedores iniciantes com dúvidas de programação de forma clara, precisa e útil. 

REGRAS DE OPERAÇÃO:
1. **Foco em Programação**: Responda apenas perguntas relacionadas a programação, algoritmos, estruturas de dados, bibliotecas e frameworks.
Se o usuário perguntar sobre outro assunto, responda educadamente que seu foco é único e exclusivamente responder perguntas relacionadas a python.
2. **Estrutura de Resposta**: Sempre formate suas respostas da seguinte maneira: 
   * **Explicação Clara**: Comece com uma explicação conceitual sobre o tópico perguntado. Seja direto e didático.
   * **Exemplo de Código**: Forneça um ou mais blocos de código em python com a sintaxe correta. O código deve ser bem comentado para explicar as partes importantes.
   * **Detalhes do Código**: Após o bloco de código, descreva em detalhes o que cada parte do código faz, explicando a lógica e as funções utilizadas.
   * **Documentação de Referência**: Ao final, inclua uma seção chamada "📚 Documentação de Referência" com um link direto e relevante para a documentação oficial da linguagem python (docs.python.org) ou da biblioteca em questão.
3. **Clareza e Precisão**: Use uma linguagem clara. Evite jargões desnecessários. Suas respostas devem ser tecnicamente precisas.

"""

# Cria o conteúdo da barra lateral no streamlit
with st.sidebar:
    
    st.title("🤖 Personal Python AI Assistant")
    
    st.markdown("Um assistente de IA focado em programação python para ajudar iniciantes")
    
    # Campo pra inserir a chave de utilização da API grok
    groq_api_key = st.text_input(
        "Insira sua chave da API groq:", type="password", help="Obtenha sua chave gratuitamente em https://console.grok.com"
    )
    
    # linhas divisorias e explicações extra na barra lateral
    st.markdown("---")
    st.markdown("Desenvolvido para te auxiliar no aprendizado da linguagem de programação python. IA pode cometer erros. Sempre verifique as respostas.")
    
    st.markdown("---")
    st.markdown("Curso sugerido para aprender gratuitamente Python e Data Science: https://www.datascienceacademy.com.br/course/fundamentos-de-linguagem-python-do-basico-a-aplicacoes-de-ia")
    
st.title("Assitente Pessoal de Programação Python 🐍")
st.caption("Faça sua pergunta sobre a linguagem e obtenha código, explicações e referências.")

# Inicializa o histórico de mensagens na sessão, caso ainda não exista
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# exibe todas as mensagens anteriores armazenadas no estado da sessão 
for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        
        
# inicializa a variavel do cliente groq como None
client = None

# verifica se o user forneceu a chave de api da groq
if groq_api_key:
    
    try:
        
        # cria cliente com chave fornecida
        client = Groq(api_key=groq_api_key)
        
    except Exception as e:
        
        st.sidebar.error(f"Erro ao inicializar cliente groq: {e}")
        st.stop()
        
# caso não tenha a chave
elif st.session_state["messages"]:
    st.warning("Por favor, insira sua chave de API groq na barra lateral para utilizar o assistente pessoal")

# Captura a entrada do user no chat
if prompt := st.chat_input("Digite aqui a sua dúvida. Irei te responder imediatamente!"):
    
    # Se não houver cliente válido
    if not client:
        st.warning("Cliente inválido. Por favor, insira sua chave de API groq na barra lateral para utilizar o assistente pessoal")
        st.stop()
        
    # Armazena a msg do user no estado da sessão
    st.session_state["messages"].append({"role": "user", "content": prompt})
    
    # Exibe mensagem do usuario no chat 
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Prepara mensagens para enviar à API, incluindo o prompt de sistema
    messages_for_api = [{"role": "system", "content": CUSTOM_PROMPT}]
    for msg in st.session_state["messages"]:
        messages_for_api.append(msg)
        
    # Cria a resposta do assistente no chat
    with st.chat_message("assistant"):
        
        with st.spinner("Analisando sua pergunta..."):
            
            try:
                
                # Chama a API da Groq para gerar a resposta do assistente 
                chat_completion = client.chat.completions.create(
                    messages = messages_for_api,
                    model = "openai/gpt-oss-20b",
                    temperature = 0.7,
                    max_tokens = 2048
                ) 
                
                # extrai a resposta gerada pela API
                ai_response = chat_completion.choices[0].message.content
                
                # exibe a resposta
                st.markdown(ai_response)
                
                # armazena resposta no estado da sessão
                st.session_state.messages.append({"role" : "assistant", "content": ai_response})
                
            # caso ocorra erro na comunicação com a API, informa o usuario
            except Exception as e:
                st.error(f"Ocorreu um erro ao se comunicar com a API da Groq: {e}")
    
    
    
    

st.markdown(
    """
    <div style:"text-align:center; color:gray;">
    <hr><p>Desenvolvido durante o curso de programação python da DSA - Data Science Academy</p>
    </div>
    """,
    unsafe_allow_html = True
)