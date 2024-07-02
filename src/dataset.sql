/*PIB do municipio*/
SELECT ano,
    id_municipio AS id_municipio_7digitos,
    pib
FROM `basedosdados.br_ibge_pib.municipio`
WHERE 1 = 1
    AND ano >= 2010
    AND ano <= 2020
    AND id_municipio IN (
        SELECT DISTINCT id_municipio
        FROM `basedosdados.br_bd_diretorios_brasil.municipio`
        WHERE sigla_uf = 'SP'
    );

/*Populacao*/
SELECT *
FROM `basedosdados.br_ibge_populacao.municipio`
WHERE 1 = 1
    AND ano >= 2010
    AND ano <= 2020
    AND sigla_uf = 'SP';

/*Governadores*/
WITH turno_decisao AS (
    SELECT ano,
        sigla_uf,
        cargo,
        MAX(turno) AS turno_decisao,
        FROM `basedosdados.br_tse_eleicoes.resultados_partido_municipio`
    WHERE 1 = 1
        AND sigla_uf = 'SP'
        AND cargo = 'governador'
        AND ano >= 2006
        AND ano <= 2020
    GROUP BY ano,
        sigla_uf,
        cargo
),
votos_finais AS (
    SELECT t1.ano,
        t1.sigla_uf,
        t1.turno,
        t1.cargo,
        t1.numero_partido,
        t1.sigla_partido,
        SUM(votos_nominais) AS qtd_votos
    FROM `basedosdados.br_tse_eleicoes.resultados_partido_municipio` AS t1
        INNER JOIN turno_decisao AS t2 ON t1.ano = t2.ano
        AND t1.sigla_uf = t2.sigla_uf
        AND t1.turno = t2.turno_decisao
        AND t1.cargo = t2.cargo
    GROUP BY ano,
        sigla_uf,
        turno,
        cargo,
        numero_partido,
        sigla_partido
),
votos_vencedor AS (
    SELECT ano,
        cargo,
        max(qtd_votos) AS votos_vencedor
    FROM votos_finais
    GROUP BY ano,
        cargo
)
SELECT vf.ano,
    vf.sigla_uf,
    vf.cargo,
    vf.sigla_partido
FROM votos_finais as vf
    INNER JOIN votos_vencedor AS vv ON vf.ano = vv.ano
    AND vf.cargo = vv.cargo
    AND vf.qtd_votos = vv.votos_vencedor;

/*Prefeitos*/
WITH turno_decisao AS (
    SELECT ano,
        id_municipio,
        cargo,
        MAX(turno) AS turno_decisao,
        FROM `basedosdados.br_tse_eleicoes.resultados_partido_municipio`
    WHERE 1 = 1
        AND sigla_uf = 'SP'
        AND cargo = 'prefeito'
        AND ano >= 2006
        AND ano <= 2020
    GROUP BY ano,
        id_municipio,
        cargo
),
votos_finais AS (
    SELECT t1.ano,
        t1.id_municipio,
        t1.sigla_uf,
        t1.turno,
        t1.cargo,
        t1.numero_partido,
        t1.sigla_partido,
        SUM(t1.votos_nominais) AS qtd_votos
    FROM `basedosdados.br_tse_eleicoes.resultados_partido_municipio` AS t1
        INNER JOIN turno_decisao AS t2 ON t1.ano = t2.ano
        AND t1.id_municipio = t2.id_municipio
        AND t1.turno = t2.turno_decisao
        AND t1.cargo = t2.cargo
    GROUP BY ano,
        id_municipio,
        sigla_uf,
        turno,
        cargo,
        numero_partido,
        sigla_partido
),
votos_vencedor AS (
    SELECT ano,
        id_municipio,
        cargo,
        max(qtd_votos) AS votos_vencedor
    FROM votos_finais
    GROUP BY ano,
        id_municipio,
        cargo
)
SELECT vf.ano,
    vf.id_municipio,
    vf.sigla_uf,
    vf.cargo,
    vf.sigla_partido
FROM votos_finais as vf
    INNER JOIN votos_vencedor AS vv ON vf.ano = vv.ano
    AND vf.id_municipio = vv.id_municipio
    AND vf.cargo = vv.cargo
    AND vf.qtd_votos = vv.votos_vencedor;