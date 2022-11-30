#%%
import pandas as pd
import numpy as np
import re
import os


def nro_upas(path: str) -> pd.DataFrame:
    """Converte a base extraida do DataSUS para um formato utilizavel na regressão.
    Caso haja duplicidade de reportes para um mesmo mês, adotamos como correto o
    maior número informado. O ID do município não é o mesmo utilizado pelo IBGE.

    A forma de extração utilizada dentro do DataSUS é:
        CNES - Estabelecimentos > Tipo de Atendimento Prestado - Urgência > UF > Tipo de Estabelecimento = Pronto Atendimento.

    path: caminho para o arquivo bruto do DataSUS.
    """
    # https://towardsdatascience.com/reshaping-a-pandas-dataframe-long-to-wide-and-vice-versa-517c7f0995ad
    # https://stackoverflow.com/questions/6116978/how-to-replace-multiple-substrings-of-a-string

    df = pd.read_csv(path, header=4, nrows=184, encoding="windows-1252", sep=";")

    df = pd.melt(
        df,
        id_vars=["Município"],
        value_vars=list(df.columns[1:]),
        value_name="upas",
        var_name="periodo",
    )

    converter = {
        "/Jan": "01",
        "/Fev": "02",
        "/Mar": "03",
        "/Abr": "04",
        "/Mai": "05",
        "/Jun": "06",
        "/Jul": "07",
        "/Ago": "08",
        "/Set": "09",
        "/Out": "10",
        "/Nov": "11",
        "/Dez": "12",
    }

    pattern = re.compile("|".join(converter.keys()))
    f = lambda x: converter[re.escape(x.group(0))]

    df = df.assign(
        id_municipio=df["Município"].str.slice(0, 6),
        nome_municipio=df["Município"].str.slice(7),
        periodo=pd.to_numeric(
            [pattern.sub(f, i) for i in df["periodo"]], errors="raise"
        ),
        ano=pd.to_numeric(df["periodo"].str.slice(0, 4), errors="raise"),
        upas=pd.to_numeric(df["upas"], errors="coerce").fillna(0, downcast="int"),
    )

    df = df.drop(labels=["Município"], axis=1)

    df = pd.pivot_table(
        data=df,
        values="upas",
        index=["id_municipio", "nome_municipio", "periodo", "ano"],
        aggfunc=max,
    ).reset_index()

    df = df[["periodo", "ano", "id_municipio", "nome_municipio", "upas"]]

    return df


def nro_mortes_mes(path: str) -> pd.DataFrame:
    """Converte a base de número de mortes extraida do DataSUS para um formato utilizavel
    na regressão. O ID do município não é o mesmo utilizado pelo IBGE.

    A forma de extração utilizada dentro do DataSUS é:
        Estatísticas Vitais > Mortalidade - desde 1996 pela CID-10 > Mortalidade geral > UF > Coluna = Mês do Óbito >
        Conteúdo = Óbitos p/ Ocorrência > Capítulo CID-10 = I + III + IV + IX + X + XI + XX

    É necessário repetir esse passo a passo para cada ano de interesse.

    path: caminho para o arquivo bruto do DataSUS.
    """

    with open(path, "r") as file:
        lines = file.readlines()
        ano_ref = lines[3].strip().split(":")[1]

        nrows = 0
        for line in lines[5:]:
            if not line.startswith('"Total"'):
                nrows += 1
            else:
                break

    df = pd.read_csv(path, header=4, nrows=nrows, encoding="windows-1252", sep=";")

    df = pd.melt(
        df,
        id_vars=["Município"],
        value_vars=list(df.columns[1:-1]),
        value_name="mortes",
        var_name="periodo",
    )

    converter = {
        "Janeiro": "01",
        "Fevereiro": "02",
        "Março": "03",
        "Abril": "04",
        "Maio": "05",
        "Junho": "06",
        "Julho": "07",
        "Agosto": "08",
        "Setembro": "09",
        "Outubro": "10",
        "Novembro": "11",
        "Dezembro": "12",
    }

    converter = dict((re.escape(k), v) for k, v in converter.items())
    pattern = re.compile("|".join(converter.keys()))
    f = lambda x: converter[re.escape(x.group(0))]

    df = df.assign(
        id_municipio=df["Município"].str.slice(0, 6),
        nome_municipio=df["Município"].str.slice(7),
        periodo=pd.to_numeric(
            [ano_ref + pattern.sub(f, i) for i in df["periodo"]], errors="raise"
        ),
        ano=pd.to_numeric(ano_ref, errors="raise"),
        mortes=pd.to_numeric(df["mortes"], errors="coerce").fillna(0, downcast="int"),
    )

    df = df.drop(labels=["Município"], axis=1)

    df = df[["periodo", "ano", "id_municipio", "nome_municipio", "mortes"]]

    return df


def consolidar_nro_mortes_ano(folder: str) -> pd.DataFrame:
    """Consolida a base de número de mortes por mês."""

    files = os.listdir(folder)

    df = None

    for file in files:
        f = nro_mortes_mes(folder + file)
        df = pd.concat([df, f], ignore_index=True)

    return df


def populacao_sp(path: str) -> pd.DataFrame:
    """Le a base de populacao dos municipios de SP.
    Query utilizada no BigQuery:

        SELECT *
        FROM `basedosdados.br_ibge_populacao.municipio`
        WHERE 1 = 1
        AND ano >= 2010
        AND ano <= 2020
        AND sigla_uf = 'SP'

    path: caminho para o arquivo bruto da Base dos Dados.

    """

    df = pd.read_csv(path, dtype={"id_municipio": str})

    df = df.assign(
        id_municipio_6digitos=df["id_municipio"].str.slice(0, 6),
        id_municipio_7digitos=df["id_municipio"],
    )

    df = df.drop(["id_municipio"], axis=1)

    return df


def juntar_bases(df_pop, df_mortes, df_upas) -> pd.DataFrame:
    """"""

    A = pd.merge(
        left=df_mortes,
        right=df_upas,
        how="left",
        on=["periodo", "ano", "id_municipio", "nome_municipio"],
    )

    B = pd.merge(
        left=A,
        right=df_pop,
        how="left",
        left_on=["id_municipio", "ano"],
        right_on=["id_municipio_6digitos", "ano"],
    )

    B = B.assign(upas=B["upas"].fillna(0, downcast="int"))

    B = B[
        [
            "periodo",
            "ano",
            "id_municipio",
            "nome_municipio",
            "mortes",
            "populacao",
            "upas",
        ]
    ]

    return B


def criar_variaveis_regressao(df: pd.DataFrame) -> pd.DataFrame:
    """Cria as variáveis no formato utilizado pela regressão dos artigos de referência."""

    df = df.assign(
        obitos_pc=((df["mortes"] / df["populacao"]) * 100000),
        upa_pc=((df["upas"] / df["populacao"]) * 100000),
    )

    dummy_tempo = pd.get_dummies(
        df["ano"],
        prefix="ef_tempo",
        drop_first=True,
    )

    dummy_municipio = pd.get_dummies(df["id_municipio"], prefix="ef", drop_first=True)

    df = pd.concat([df, dummy_tempo, dummy_municipio], axis=1)

    return df


#%%

if __name__ == "__main__":

    df_populacao = populacao_sp("dados/populacao_sp.csv")
    df_mortes = consolidar_nro_mortes_ano("dados/mortes_por_mes_sp/")
    df_upas = nro_upas("dados/upas_sp.csv")

    df = juntar_bases(df_populacao, df_mortes, df_upas)

    df = criar_variaveis_regressao(df)

# %%
