import numpy as np
import pandas as pd


def resultados():

    df = pd.DataFrame(
        np.stack(
            [
                ["-3,027***", "6.389", "0,134", "645", "Não", "Sim", "-", "-"],
                ["-0,894", "6.389", "0,007", "645", "Sim", "Sim", "4,8951", "9,4999"],
                ["-0,719", "6.389", "0,006", "645", "Sim", "Não", "-", "-"],
                ["-0,827", "6.389", "0,013", "645", "Sim", "Sim", "-", "-"],
                ["-0,633*", "6.389", "0,011", "645", "Sim", "Sim", "-", "-"],
                ["-0,261", "6.389", "0,032", "645", "Sim", "Sim", "-", "-"],
                ["-1,000***", "6.389", "0,011", "645", "Sim", "Sim", "-", "-"],
                ["0,992***", "6.389", "0,031", "645", "Sim", "Sim", "-", "-"],
            ],
            axis=1,
        ),
        index=[
            "UPA per capita",
            "Observações",
            "R^2",
            "Número de Municípios",
            "Efeitos Fixos",
            "Controles",
            "Teste de Hausman",
            "Teste de Breusch-Pagan",
        ],
        columns=pd.MultiIndex.from_tuples(
            [
                (
                    "Variável dependente: taxa de mortalidade (óbitos/população) * 100.000",
                    "Total",
                    "MQO (pooling) (1)",
                ),
                (
                    "Variável dependente: taxa de mortalidade (óbitos/população) * 100.000",
                    "Total",
                    "Efeitos Aleatórios (2)",
                ),
                (
                    "Variável dependente: taxa de mortalidade (óbitos/população) * 100.000",
                    "Total",
                    "Efeitos Fixos (LSDV) (3)",
                ),
                (
                    "Variável dependente: taxa de mortalidade (óbitos/população) * 100.000",
                    "Total",
                    "Efeitos Fixos (LSDV) (4)",
                ),
                (
                    "Variável dependente: taxa de mortalidade (óbitos/população) * 100.000",
                    "Em casa",
                    "Efeitos Fixos (LSDV) (5)",
                ),
                (
                    "Variável dependente: taxa de mortalidade (óbitos/população) * 100.000",
                    "Na rua",
                    "Efeitos Fixos (LSDV) (6)",
                ),
                (
                    "Variável dependente: taxa de mortalidade (óbitos/população) * 100.000",
                    "No hospital",
                    "Efeitos Fixos (LSDV) (7)",
                ),
                (
                    "Variável dependente: taxa de mortalidade (óbitos/população) * 100.000",
                    "UPA e outros",
                    "Efeitos Fixos (LSDV) (8)",
                ),
            ]
        ),
    )

    return df


if __name__ == "__main__":
    pass
