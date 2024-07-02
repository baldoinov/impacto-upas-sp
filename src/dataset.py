import re
import os

import pandas as pd
import numpy as np


CONVERSAO_MES_CURTO = {
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

CONVERSAO_MES_LONGO = {
    "Janeiro": "01",
    "Fevereiro": "02",
    "Marco": "03",
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


def numero_de_upas_por_municipio(path: str) -> pd.DataFrame:
    """
    Converte a base extraida do DataSUS para um formato utilizavel na regressão.
    Caso haja duplicidade de reportes para um mesmo mês, adotamos como correto o
    maior número informado. O ID do Municipio não é o mesmo utilizado pelo IBGE.

    A forma de extração utilizada dentro do DataSUS é:
        CNES - Estabelecimentos > Tipo de Atendimento Prestado - Urgência > UF > Tipo de Estabelecimento = Pronto Atendimento.

    path: caminho para o arquivo bruto do DataSUS.
    """
    # https://towardsdatascience.com/reshaping-a-pandas-dataframe-long-to-wide-and-vice-versa-517c7f0995ad
    # https://stackoverflow.com/questions/6116978/how-to-replace-multiple-substrings-of-a-string

    df = pd.read_csv(path, header=4, nrows=184, encoding="windows-1252", sep=";")

    df = pd.melt(
        df,
        id_vars=["Municipio"],
        value_vars=list(df.columns[1:]),
        value_name="upas",
        var_name="periodo",
    )

    pattern = re.compile("|".join(CONVERSAO_MES_CURTO.keys()))
    f = lambda x: CONVERSAO_MES_CURTO[re.escape(x.group(0))]

    df = df.assign(
        id_municipio_6digitos=df["Municipio"].str.slice(0, 6),
        nome_municipio=df["Municipio"].str.slice(7),
        periodo=pd.to_numeric(
            [pattern.sub(f, i) for i in df["periodo"]], errors="raise"
        ),
        ano=pd.to_numeric(df["periodo"].str.slice(0, 4), errors="raise"),
        upas=pd.to_numeric(df["upas"], errors="coerce").fillna(0, downcast="int"),
    )

    df = df.drop(labels=["Municipio"], axis=1)

    df = pd.pivot_table(
        data=df,
        values="upas",
        index=["id_municipio_6digitos", "nome_municipio", "periodo", "ano"],
        aggfunc=max,
    ).reset_index()

    df = df[["periodo", "ano", "id_municipio_6digitos", "nome_municipio", "upas"]]

    return df


def numero_de_samu_por_municipio(path: str) -> pd.DataFrame:
    """
    Converte a base extraida do DataSUS para um formato utilizavel na regressão.
    Caso haja duplicidade de reportes para um mesmo mês, adotamos como correto o
    maior número informado. O ID do Municipio não é o mesmo utilizado pelo IBGE.

    A forma de extração utilizada dentro do DataSUS é:
        CNES - Estabelecimentos > Tipo de Atendimento Prestado - Urgência > UF >
        Tipo de Estabelecimento = UNIDADE MOVEL TERRESTRE,
                                  UNIDADE MOVEL DE NIVEL PRE-HOSPITALAR NA AREA DE URGENCIA,
                                  CENTRAL DE REGULACAO MEDICA DAS URGENCIAS.

    path: caminho para o arquivo bruto do DataSUS.
    """

    df = pd.read_csv(path, header=4, nrows=254, encoding="windows-1252", sep=";")

    df = pd.melt(
        df,
        id_vars=["Municipio"],
        value_vars=list(df.columns[1:]),
        value_name="samu",
        var_name="periodo",
    )

    pattern = re.compile("|".join(CONVERSAO_MES_CURTO.keys()))
    f = lambda x: CONVERSAO_MES_CURTO[re.escape(x.group(0))]

    df = df.assign(
        id_municipio_6digitos=df["Municipio"].str.slice(0, 6),
        nome_municipio=df["Municipio"].str.slice(7),
        periodo=pd.to_numeric(
            [pattern.sub(f, i) for i in df["periodo"]], errors="raise"
        ),
        ano=pd.to_numeric(df["periodo"].str.slice(0, 4), errors="raise"),
        samu=pd.to_numeric(df["samu"], errors="coerce").fillna(0, downcast="int"),
    )

    df = df.drop(labels=["Municipio"], axis=1)

    df = pd.pivot_table(
        data=df,
        values="samu",
        index=["id_municipio_6digitos", "nome_municipio", "periodo", "ano"],
        aggfunc=max,
    ).reset_index()

    df = df[["periodo", "ano", "id_municipio_6digitos", "nome_municipio", "samu"]]

    return df


def numero_de_mortes_por_local(path: str) -> pd.DataFrame:
    """
    Converte a base de número de mortes extraida do DataSUS para um formato utilizavel
    na regressão. O ID do município não é o mesmo utilizado pelo IBGE.

    A forma de extração utilizada dentro do DataSUS é:
        Estatísticas Vitais > Mortalidade - desde 1996 pela CID-10 > Mortalidade geral > UF > Coluna = Local do Óbito >
        Conteúdo = Óbitos p/ Ocorrência > Capítulo CID-10 = I + III + IV + IX + X + XI + XX

    É necessário repetir esse passo a passo para cada ano de interesse.

    path: caminho para o arquivo bruto do DataSUS.
    """

    with open(path, "r", encoding="latin-1") as file:
        lines = file.readlines()
        ano_ref = lines[3].strip().split(":")[1]

        nrows = 0
        for line in lines[5:]:
            if not line.startswith('"Total"'):
                nrows += 1
            else:
                break

    df = pd.read_csv(path, header=4, nrows=nrows, encoding="windows-1252", sep=";")

    df = df.assign(
        id_municipio_6digitos=df["Municipio"].str.slice(0, 6),
        nome_municipio=df["Municipio"].str.slice(7),
        ano=pd.to_numeric(ano_ref, errors="raise"),
        mortes_hospital=pd.to_numeric(df["Hospital"], errors="coerce").fillna(
            0, downcast="int"
        ),
        mortes_outro_estab_saude=pd.to_numeric(
            df["Outro estabelecimento de saude"], errors="coerce"
        ).fillna(0, downcast="int"),
        mortes_domicilio=pd.to_numeric(df["Domicilio"], errors="coerce").fillna(
            0, downcast="int"
        ),
        mortes_via_publica=pd.to_numeric(df["Via publica"], errors="coerce").fillna(
            0, downcast="int"
        ),
        mortes_outros_locais=pd.to_numeric(df["Outros"], errors="coerce").fillna(
            0, downcast="int"
        ),
        mortes_info_ignorada=pd.to_numeric(df["Ignorado"], errors="coerce").fillna(
            0, downcast="int"
        ),
    )

    df = df[
        [
            "ano",
            "id_municipio_6digitos",
            "nome_municipio",
            "mortes_hospital",
            "mortes_outro_estab_saude",
            "mortes_domicilio",
            "mortes_via_publica",
            "mortes_outros_locais",
            "mortes_info_ignorada",
        ]
    ]

    return df


def consolidar_numero_de_mortes_por_local(folder: str) -> pd.DataFrame:
    """Consolida a base de número de mortes por local."""

    files = os.listdir(folder)

    df = None

    for file in files:
        f = numero_de_mortes_por_local(folder + file)
        df = pd.concat([df, f], ignore_index=True)

    return df


def numero_de_mortes_por_mes(path: str) -> pd.DataFrame:
    """
    Converte a base de número de mortes extraida do DataSUS para um formato utilizavel
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
        id_vars=["Municipio"],
        value_vars=list(df.columns[1:-1]),
        value_name="mortes",
        var_name="periodo",
    )

    converter = dict((re.escape(k), v) for k, v in CONVERSAO_MES_LONGO.items())
    pattern = re.compile("|".join(converter.keys()))
    f = lambda x: converter[re.escape(x.group(0))]

    df = df.assign(
        id_municipio_6digitos=df["Municipio"].str.slice(0, 6),
        nome_municipio=df["Municipio"].str.slice(7),
        periodo=pd.to_numeric(
            [ano_ref + pattern.sub(f, i) for i in df["periodo"]], errors="raise"
        ),
        ano=pd.to_numeric(ano_ref, errors="raise"),
        mortes=pd.to_numeric(df["mortes"], errors="coerce").fillna(0, downcast="int"),
    )

    df = df[["periodo", "ano", "id_municipio_6digitos", "nome_municipio", "mortes"]]

    return df


def consolidar_numero_de_mortes_por_ano(folder: str) -> pd.DataFrame:
    """Consolida a base de número de mortes por mês."""

    files = os.listdir(folder)

    df = None

    for file in files:
        f = numero_de_mortes_por_mes(folder + file)
        df = pd.concat([df, f], ignore_index=True)

    return df


def populacao_sp(path: str) -> pd.DataFrame:
    """
    Le a base de populacao dos municipios de SP.
    A query utilizada no BigQuery para extrair os dados está no arquivo dataset.sql.

    path: caminho para o arquivo bruto da Base dos Dados.

    """

    df = pd.read_csv(path, dtype={"id_municipio": str})

    df = df.assign(
        id_municipio_6digitos=df["id_municipio"].str.slice(0, 6),
        id_municipio_7digitos=df["id_municipio"],
    )

    df = df.drop(["id_municipio"], axis=1)

    return df


def pib_municipios(path: str) -> pd.DataFrame:
    """
    Le a base de PIB dos municipios de SP.
    A query utilizada no BigQuery para extrair os dados está no arquivo dataset.sql.

    path: caminho para o arquivo bruto da Base dos Dados.
    """

    df = pd.read_csv(path, dtype={"id_municipio_7digitos": str})

    df = df.assign(
        id_municipio_6digitos=df["id_municipio_7digitos"].str.slice(0, 6),
    )

    return df


def bases_politicas(path: str, type: str = None) -> pd.DataFrame:
    """
    Le as bases de variáveis políticas. Ao extrair as bases nós adotamos a simplificação de
    que o partido que venceu a eleição é o que governará até a próxima eleição. Também
    desconsideramos a possibilidade do governante trocar de partido durante o mandato.

    A query utilizada no BigQuery para extrair os dados está no arquivo dataset.sql.
    """

    if type == "pref":
        df = pd.read_csv(path, dtype={"ano": int, "id_municipio": str})
        df = df.assign(
            id_municipio_7digitos=df["id_municipio"],
            sigla_partido_pref=df["sigla_partido"],
        )
        df = df.drop(labels=["id_municipio", "sigla_partido"], axis=1)
        df = df.assign(ano=df["ano"].replace(2008, 2010))
        df = df.drop(index=[1288, 2497], axis=0)

    else:
        df = pd.read_csv(path)
        df = df.assign(sigla_partido_gov=df["sigla_partido"])
        df = df.drop(labels=["sigla_partido"], axis=1)

    return df


def base_saneamento(path: str) -> pd.DataFrame:
    """
    Converte a base extraida do SNIS para um formato utilizavel na regressão.

    A forma de extração utilizada dentro do SNIS é:
        # https://www.gov.br/mdr/pt-br/assuntos/saneamento/snis
        Série Histórica > Municipios > Informações e indicadores municipais consolidados >
        Ano de Referência = 2010 - 2020 > Estado = São Paulo > Municipios = Todos >
        Famílias de Informações e Indicadores = [AE - Inf. Água, Inf. AE - Esgoto, Inf. AE - Qualidade] >
        Informações e Indicadores = [AG002 - Quantidade de ligações ativas de água,
                                     AG007 - Volume de água tratada em ETAs,
                                     ES002 - Quantidade de ligações ativas de esgotos,
                                     ES006 - Volume de esgotos tratado,
                                     QD002 - Quantidades de paralisações no sistema de distribuição de água,
                                     QD003 - Duração das paralisações]

    path: caminho para o arquivo bruto.
    """

    df = pd.read_excel(
        path, dtype={"Código do Municipio": str, "Ano de Referência": int}
    )

    df = df.assign(
        ano=df["Ano de Referência"],
        id_municipio_6digitos=df["Código do Município"],
        nome_municipio=df["Município"],
        ligacoes_agua=df["AG002 - Quantidade de ligações ativas de água"],
        ligacoes_esgoto=df["ES002 - Quantidade de ligações ativas de esgotos"],
        volume_agua_tratada=df["AG007 - Volume de água tratada em ETAs"],
        volume_esgoto_tratado=df["ES006 - Volume de esgotos tratado"],
        paralisacoes_agua=df[
            "QD002 - Quantidades de paralisações no sistema de distribuição de água"
        ],
        duracao_paralisacao=df["QD003 - Duração das paralisações"],
    )

    df = df[
        [
            "ano",
            "id_municipio_6digitos",
            "nome_municipio",
            "ligacoes_agua",
            "ligacoes_esgoto",
            "volume_agua_tratada",
            "volume_esgoto_tratado",
            "paralisacoes_agua",
            "duracao_paralisacao",
        ]
    ]

    return df


def juntar_bases(
    df_pop,
    df_pib,
    df_mortes,
    df_upas,
    df_samu,
    df_gov,
    df_pref,
    df_saneamento,
    df_mortes_local,
) -> pd.DataFrame:
    """Função que todas as bases."""

    A = pd.merge(
        left=df_mortes,
        right=df_upas,
        how="left",
        on=["periodo", "ano", "id_municipio_6digitos"],
        suffixes=("", "_right"),
    )

    B = pd.merge(
        left=A,
        right=df_samu,
        how="left",
        on=["periodo", "ano", "id_municipio_6digitos"],
        suffixes=("", "_right"),
    )

    C = pd.merge(
        left=B,
        right=df_pop,
        how="left",
        left_on=["id_municipio_6digitos", "ano"],
        right_on=["id_municipio_6digitos", "ano"],
        suffixes=("", "_right"),
    )

    D = pd.merge(
        left=C,
        right=df_pref,
        how="left",
        left_on=["ano", "id_municipio_7digitos", "sigla_uf"],
        right_on=["ano", "id_municipio_7digitos", "sigla_uf"],
        suffixes=("", "_right"),
    )

    E = pd.merge(
        left=D,
        right=df_gov,
        how="left",
        on=["ano", "sigla_uf"],
        suffixes=("", "_y"),
    )

    F = pd.merge(
        left=E,
        right=df_pib,
        how="left",
        on=["ano", "id_municipio_6digitos", "id_municipio_7digitos"],
        suffixes=("", "_y"),
    )

    G = pd.merge(
        left=F,
        right=df_saneamento,
        how="left",
        on=["ano", "id_municipio_6digitos"],
        suffixes=("", "_y"),
    )

    H = pd.merge(
        left=G,
        right=df_mortes_local,
        how="left",
        on=["ano", "id_municipio_6digitos"],
        suffixes=("", "_y"),
    )

    df = H[
        [
            "periodo",
            "ano",
            "id_municipio_6digitos",
            "id_municipio_7digitos",
            "nome_municipio",
            "sigla_partido_pref",
            "sigla_partido_gov",
            "mortes",
            "populacao",
            "upas",
            "samu",
            "pib",
            "ligacoes_agua",
            "ligacoes_esgoto",
            "volume_agua_tratada",
            "volume_esgoto_tratado",
            "paralisacoes_agua",
            "duracao_paralisacao",
            "mortes_hospital",
            "mortes_outro_estab_saude",
            "mortes_domicilio",
            "mortes_via_publica",
            "mortes_outros_locais",
            "mortes_info_ignorada",
        ]
    ]

    df = df.assign(
        upas=df["upas"].fillna(0, downcast="int"),
        samu=df["samu"].fillna(0, downcast="int"),
        ligacoes_agua=df["ligacoes_agua"].fillna(0, downcast="int"),
        ligacoes_esgoto=df["ligacoes_esgoto"].fillna(0, downcast="int"),
        volume_agua_tratada=df["volume_agua_tratada"].fillna(0, downcast="int"),
        volume_esgoto_tratado=df["volume_esgoto_tratado"].fillna(0, downcast="int"),
        paralisacoes_agua=df["paralisacoes_agua"].fillna(0, downcast="int"),
        duracao_paralisacao=df["duracao_paralisacao"].fillna(0, downcast="int"),
        mortes_hospital=df["mortes_hospital"].fillna(0, downcast="int"),
        mortes_outro_estab_saude=df["mortes_outro_estab_saude"].fillna(
            0, downcast="int"
        ),
        mortes_domicilio=df["mortes_domicilio"].fillna(0, downcast="int"),
        mortes_via_publica=df["mortes_via_publica"].fillna(0, downcast="int"),
        mortes_outros_locais=df["mortes_outros_locais"].fillna(0, downcast="int"),
        mortes_info_ignorada=df["mortes_info_ignorada"].fillna(0, downcast="int"),
        sigla_partido_pref=df["sigla_partido_pref"].fillna(method="ffill"),
        sigla_partido_gov=df["sigla_partido_gov"].fillna(method="ffill"),
    )

    df = pd.pivot_table(
        df,
        index=[
            "ano",
            "id_municipio_6digitos",
            "id_municipio_7digitos",
            "nome_municipio",
            "sigla_partido_pref",
            "sigla_partido_gov",
        ],
        aggfunc={
            "mortes": "sum",
            "populacao": "max",
            "upas": "max",
            "samu": "max",
            "pib": "max",
            "ligacoes_agua": "max",
            "ligacoes_esgoto": "max",
            "volume_agua_tratada": "max",
            "volume_esgoto_tratado": "max",
            "paralisacoes_agua": "max",
            "duracao_paralisacao": "max",
            "mortes_hospital": "max",
            "mortes_outro_estab_saude": "max",
            "mortes_domicilio": "max",
            "mortes_via_publica": "max",
            "mortes_outros_locais": "max",
            "mortes_info_ignorada": "max",
        },
    ).reset_index()

    df = df.dropna()

    return df


def criar_variaveis_regressao(df: pd.DataFrame) -> pd.DataFrame:
    """Cria as variáveis no formato utilizado pela regressão dos artigos de referência."""

    df = df.assign(
        obitos_pc=((df["mortes"] / df["populacao"]) * 100000),
        upa_pc=((df["upas"] / df["populacao"]) * 100000),
        pib_pc=((df["pib"] / df["populacao"])),
        partido=list(map(int, (df["sigla_partido_pref"] == df["sigla_partido_gov"]))),
        ligacoes_agua_pc=(df["ligacoes_agua"] / df["populacao"]),
        volume_esgoto_tratado_pc=(df["volume_esgoto_tratado"] / df["populacao"]),
        mortes_hospital_pc=((df["mortes_hospital"] / df["populacao"]) * 100000),
        mortes_outro_estab_saude_pc=(
            (df["mortes_outro_estab_saude"] / df["populacao"]) * 100000
        ),
        mortes_domicilio_pc=((df["mortes_domicilio"] / df["populacao"]) * 100000),
        mortes_via_publica_pc=((df["mortes_via_publica"] / df["populacao"]) * 100000),
        mortes_outros_locais_pc=(
            (df["mortes_outros_locais"] / df["populacao"]) * 100000
        ),
        mortes_info_ignorada_pc=(
            (df["mortes_info_ignorada"] / df["populacao"]) * 100000
        ),
    )

    return df


if __name__ == "__main__":

    df_populacao = populacao_sp("data/raw/populacao-sp.csv")
    df_pib = pib_municipios("data/raw/pib-municipios.csv")
    df_mortes = consolidar_numero_de_mortes_por_ano("data/raw/mortes-por-mes-sp/")
    df_upas = numero_de_upas_por_municipio("data/raw/numero-de-upas.csv")
    df_samu = numero_de_samu_por_municipio("data/raw/numero-de-samu.csv")
    df_gov = bases_politicas("data/raw/partidos-vencedores-governador.csv")
    df_pref = bases_politicas("data/raw/partidos-vencedores-prefeitos.csv", type="pref")
    df_saneamento = base_saneamento("data/raw/saneamento-municipio.xlsx")
    df_mortes_local = consolidar_numero_de_mortes_por_local(
        "data/raw/mortes-por-local-sp/"
    )

    df = juntar_bases(
        df_populacao,
        df_pib,
        df_mortes,
        df_upas,
        df_samu,
        df_gov,
        df_pref,
        df_saneamento,
        df_mortes_local,
    )

    df = criar_variaveis_regressao(df)

    df.to_excel("data/processed/base-regressao.xlsx", index=False)
    print("Base exportada.")
