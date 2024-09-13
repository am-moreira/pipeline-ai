import os
import psycopg2
from psycopg2 import sql
from contrato import Vendas
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

def insert_banco(dados: Vendas):
    """
    Função para inserir os dados na tabela
    """
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        cursor = conn.cursor()
        sql_query = sql.SQL(
            "INSERT INTO vendas (email, data_venda, valor, quantidade, produto) VALUES (%s, %s, %s, %s, %s)"
        )
        cursor.execute(sql_query, (
            dados.email,
            dados.data_venda,
            dados.valor,
            dados.quantidade,
            dados.produto.value
        ))
        conn.commit()
        cursor.close()
        conn.close()

        st.success("Dados Inseridos com Sucesso!!")
    except Exception as e:
        st.error(f"Erro ao salva no banco de dados: {e}")