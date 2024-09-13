import streamlit as st
from contrato import Vendas
from datetime import datetime, time
from database import insert_banco
from pydantic import ValidationError

def main():

    st.title("Sistema de CRM")

    email = st.text_input("E-mail Vendedor")
    data = st.date_input("Data da Venda", format="DD/MM/YYYY")
    hora = st.time_input("Hora da Venda")
    valor = st.number_input("Valor da Venda")
    quantidade = st.number_input("Quantidade", min_value=1, step=1)
    produto = st.selectbox("Produto Vendido", ["Gemini", "ChatGPT", "LLama"])

    data_hora = datetime.combine(data, hora)

    if st.button("Salvar"):
        try:
            venda = Vendas(
                email = email,
                data_venda = data_hora,
                valor = valor,
                quantidade = quantidade,
                produto = produto
            )
            st.write(venda)
            insert_banco(venda)
        except ValidationError as e:
            st.error(f"Erro: {e}")

if __name__ == "__main__":
    main()