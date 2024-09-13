from datetime import datetime
from typing import Tuple
from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt
from enum import Enum

class ProdutoEnum(str, Enum):
    """
    Modelo de validação dos produtos.
    """
    produto1 = "Gemini"
    produto2 = "ChatGPT"
    produto3 = "LLama"

class Vendas(BaseModel):
    """
    Modelo de dados para as vendas.

    Args:
        email (EmailStr): email do comprador
        data (datetime): data e hora da compra
        valor (PositiveFloat): valor da compra
        produto (ProdutoEnum): nome do produto
        quantidade (PositiveInt): quantidade de produtos
    """
    email: EmailStr
    data_venda: datetime
    valor: PositiveFloat
    quantidade: PositiveInt
    produto: ProdutoEnum
