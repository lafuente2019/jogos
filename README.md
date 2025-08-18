# Monitor de Marcas

## Tabela de conteúdo

- [Cliente](#cliente)
- [Parceiro](#parceiro)
- [Fontes de dados](#fontes-de-dados)
- [Descrição](#descrição)
- [Tipos de arquivos disponibilizados](#tipos-de-arquivos-disponibilizados)
- [Categorias de Pesquisas Kantar](#categorias-de-pesquisas-kantar)
  - [Categorias](#categorias)
- [Masterbrand](#masterbrand)
  - [Frequência de realização do Questionário](#frequência-de-realização-do-questionário)
  - [Frequência de envio dos arquivos Proprietários](#frequência-de-envio-dos-arquivos-proprietários)
  - [Marcas abordadas](#marcas-abordadas)
  - [Indicadores Proprietários Kantar](#indicadores-proprietários-kantar)
  - [Indicadores extraídos do Questionário](#indicadores-extraídos-do-questionário)
  - [Filtros extraídos do Questionário](#filtros-extraídos-do-questionário)
- [Arquitetura de Automação e Execução](#arquitetura-de-automação-e-execução)
  - [Lógica de execução](#lógica-de-execução)
  - [Nomenclatura dos recursos utilizados](#nomenclatura-dos-recursos-utilizados)
- [Dataproc Workflow Templates](#dataproc-workflow-templates)
  - [Workflow: questionario](#workflow-au029-marcas-masterbrand-questionario)
  - [Workflow: proprietarios](#workflow-au029-marcas-masterbrand-proprietarios)
- [Validação e Registro de Erros](#validação-e-registro-de-erros)
- [Arquitetura](#arquitetura)
- [Persistência](#persistência)
- [Indicadores do Questionário e Regras de Negócio](#indicadores-do-questionário-e-regras-de-negócio)
  - [Afinidade](#afinidade)
  - [Atende às Necessidades](#atende-às-necessidades)
  - [Confiança](#confiança)
  - [Consideração](#consideração)
  - [Diferente](#diferente)
  - [Dita Tendências](#dita-tendências)
  - [Familiaridade](#familiaridade)
  - [Imagem](#imagem-associação-absoluta)
  - [NPS](#nps)
  - [Preferência](#preferência)
  - [Fatores de Escolha](#fatores-de-escolha)
  - [Preço Percebido](#preço-percebido)
  - [Vale à Pena](#vale-à-pena)
- [Indicadores Proprietários Kantar](#indicadores-proprietários-kantar)
  - [Power e Dimensões](#power-e-dimensões)
  - [Premium](#premium)
  - [Contriubuição das Dimensões para o Power](#contriubuição-das-dimensões-para-o-power)
  - [BIP](#bip)
  - [Agrupamentos de Atributos BIP e Contribuição para o Power](#agrupamentos-de-atributos-bip-e-contribuição-para-o-power)
  - [Barreiras e Facilitadores](#barreiras-e-facilitadores)
  - [Média de Mercado do NPS para Conhecedores e Consumidores](#média-de-mercado-do-nps-para-conhecedores-e-consumidores)
- [Indicadores de Respostas Espontâneas](#indicadores-de-respostas-espontâneas)
- [Filtros](#filtros)
  - [Filtros Demográficos](#filtros-demográficos)
  - [Assinantes por plataforma](#assinantes-por-plataforma)
- [Dashboard](#dashboard)
  - [Indicadores Contemplados](#indicadores-contemplados)
  - [Estrutura](#estrutura)
  - [Métricas](#métricas)
  - [Granularidade de visualização](#granularidade-de-visualização)
  - [Filtros do dashboard](#filtros-do-dashboard)
- [Arquivo Power BI - Monitor de Marcas](#arquivo-power-bi---monitor-de-marcas)
  - [Agendamento de carga](#agendamento-de-carga)
  - [Como gerar embed dos dashboards](#gerando-link-para-embed-dos-dashboards-do-monitor-de-marcas)
  - [Filtros de período](#filtros-de-período)
- [Solução dos filtros de período para os Indicadores não proprietários](#solucao-dos-filtros-de-periodo-para-os-indicadores-nao-proprietarios)
- [Solução de período para Matrizes das páginas “Multi Period tabela”](#solucao-de-periodo-para-matrizes-das-paginas-multi-period-tabela)
  - [Fórmulas DAX - Indicador "Diferente"](#fórmulas-dax---indicador-diferente)
  - [Query: tb_filtro_trimestral_nao_proprietario](#query-tb_filtro_trimestral_nao_proprietario)
  - [Query: tb_filtro_semestral_nao_proprietario](#query-tb_filtro_semestral_nao_proprietario)
- [Dashboards Amor à Marca](#dashboards-amor-à-marca)
  - [Fórmulas Dax Amor á Marca](#fórmulas-dax-amor-á-marca)
- [Dashboards Atende às Necessidades](#dashboards-atende-às-necessidades)
  - [Fórmulas Dax Atende às necessidades](#fórmulas-dax-atende-às-necessidades)
- [Dashboards Confiança](#dashboards-confiança)
  - [Fórmulas Dax Confiança](#fórmulas-dax-confiança)
- [Dashboards Consideração](#dashboards-consideração)
  - [Fórmulas Dax Consideração](#fórmulas-dax-consideração)
- [Dashboards Diferente](#dashboards-diferente)
  - [Formulas Dax Diferente](#fórmulas-dax-diferente)
- [Dashboards Dita Tendências](#dashboards-dita-tendências)
  - [Fórmulas Dax Dita Tendências](#fórmulas-dax-dita-tendências)
- [Dashboards NPS](#dashboards-nps)
  - [Fórmulas Dax NPS](#fórmulas-dax-nps)
- [Dashboards Power e dimensões](#dashboards-power-e-dimensões)
  - [Fórmulas Dax Power e dimensões](#fórmulas-dax-power-e-dimensões)
- [Dashboards Contribuição das Dimensões para o Power](#dashboards-contribuição-das-dimensões-para-o-power)
  - [Fórmulas DAX Contribuição das Dimensões para o Power](#fórmulas-dax-contribuição-das-dimensões-para-o-power)
- [Dashboards BIP - Brand Image Profile](#dashboards-bip---brand-image-profile)
- [Dashboards Agrupamentos de Atributos BIP e Contribuição para o Power](#dashboards-agrupamentos-de-atributos-bip-e-contribuição-para-o-power)
- [Links e referências](#links-e-referências)


| Modificado por | Data       |
| :------------- | :--------- |
| Pedro Sales    | 10/10/2024 |
| Valter Lafuente   | 18/07/2025 |

## Cliente

Time de PESQUISA E CONHECIMENTO

Pontos focais:

- Raissa Paes, raissa.paes@g.globo
- Rafael Gussi, rafael.gussi@g.globo
- Glaucia Ferreira, glaucia.ferreira@g.globo

## Parceiro

Time de SOLUÇÕES DE MARCA, COMUNICAÇÃO E AUDIÊNCIA

Pontos focais:

- Roberto Roulin, roberto.moulin@g.globo
- Fernando Albino, fernando.albino@g.globo
- Tauan Jancso, tauan.jancso_stormgroup@prestador.globo

## Fontes de dados

Arquivos disponibilizados pelo time cliente em página do Sharepoint: [Sharepoint Monitor de Marcas](https://tvglobocorp.sharepoint.com/sites/solucoes_analiticas/monitor_marca/Forms/AllItems.aspx)

- Questionários de pesquisas Kantar preenchidos por pessoas físicas:
  Arquivos SPSS (formato .sav)
- Métricas geradas por cálculos proprietários Kantar: Arquivos Excel

## Descrição

Processo com o objetivo de automatizar a geração de métricas e visualizações de KPIs de Marcas para disponibilização para o time cliente, visando a evolução da solução integrada de Saúde de Marcas.

Os KPIs são obtidos através de pesquisas feitas com a sociedade, encomendadas com a Kantar, para entender a percepção com relação à marca Globo das pessoas que consomem nosso conteúdo, como nos avaliam e comparam a outras marcas, e que ações podemos tomar para melhorar.

Os arquivos referentes aos resultados dessas pesquisas, disponibilizados no Sharepoint, são processados em ambiente Google Cloud, gerando tabelas no BigQuery para cada um dos indicadores e filtros requisitados.

Essas tabelas são utilizadas para construção de dashboards no PowerBI referentes às métricas e cruzamentos de dados desejados, que são incorporados na aplicação desenvolvida pelo time parceiro, acessada pelo time cliente.

## Tipos de arquivos disponibilizados

Os arquivos disponibilizados pelo time cliente se enquadram em dois tipos distintos:

- Dados brutos de respostas de pessoas físicas a questionários formulados pela Kantar, a partir dos quais são extraídos uma série de indicadores e filtros conforme as regras de negócio passadas.
- Dados de indicadores/métricas específicos cuja fórmula de cálculo é propriedade da Kantar e são entregues já calculadas.

## Categorias de Pesquisas Kantar

Ambos os tipos de arquivos recebidos correspondem a formulários de pesquisa acordados com a Kantar, que se enquadram em 8 categorias, iniciados em Agosto de 2022 mas variando quanto às perguntas realizadas, frequência de realização do questionário e marcas abordadas.

### Categorias

- Masterbrand
- Novelas
- Jornalismo
- Streaming
- Filmes e Séries
- Esportes
- Infantil
- Variedades

## Masterbrand

Para a categoria de **Masterbrand**, temos:

### Frequência de realização do Questionário

- Relatório pontual inicial em Ago/2022 (considerado como Jul/2022 para fins de análise dos dados)
- Relatório pontual referente ao período Ago-Out/2022
- Relatórios pontuais em Nov/2022 e Dez/2022
- Relatórios trimestrais a partir de Jan/2023

### Frequência de envio dos arquivos Proprietários

- Envios trimestrais para 2 indicadores
- Envios semestrais para 5 indicadores

### Marcas abordadas

- Globo
- Netflix
- UOL
- Discovery
- Facebook
- Apple
- Twitter
- Amazon
- Spotify
- SBT
- Youtube
- HBO
- Record
- Google
- TikTok
- Disney
- Instagram

### Indicadores Proprietários Kantar

- Power, Premium e Dimensões (semestral)
- Contriubuição das Dimensões para o Power (semestral)
- BIP (trimestral e semestral)
- Agrupamentos de Atributos BIP e Contribuição para o Power (semestral)
- Barreiras e Facilitadores (semestral)
- Média de Mercado do NPS para Conhecedores e Consumidores (trimestral)
- NPS para Conhecedores e Consumidores, Mensal e Acumulado (mensal)

### Indicadores extraídos do Questionário

- Afinidade
- Atende às Necessidades
- Confiança
- Consideração
- Diferente
- Dita Tendências
- Familiaridade
- Imagem (associação absoluta)
- NPS
- Preferência
- Fatores de Escolha
- Preço Percebido
- Vale à Pena

### Filtros extraídos do Questionário

- Familiaridade
- NPS
- Sexo
- Faixa Etária
- Classe Social
- Região
- Assinantes por Plataforma

## Arquitetura de Automação e Execução

A arquitetura de automação e execução do processo consiste em **um fluxo unificado com ramificação lógica** para: `questionario`, `proprietarios` e `nps_mensal`.

Para a categoria **Masterbrand**, o processamento é realizado com base no projeto:

- `au029-marcas-masterbrand`

O fluxo é executado no ambiente **Google Cloud**, no projeto `gglobo-audiencia-hdg-prd`, com dois **Cloud Schedulers** distintos como gatilhos. Cada um dispara uma **Cloud Function única**, mas com parâmetros específicos:

- `"TIPO_PROCESSAMENTO": "QUESTIONARIO"`  
- `"TIPO_PROCESSAMENTO": "PROPRIETARIOS"`  
- `"TIPO_PROCESSAMENTO": "NPS_MENSAL"`

Todos são agendados para execução diária às **8h (BRT)**, mas a lógica interna da **Cloud Function** garante o processamento apenas quando há novos arquivos disponíveis, respeitando a periodicidade de cada tipo de dado.

### Lógica de execução:

1. Disparo agendado do **Cloud Scheduler**, com payload indicando o tipo de processamento (`TIPO_PROCESSAMENTO`)  
2. A **Cloud Function** executa de forma **independente para cada tipo de dado**, processando apenas o tipo especificado no payload (`questionario`, `proprietarios` e `nps_mensal`)  
3. A função autentica no SharePoint e verifica a existência de arquivos novos na pasta correspondente  
4. Os arquivos identificados como novos são salvos no **bucket LND** do Cloud Storage  
5. A função realiza a **detecção do tipo de período** (trimestral, semestral ou mensal) com base no nome do arquivo  
6. Para arquivos do tipo `proprietarios`, é realizada a **validação das abas obrigatórias** do Excel.  
   - Caso alguma aba esperada esteja ausente, o processo é **interrompido com erro** e um **e-mail é enviado** com as divergências encontradas  
7. A função gera um **arquivo auxiliar** no bucket de processamento com a lista de arquivos válidos a serem processados  
8. A **Cloud Function** dispara o **Workflow do Dataproc**, definindo os steps de execução com base no tipo informado  
9. O **Dataproc** lê o arquivo de controle com a lista de arquivos  
10. O **Dataproc** processa os arquivos localizados no bucket **LND**  
11. Os dados brutos são armazenados no bucket da camada **RAW**  
12. Cada indicador é persistido em tabelas específicas no **BigQuery**, na camada **PREP**


### Nomenclatura dos recursos utilizados:

- **Cloud Scheduler**: `[SOLUCAO]-extract-sharepoint-cloudfunction`
- **Cloud Function**: `[SOLUCAO]-extract-sharepoint`
- **Dataproc Workflow Template**: `[SOLUCAO]-[TIPO]`
- **Buckets (Cloud Storage)**:
  - Camada **LND**: `[SOLUCAO]-lnd-fb23a`
  - Camada **RAW**: `[SOLUCAO]-raw-fb23a`
  - Bucket auxiliar: `[SOLUCAO]-dados-para-processamento`
- **Datasets (BigQuery)**:
  - Camada **RAW**: `raw_monitor_marcas_[CATEGORIA]`
  - Camada **PREP**: `prep_monitor_marcas_[CATEGORIA]`

## Dataproc Workflow Templates

### Workflow: `au029-marcas-masterbrand-questionario`

**Etapas:**

- `load-questionario`  
  ➤ Esta etapa inclui uma **validação automática do arquivo da Kantar**, garantindo que ele esteja no formato e com o conteúdo esperado.  
  ➤ Caso o arquivo esteja com **divergências**, o processo é **interrompido com erro** e um **e-mail é enviado** com os detalhes das inconsistências encontradas.
- `transform-questionario-afinidade`
- `transform-questionario-diferente`
- `transform-questionario-dita-tendencias`
- `transform-questionario-necessidades`
- `transform-questionario-imagem`
- `transform-questionario-preferencia`
- `transform-questionario-confianca`
- `transform-questionario-familiaridade`
- `transform-questionario-consideracao`
- `transform-questionario-nps`
- `transform-questionario-filtro-demografico`
- `transform-questionario-filtro-consumo-meios`

---

### Workflow: `au029-marcas-masterbrand-proprietarios`

**Etapas:**

- `load-metricas-bip`
- `load-metricas-peso-atributos`
- `load-metricas-facilitadores`
- `load-metricas-nps-mercado`
- `load-metricas-contribuicao-power`
- `load-metricas-premium`
- `load-metricas-power-dimensoes`

---

### Workflow: `au029-marcas-masterbrand-nps-mensal`

**Etapas:**

- `load-nps-mansal`
- `load-nps-acumulado`


Onde:

- [SOLUCAO] -> Nome do fluxo específico do processo. (au029-marcas-masterbrand)
- [CATEGORIA] -> Nome da categoria. (masterbrand)
- [TIPO] -> Processamento a ser executado (`questionario`, `proprietarios` e `nps_mensal`).

---

## Validação e Registro de Erros

Durante o processamento dos arquivos de questionário no Dataproc, o sistema executa validações automáticas para garantir a integridade e conformidade dos dados.

### Etapas com validação:

- `load-questionario`

### Tipos de validação realizados:

1. **Respostas inválidas** (não previstas na estrutura de homologação)
2. **Mesmo código com labels diferentes**
3. **Mesmo label com códigos diferentes**

### Registro de erros:

Quando qualquer uma dessas validações identifica inconsistências, os dados com erro são automaticamente registrados na seguinte tabela de log: **`gglobo-audiencia-hdg-prd.raw_monitor_marcas_governanca.tb_validacao_erros_kantar`**




### Campos registrados:

| Campo                 | Tipo     | Descrição                                                                 |
|----------------------|----------|---------------------------------------------------------------------------|
| arquivo_nome          | STRING   | Nome do arquivo processado                                                |
| data_validacao        | DATE     | Data em que a validação foi realizada                                     |
| tipo_erro             | STRING   | Tipo do erro encontrado                                                   |
| codigo_pergunta       | STRING   | Código da pergunta (se aplicável)                                         |
| respostas_homologadas | STRING   | Lista de respostas válidas esperadas                                      |
| resposta_encontrada   | STRING   | Resposta encontrada no arquivo                                            |
| label_homologado      | STRING   | Label esperado (homologado)                                               |
| label_encontrado      | STRING   | Label encontrado durante a validação                                      |
| codigo_encontrado     | STRING   | Código encontrado (quando diferente do homologado)                        |

---
## Arquitetura
![Arquitetura](documentacao/monitor_marcas-Arquitetura_MD.drawio.png)

### Persistência

A persistência dos dados também segue o mesmo princípio da arquitetura do processo, consistindo em ambientes separados para cada uma das categorias existentes.

- Os dados extraídos do sharepoint são armazenados sem alteração no Cloud Storage no bucket da camada LND.
- O arquivo do questionário no bucket LND passa por um processamento inicial para poder ser lido de forma tabular, e esse resultado é armazenado no Cloud Storage no formato Parquet, no respectivo bucket da camada RAW do fluxo.
- Os dados de questionário tabular no bucket da camada RAW também podem ser acessados através de uma tabela externa do BigQuery, que se encontra no respectivo dataset da camada RAW.
- Os dados do questionário tabular na camada RAW são processados para extração dos indicadores e filtros de interesse, e cada um deles é salvo em uma tabela nativa BigQuery individual no dataset da camada PREP
- Os dados de indicadories proprietários Kantar no bucket LND são processados separadamente e vão direto para as respetivas tabelas nativas BigQuery no dataset da camada PREP, cada um tendo a sua tabela individual.

![Persistência](documentacao/monitor_marcas-Persistencia.drawio.png)

## Indicadores do Questionário e Regras de Negócio

A partir das perguntas dos questionários realizados, são extraídos uma série de indicadores conforme regras de negócio estabelecidas pelo time cliente.

A maior parte desses indicadores corresponde a perguntas do questionário nas quais o respondente seleciona uma ou mais respostas de uma lista de opções já definidas, e cujas regras de negócio aplicadas podem ser compartilhadas e reproduzidas internamente.

### Afinidade

Nomes alternativos: "Amor à Marca".

Tabela no BigQuery: "tb_afinidade"

Representa a percepção da população do quanto tem afinidade pela marca em questão, numa escala que vai de -3 a +3 conforme o critério:

- -3 -> "Eu odeio"
- 0 -> "Neutro"
- +3 -> "Eu amo"

Além das opções possíveis nessa escala, também é feita a classificação das respostas em outras categorias:

- "TOP2BOX" -> Corresponde a indivíduos que marcaram as opções 2 ou 3.
- "TOP2BOTTOM" -> Corresponde a indivíduos que marcaram as opções -3 ou -2.

Identificação da pergunta respectiva no questionário:

- Código -> "BE6"
- Texto -> "Como você se sente com relação a cada marca?"

Regra para identificação no arquivo SPSS:

- Código da pergunta começa com "BE6_BRAND"

### Atende às Necessidades

Nomes alternativos: "Atende as minhas necessidades", "Necessidades".

Tabela no BigQuery: "tb_necessidades"

Representa a percepção da população do quanto a marca atende suas necessidades de entretenimento e informação, numa escala que vai de 1 a 7 conforme o critério:

- 1 -> "Não atende nenhuma das minhas necessidades"
- 7 -> "Atende muito bem as minhas necessidades"

Além das opções possíveis nessa escala, também é feita a classificação das respostas em outras categorias:

- "TOP2BOX" -> Corresponde a indivíduos que marcaram as opções 6 ou 7.
- "TOP2BOTTOM" -> Corresponde a indivíduos que marcaram as opções 1 ou 2.

Identificação da pergunta respectiva no questionário:

- Código -> "BP2"
- Texto -> "Arraste cada uma das marcas para a escala que indica o quanto cada marca atende as suas necessidades com relação a [TEXTO ESPECÍFICO POR CATEGORIA]."

Regra para identificação no arquivo SPSS:

- Código da pergunta começa com "BP2_BRAND"

### Confiança

Tabela no BigQuery: "tb_confianca"

Representa a percepção da população do quanto confia na marca, numa escala que vai de 1 a 7 conforme o critério:

- 1 -> "Não confio nada"
- 7 -> "Confio totalmente"

Além das opções possíveis nessa escala, também é feita a classificação das respostas em outras categorias:

- "TOP2BOX" -> Corresponde a indivíduos que marcaram as opções 6 ou 7.
- "TOP2BOTTOM" -> Corresponde a indivíduos que marcaram as opções 1 ou 2.
- "Confio totalmente" -> Corresponde a indivíduos que marcaram a opção 7.
- "Neutro" -> Corresponde a indivíduos que marcaram as opções 3, 4, 5 ou 6.
- "Não confio em nada" -> Corresponde a indivíduos que marcaram as opções 1 ou 2.

Identificação da pergunta respectiva no questionário:

- Código -> "CONFIANCA"
- Texto -> "Arraste cada marca para a escala abaixo para indicar o quanto você confia nela."

Regra para identificação no arquivo SPSS:

- Código da pergunta começa com "CONFIANCA_BRAND"

### Consideração

Tabela no BigQuery: "tb_consideracao"

Representa a percepção da população do quanto consideraria escolher a marca para consumo de entretenimento e informação, numa escala que vai de 1 a 4 conforme o critério:

- 1 -> "Seria a minha primeira escolha"
- 2 -> "Eu consideraria seriamente"
- 3 -> "Eu poderia considerar"
- 4 -> "Eu não consideraria"

Além das opções possíveis nessa escala, também é feita a classificação das respostas em outras categorias:

- "TOP2BOX" -> Corresponde a indivíduos que marcaram as opções 1 ou 2.
- "TOP2BOTTOM" -> Corresponde a indivíduos que marcaram as opções 3 ou 4.

Identificação da pergunta respectiva no questionário:

- Código -> "BE3"
- Texto -> "Qual a probabilidade de você escolher cada uma das seguintes marcas na sua próxima ESCOLHA de [TEXTO ESPECÍFICO POR CATEGORIA]?"

Regra para identificação no arquivo SPSS:

- Código da pergunta começa com "BE3_BRAND"

### Diferente

Nomes alternativos: "Única".

Tabela no BigQuery: "tb_diferente"

Representa a percepção da população do quanto a marca em questão difere das demais, numa escala que vai de 1 a 7 conforme o critério:

- 1 -> "Exatamente a mesma coisa"
- 7 -> "Muito Diferente"

Além das opções possíveis nessa escala, também é feita a classificação das respostas em outras categorias:

- "TOP2BOX" -> Corresponde a indivíduos que marcaram as opções 6 ou 7.
- "TOP2BOTTOM" -> Corresponde a indivíduos que marcaram as opções 1 ou 2.

Identificação da pergunta respectiva no questionário:

- Código -> "BP1"
- Texto -> "Por favor arraste cada marca para o ponto da escala que melhor indica o quanto ela parece ser diferente das outras marcas de [TEXTO ESPECÍFICO POR CATEGORIA]."

Regra para identificação no arquivo SPSS:

- Código da pergunta começa com "BP1_BRAND"

### Dita Tendências

Nomes alternativos: "Dita/Lança tendências", "Dinâmica", "Dinamismo".

Tabela no BigQuery: "tb_dita_tendencias"

Representa a percepção da população do quanto a marca em questão é responsável por lançar novas tendências em comparação com as demais, numa escala que vai de 1 a 7 conforme o critério:

- 1 -> "Segue/copia as outras"
- 7 -> "Dita/lança tendências"

Além das opções possíveis nessa escala, também é feita a classificação das respostas em outras categorias:

- "TOP2BOX" -> Corresponde a indivíduos que marcaram as opções 6 ou 7.
- "TOP2BOTTOM" -> Corresponde a indivíduos que marcaram as opções 1 ou 2.

Identificação da pergunta respectiva no questionário:

- Código -> "BP3"
- Texto -> "Arraste cada marca para a escala abaixo para indicar o quanto ela dita ou lança tendências."

Regra para identificação no arquivo SPSS:

- Código da pergunta começa com "BP3_BRAND"

### Familiaridade

Nomes alternativos: "Funil de familiaridade", filtro "Consumidor".

Tabela no BigQuery: "tb_familiaridade"

Representa a percepção da população do quanto está familiarizada com a marca em questão, numa escala que vai de 1 a 6 conforme o critério:

- 1 -> "É a marca que eu consumo com maior frequência"
- 2 -> "É uma marca que eu consumo regularmente"
- 3 -> "Eu já consumi"
- 4 -> "Já vi ou ouvi falar muito nela, mas nunca consumi"
- 5 -> "Já vi ou ouvi falar um pouco nela, mas nunca consumi"
- 6 -> "Até hoje, nunca tinha visto ou ouvido falar nesta marca"

Além das opções possíveis nessa escala, também é feita a classificação das respostas em outras categorias:

- "Conhecedores" -> Corresponde a indivíduos que marcaram as opções 1, 2, 3, 4 ou 5.
- "Não Conhecedores" -> Corresponde a indivíduos que marcaram a opção 6.
- "Consumidores" -> Corresponde a indivíduos que marcaram as opções 1 ou 2.
- "Não Consumidores" -> Corresponde a indivíduos que marcaram as opções 4, 5 ou 6.
- "Consumidores Frequentes" -> Corresponde a indivíduos que marcaram a opção 1.
- "Consumidores Regulares" -> Corresponde a indivíduos que marcaram a opção 2.
- "Já Consumiu" -> Corresponde a indivíduos que marcaram as opções 1, 2 ou 3.
- "Abandonadores" -> Corresponde a indivíduos que marcaram a opção 3.
- "Conhecedores Não Consumidores" -> Corresponde a indivíduos que marcaram as opções 4 ou 5.

Identificação da pergunta respectiva no questionário:

- Código -> "BE2A"
- Texto -> "O quanto você está familiarizado(a) com cada uma destas marcas de entretenimento e informação?"

Regra para identificação no arquivo SPSS:

- Código da pergunta começa com "BE2A_BRAND"

### Imagem (associação absoluta)

Nomes alternativos: "Imagem (%)", "Atributos de Imagem".

Tabela no BigQuery: "tb_imagem"

Representa a percepção da população sobre a visão que se tem da marca em questão, partindo de um grupo de opções de frases para as quais o respondente assinala que é relevante ("Sim") ou deixa a opção em branco ("Não"):

- "É uma marca que faz parte do meu dia a dia" (1)
- "É uma marca que é interativa com seu público" (2)
- "É uma marca que me permite aprender coisas novas" (3)
- "É uma marca que desperta emoções" (4)
- "É uma marca que conta boas histórias" (5)
- "É uma marca que está sempre lançando novidades" (6)
- "É uma marca que tem variedade que atende a diferentes gostos" (7)
- "É uma marca que entende profundamente o Brasil e os brasileiros" (8)
- "É uma marca que tem um time de profissionais diverso" (9)
- "É uma marca que é inspiração para outras marcas" (10)
- "É uma marca que está ao lado da população brasileira" (11)
- "É uma marca que investe para construir um futuro melhor" (12)

Essas opções de seleção também são classificadas em categorias conforme o seguinte critério:

- "Dia a dia/Aprendizado" -> Opções 1 e 3.
- "Conexão emocional" -> Opções 4 e 5.
- "Inspiração/Novidade" -> Opções 6 e 10.
- "Interatividade" -> Opção 2.
- "Variedade" -> Opções 7 e 9.
- "Brasilidade" -> Opções 8 e 11.
- "Futuro melhor" -> Opção 12.

Identificação da pergunta respectiva no questionário:

- Código -> "BD11"
- Texto -> "Pensando em marcas de [TEXTO ESPECÍFICO POR CATEGORIA], qual destas marcas acha que...? Selecione todas que se aplicam."

Regra para identificação no arquivo SPSS:

- Código da pergunta começa com "BD11\_" seguido de um dígito numérico

### NPS

Nomes alternativos: "Recomendação".

Tabela no BigQuery: "tb_nps"

Representa a percepção da população sobre o quanto recomendariam a marca em questão para amigos e parentes, numa escala que vai de 0 a 10 conforme o critério:

- 0 -> "Nada provável"
- 10 -> "Muito provável"

Além das opções possíveis nessa escala, também é feita a classificação das respostas em outras categorias:

- "Detratores" -> Corresponde a indivíduos que marcaram as opções 0, 1, 2, 3, 4, 5 ou 6.
- "Neutros" -> Corresponde a indivíduos que marcaram as opções 7 ou 8.
- "Promotores" -> Corresponde a indivíduos que marcaram as opções 9 ou 10.

Identificação da pergunta respectiva no questionário:

- Código -> "NPS"
- Texto -> "Qual a probabilidade de você recomendar estas marcas para amigos ou parentes?"

Regra para identificação no arquivo SPSS:

- Código da pergunta começa com "NPS_BRAND"

### Preferência

Tabela no BigQuery: "tb_preferencia"

Representa o posicionamento da população quanto à sua marca de preferência dentre as abordadas no questionário.

Identificação da pergunta respectiva no questionário:

- Código -> "PREF"
- Texto -> "Pensando nas marcas de [TEXTO ESPECÍFICO POR CATEGORIA], qual sua marca preferida?"

Regra para identificação no arquivo SPSS:

- Código da pergunta é igual a "PREF"

### Fatores de Escolha

_Ainda não contemplado pelo dashboard._

Nomes alternativos: "Barreiras e facilitadores de mercado (associação absoluta)".

Representa a percepção da população sobre quais fatores influenciam na escolha da marca em questão, partindo de um grupo de opções de frases para as quais o respondente deve assinalar que é relevante ("Sim") ou deixar a opção em branco ("Não"):

- "Tem o melhor conteúdo para mim"
- "Tem o preço que eu estava disposto(a) a pagar"
- "Estava com preço promocional"
- "Vi um anúncio/ comercial"
- "Tem uma linguagem fácil de entender"
- "Oferece conteúdo sem anúncios/ sem propagandas"
- "É fácil de acessar"
- "Oferece a melhor experiência de uso"
- "Não consumi recentemente"
- "Nenhuma destas"
- "Não sei"

Identificação da pergunta respectiva no questionário:

- Código -> "ACT1"
- Texto -> "Quais frases abaixo descrevem fatores que influenciaram você na escolha das marcas de entretenimento e informação?"

Regra para identificação no arquivo SPSS:

- Código da pergunta começa com "ACT1_BRAND"

### Preço Percebido

_Ainda não contemplado pelo dashboard._

Nomes alternativos: "Preço".

Representa a percepção da população do quanto ao preço da marca em questão com em comparação com as demais, numa escala que vai de 1 a 7 conforme o critério:

- 1 -> "Tem/teria o preço mais baixo"
- 7 -> "Tem/teria o preço mais alto"

Além das opções possíveis nessa escala, também é feita a classificação das respostas em outras categorias:

- "TOP2BOX" -> Corresponde a indivíduos que marcaram as opções 6 ou 7.
- "TOP2BOTTOM" -> Corresponde a indivíduos que marcaram as opções 1 ou 2.

Identificação da pergunta respectiva no questionário:

- Código -> "BP5"
- Texto -> "Destas marcas, algumas são pagas e outras gratuitas. Para esta pergunta, imagine que as gratuitas teriam um preço, ou seja, seriam pagas. Arraste cada marca para a escala para expressar sua opinião sobre o preço de cada uma delas."

Regra para identificação no arquivo SPSS:

- Código da pergunta começa com "BP5_BRAND"

### Vale à Pena

_Ainda não contemplado pelo dashboard._

Representa a percepção da população do quanto consideram que a marca em questão vale em comparação com as demais, numa escala que vai de 1 a 3 conforme o critério:

- 1 -> "Vale menos que outras marcas"
- 2 -> "Vale o mesmo que outras marcas"
- 3 -> "Vale mais que outras marcas"

Identificação da pergunta respectiva no questionário:

- Código -> "BP6"
- Texto -> "Considerando o VALOR que essa empresa/marca entrega para você na categoria de entretenimento, quanto você acha que essa marca vale?"

Regra para identificação no arquivo SPSS:

- Código da pergunta começa com "BP6_BRAND"

## Indicadores Proprietários Kantar

Há outro tipo de indicadores que está vinculado a métricas cuja forma de cálculo é propriedade intelectual da Kantar, e consequentemente não é compartilhada com a Globo para ser reproduzida internamente a partir dos dados brutos dos questionários.

Para esses casos, são recebidos arquvios apartados com a informação já calculada para uso direto.

### Nps Mensal

_Ainda não contemplado pelo dashboard._

Tabela no BigQuery: "tb_nps_mensal_acumulado"

Apresenta a média de mercado do índice de NPS, referente à probabilidade de se recomendar uma marca, nas visões de filtro de Familiaridade de "Consumidores" e "Conhecedores", para cada uma das marcas(`Globo`, `Youtube` e `Netflix`).

Classificação das respostas em:

- "Detratores" -> Corresponde a indivíduos que marcaram as opções 0, 1, 2, 3, 4, 5 ou 6.
- "Neutros" -> Corresponde a indivíduos que marcaram as opções 7 ou 8.
- "Promotores" -> Corresponde a indivíduos que marcaram as opções 9 ou 10.

### Power e Dimensões

Tabela no BigQuery: "tb_power_dimensoes"

Contém um índice de "Power", que representa uma metrificação da força da marca, além das três dimensões que compõem esse índice: "Diferenciação", "Significância" e "Saliência".

### Premium

Tabela no BigQuery: "tb_premium"

Contém um índice de "Premium", composto a partir das mesmas dimensões do índice Power, que representa uma metrificação do quanto o valor percebido da marca suporta o seu preço atual.

### Contriubuição das Dimensões para o Power

Tabela no BigQuery: "tb_contribuicao_power"

Contém o valor percentural da contribuição de cada uma das dimensões para o cálculo do índice de "Power".

### BIP

Nomes alternativos: "Imagem/BIP (associação relativa)", "Brand Image Profile", "Imagem relativa".

Tabela no BigQuery: "tb_bip_relativo"

Parte da mesma lista de opções pré definidas do indicador de "Imagem (associação absoluta)", representando formas como o indivíduo pode enxergar a marca em questão.

Para cada opção, apresenta um índice representando o quanto a imagem geral da marca está associada a esse ponto (positiva ou negativamente), o que indica se este pode ser considerado uma força ou fraqueza relativa da marca.

### Agrupamentos de Atributos BIP e Contribuição para o Power

_Ainda não contemplado pelo dashboard._

Tabela no BigQuery: "tb_peso_atributos"

Contém a categorização dos atributos de BIP em grupos, o peso de cada um dos atributos dentro do seu respectivo grupo, e o valor da contribuição percentual de cada um desses grupos para a formação do índice de "Power".

### Barreiras e Facilitadores

_Ainda não contemplado pelo dashboard._

Tabela no BigQuery: "tb_barreiras_facilitadores"

Nomes alternativos: "Barreiras e facilitadores de mercado (índice)"

Parte da mesma lista de opções pré definidas do indicador de "Fatores de Escolha", representando fatores que levam o indivíduo a ecolher ou não a marca em questão como fonte de consumo de conteúdo.

Para cada fator, apresenta um índice percentual representando o quanto este influenciou (positiva ou negativamente) na escolha.

### Média de Mercado do NPS para Conhecedores e Consumidores

_Ainda não contemplado pelo dashboard._

Tabela no BigQuery: "tb_nps_mercado"

Apresenta a média de mercado do índice de NPS, referente à probabilidade de se recomendar uma marca, nas visões de filtro de Familiaridade de "Consumidores" e "Conhecedores", para cada uma das marcas.

## Indicadores de Respostas Espontâneas

Existem ainda outros indicadores referentes a algumas perguntas específicas dos questionários nas quais o respondente passa uma resposta textual espontânea, ao contrário de marcar uma opção de pré definida.

Esses indicadores ainda não são contemplados pelo processo de carga de dados nem pelo dashboard, e seu entendimento ainda não está detalhado. Dentre eles, os que já foram mapeados são:

- Awareness espontaneo - Top of Mind
- Awareness espontaneo - Menções Totais
- Needs - Necessidades básicas da categoria - Menções totais
- Associação espontânea das marcas aos needs - Menções Totais
- Razões de não consumo
- Buzz - Ouviu falar alguma coisa sobre a Globo
- Buzz - O que ouviu falar
- Buzz - Concordância com o que ouviu falar

## Filtros

Para todos os indicadores, existe uma série de filtros que podem ser aplicados.

Parte deles corresponde a casos de indicadores que também são utilizados como filtros, aplicados a nível de cada combinação de respondente e marca, cujos valores possíveis são as opções de classificação da resposta dada pelo respondente para a marca em questão:

- NPS -> Opções de filtro: "Promotores", "Detratores", "Neutros"
- Familiaridade: -> Opções de filtro: "Conhecedores", "Consumidores", "Consumidores Frequentes", "Consumidores Regulares", "Já Consumiu", "Abandonadores", "Conhecedores Não Consumidores", "Não Consumidores", "Não Conhecedores"

Além deles, existem filtros que correspondem a perguntas específicas do questionário que não geram indicadores individuais, mas são utilizadas para gerar filtros cujos valores se aplicam diretamente ao respondente, sem fazer referência a nenhuma marca específica:

- Filtros Demográficos
- Assinantes por plataforma

Os dados para a aplicação desses filtros são armazenados em tabelas específicas no BigQuery.

### Filtros Demográficos

Tabela no BigQuery: "tb_filtro_demografico"

Correspondem a quatro filtros distintos, cada um extraído de uma pergunta diferente do questionário:

- Sexo -> "Masculino", "Feminino"
- Região -> "Norte", "Nordeste", "Centro-Oeste", "Sudeste", "Sul"
- Faixa Etária -> "18-24", "25-34", "35-49", "50-65"
- Classe Social -> "A", "B", "A/B", "C"

### Assinantes por plataforma

Tabela no BigQuery: "tb_filtro_consumo_meios"

Corresponde a uma pergunta do questionário na qual o respondente marca uma ou mais opções dentre uma série de possibilidades referentes a canais de consumo de conteúdo dos quais faz uso.

Até o mês de Outubro/2022, corresponde à pergunta referente a "Consumo de Meios". Entre Outubro/2022 e Junho/2023, a pergunta não constou no questionário e o filtro não é aplicável. A partir de Julho/2023, corresponde à pergunta referente a "STREAMING".

Nesse primeiro caso, a aplicação do filtro consiste apenas em listar os assinantes de TV paga, pela seleção dos usuários que marcaram a opção "**Canais de TV por assinatura**", independentemente de que outras opções tenham ou não sido assinaladas.

No segundo caso, a aplicação consiste em classificar os usuários em alguns grupos dependendo das opções que assinalaram, conforme abaixo:

- "Assinantes de streaming" -> Marcaram quaisquer opções válidas **exceto** "TV por assinatura como, clarotv, sky, vivotv, etc", "TV BOX com acesso à IPTV" e/ou "Não tenho acesso"
- "Assinantes de TV por assinatura" -> Marcaram a opção "TV por assinatura como, clarotv, sky, vivotv, etc"
- "Assinantes Pirata" -> Marcaram a opção "TV BOX com acesso à IPTV"
- "Não Assinantes" -> Marcaram a opção "Não tenho acesso"
- "Assinantes de Globoplay" -> Marcaram as opções "Globoplay versão paga simples" e/ou "Globoplay + Canais Ao Vivo"
- "Assinantes de Netflix" -> Marcaram a opção "Netflix"
- "Assinantes de Youtube Premium" -> Marcaram a opção "Youtube Premium"
- "Assinantes de Prime Video" -> Marcaram a opção "Amazon Prime Video"
- "Assinantes de Disney+" -> Marcaram a opção "Disney+"
- "Assinantes de Hbo Max" -> Marcaram a opção "Hbo Max"

## Dashboard

### Indicadores Contemplados

A lista dos indicadores já contemplados e as tabelas no BigQuery com seus respectivos dados é a seguinte:

**Indicadores Proprietários**

- Power e Dimensões -> tb_power_dimensoes
- Premium -> tb_premium
- Contriubuição das Dimensões para o Power -> tb_contribuicao_power
- BIP -> tb_bip_relativo
- Agrupamentos de Atributos BIP e Contribuição para o Power -> tb_peso_atributos

**Indicadores extraídos do Questionário**

- Afinidade -> tb_afinidade
- Atende às Necessidades -> tb_necessidades
- Confiança -> tb_confianca
- Consideração -> tb_consideracao
- Diferente -> tb_diferente
- Dita Tendências -> tb_dita_tendencias
- Familiaridade -> tb_familiaridade
- Imagem (associação absoluta) -> tb_imagem
- NPS -> tb_nps
- Preferência -> tb_preferencia

### Estrutura

Os indicadores de métricas proprietárias são extraídos já calculados, e já com os filtros possíveis, direto de suas respectivas tabelas.

Os demais indicadores, que vem do questionário, são importados para o PBI utilizando queries específicas que realizam um pré tratamento para os dados de cada um:

- Afinidade

```sql
WITH proc_class AS(
    SELECT
        * EXCEPT(cd_label, ds_label, ds_resposta, nm_indicador, ds_classificacao, ds_classificacao_aux, dt_processamento),
        CONCAT(cd_pessoa,dt_mes_inicio,dt_mes_fim) as id_pesquisa,
        CONCAT(cd_pessoa,dt_mes_inicio,dt_mes_fim,nm_marca) as id_pesquisa_marca,
        CASE WHEN ds_classificacao_aux = ds_resposta AND ARRAY_LENGTH(ds_classificacao) <= 1 THEN NULL
            ELSE ds_classificacao_aux
            END AS ds_classificacao_expl,
        CASE WHEN ds_resposta = '+3 Eu amo' THEN '7 Eu amo'
            WHEN ds_resposta = '+2' THEN '6'
            WHEN ds_resposta = '+1' THEN '5'
            WHEN ds_resposta = '0 Neutro' THEN '4 Neutro'
            WHEN ds_resposta = '-1' THEN '3'
            WHEN ds_resposta = '-2' THEN '2'
            WHEN ds_resposta = '-3 Eu odeio' THEN '1 Eu odeio'
            END AS ds_resposta,
        ds_resposta AS ds_resposta_orig,
        CASE WHEN nm_marca = "Amazon" then 1
            WHEN nm_marca = "Apple" then 2
            WHEN nm_marca = "Discovery" then 3
            WHEN nm_marca = "Disney" then 4
            WHEN nm_marca = "Facebook" then 5
            WHEN nm_marca = "Google" then 6
            WHEN nm_marca = "Globo" then 7
            WHEN nm_marca = "HBO" then 8
            WHEN nm_marca = "Instagram" then 9
            WHEN nm_marca = "Netflix" then 10
            WHEN nm_marca = "Record" then 11
            WHEN rtrim(ltrim(nm_marca)) = "SBT" then 12
            WHEN nm_marca = "Spotify" then 13
            WHEN nm_marca = "TikTok" then 14
            WHEN nm_marca = "Twitter" then 15
            WHEN nm_marca = "Youtube" then 16
            END id_marca
    FROM gglobo-audiencia-hdg-prd.prep_monitor_marcas_masterbrand.tb_afinidade,
        UNNEST(ds_classificacao) AS ds_classificacao_aux
)
SELECT * EXCEPT(ds_resposta_orig) FROM proc_class
WHERE (ds_classificacao_expl != ds_resposta_orig OR ds_classificacao_expl IS NULL)
```

- Confiança

```sql
WITH proc_regra AS(
    SELECT DISTINCT
        * EXCEPT(cd_label, ds_label, nm_indicador, ds_classificacao, ds_classificacao_aux, dt_processamento),
        CASE
            WHEN ds_classificacao_aux = ds_resposta AND ARRAY_LENGTH(ds_classificacao) <= 1 THEN NULL
            WHEN ds_classificacao_aux IN ("TOP2BOTTOM", "TOP2BOX") THEN NULL
            ELSE ds_classificacao_aux
            END AS ds_classificacao_expl
    FROM gglobo-audiencia-hdg-prd.prep_monitor_marcas_masterbrand.tb_confianca,
        UNNEST(ds_classificacao) AS ds_classificacao_aux
    WHERE (ds_classificacao_aux = ds_resposta AND ARRAY_LENGTH(ds_classificacao) <= 1)
        OR ds_classificacao_aux NOT IN ("TOP2BOTTOM", "TOP2BOX")
),
proc_top2 AS(
    SELECT DISTINCT
        * EXCEPT(cd_label, ds_label, nm_indicador, ds_classificacao, ds_classificacao_aux, dt_processamento),
        CASE
            WHEN ds_classificacao_aux = ds_resposta AND ARRAY_LENGTH(ds_classificacao) <= 1 THEN NULL
            WHEN ds_classificacao_aux NOT IN ("TOP2BOTTOM", "TOP2BOX") THEN NULL
            ELSE ds_classificacao_aux
            END AS ds_classificacao_expl_top2
    FROM gglobo-audiencia-hdg-prd.prep_monitor_marcas_masterbrand.tb_confianca,
        UNNEST(ds_classificacao) AS ds_classificacao_aux
    WHERE (ds_classificacao_aux = ds_resposta AND ARRAY_LENGTH(ds_classificacao) <= 1)
        OR ds_classificacao_aux IN ("TOP2BOTTOM", "TOP2BOX")
),
proc_class AS(
  SELECT * FROM proc_regra LEFT JOIN proc_top2
  USING(cd_pessoa,ds_periodo,dt_entrevista,nm_categoria,nm_marca,cd_resposta,dt_mes_inicio,dt_mes_fim,ds_onda,ds_resposta)
)
SELECT *,
    CONCAT(cd_pessoa,dt_mes_inicio,dt_mes_fim) as id_pesquisa,
    CONCAT(cd_pessoa,dt_mes_inicio,dt_mes_fim,nm_marca) as id_pesquisa_marca
FROM proc_class
WHERE (ds_classificacao_expl != ds_resposta OR ds_classificacao_expl IS NULL)
```

- Consideração

```sql
WITH proc_class AS(
    SELECT
        * EXCEPT(cd_label, ds_label, nm_indicador, ds_classificacao, ds_classificacao_aux, dt_processamento),
        CASE WHEN ds_classificacao_aux = ds_resposta AND ARRAY_LENGTH(ds_classificacao) <= 1 THEN NULL
            ELSE ds_classificacao_aux
            END AS ds_classificacao_expl
    FROM gglobo-audiencia-hdg-prd.prep_monitor_marcas_masterbrand.tb_consideracao,
        UNNEST(ds_classificacao) AS ds_classificacao_aux
)
SELECT
    *,
    CONCAT(cd_pessoa,dt_mes_inicio,dt_mes_fim) as id_pesquisa,
    CONCAT(cd_pessoa,dt_mes_inicio,dt_mes_fim,nm_marca) as id_pesquisa_marca
FROM proc_class
WHERE ds_classificacao_expl = "TOP2BOX" OR (cd_resposta IN (3,4) AND ds_classificacao_expl != "TOP2BOTTOM")
```

- Diferente

```sql
WITH proc_class AS(
    SELECT
        * EXCEPT(cd_label, ds_label, nm_indicador, ds_classificacao, ds_classificacao_aux, dt_processamento),
        CASE WHEN ds_classificacao_aux = ds_resposta AND ARRAY_LENGTH(ds_classificacao) <= 1 THEN NULL
            ELSE ds_classificacao_aux
            END AS ds_classificacao_expl
    FROM gglobo-audiencia-hdg-prd.prep_monitor_marcas_masterbrand.tb_diferente,
        UNNEST(ds_classificacao) AS ds_classificacao_aux
)
SELECT
    *,
    CONCAT(cd_pessoa,dt_mes_inicio,dt_mes_fim) as id_pesquisa,
    CONCAT(cd_pessoa,dt_mes_inicio,dt_mes_fim,nm_marca) as id_pesquisa_marca
FROM proc_class
WHERE (ds_classificacao_expl != ds_resposta OR ds_classificacao_expl IS NULL)
```

- Dita Tendências

```sql
WITH proc_class AS(
    SELECT
        * EXCEPT(cd_label, ds_label, nm_indicador, ds_classificacao, ds_classificacao_aux, dt_processamento),
        CASE WHEN ds_classificacao_aux = ds_resposta AND ARRAY_LENGTH(ds_classificacao) <= 1 THEN NULL
            ELSE ds_classificacao_aux
            END AS ds_classificacao_expl
    FROM gglobo-audiencia-hdg-prd.prep_monitor_marcas_masterbrand.tb_dita_tendencias,
        UNNEST(ds_classificacao) AS ds_classificacao_aux
)
SELECT
    *,
    CONCAT(cd_pessoa,dt_mes_inicio,dt_mes_fim) as id_pesquisa,
    CONCAT(cd_pessoa,dt_mes_inicio,dt_mes_fim,nm_marca) as id_pesquisa_marca
FROM proc_class
WHERE (ds_classificacao_expl != ds_resposta OR ds_classificacao_expl IS NULL)
```

- Familiaridade

```sql
WITH proc_class AS(
    SELECT
        * EXCEPT(cd_label, ds_label, nm_indicador, ds_classificacao, ds_classificacao_aux, dt_processamento),
        CONCAT(cd_pessoa,dt_mes_inicio,dt_mes_fim) as id_pesquisa,
        CONCAT(cd_pessoa,dt_mes_inicio,dt_mes_fim,nm_marca) as id_pesquisa_marca,
        CASE WHEN ds_classificacao_aux = ds_resposta AND ARRAY_LENGTH(ds_classificacao) <= 1 THEN NULL
            ELSE ds_classificacao_aux
            END AS ds_classificacao_expl
    FROM gglobo-audiencia-hdg-prd.prep_monitor_marcas_masterbrand.tb_familiaridade,
        UNNEST(ds_classificacao) AS ds_classificacao_aux
)
SELECT * FROM proc_class
WHERE (ds_classificacao_expl != ds_resposta OR ds_classificacao_expl IS NULL)
```

- Imagem

```sql
WITH proc_resp AS(
    SELECT
        * EXCEPT(cd_label, ds_label, cd_resposta, ds_resposta, nm_indicador, ds_classificacao, ds_classificacao_expl, dt_processamento),
        REGEXP_REPLACE(ds_classificacao_expl,"Que Que ","Que ") AS ds_resposta_proc
    FROM gglobo-audiencia-hdg-prd.prep_monitor_marcas_masterbrand.tb_imagem,
        UNNEST(ds_classificacao) AS ds_classificacao_expl
    WHERE ds_resposta = "Yes" AND UPPER(ds_classificacao_expl) LIKE "É UMA MARCA%"
)
SELECT
    * EXCEPT(ds_resposta_proc),
    REGEXP_REPLACE(ds_resposta_proc,"É Uma Marca Que ","") AS ds_resposta,
    CONCAT(cd_pessoa,dt_mes_inicio,dt_mes_fim) as id_pesquisa,
    CONCAT(cd_pessoa,dt_mes_inicio,dt_mes_fim,nm_marca) as id_pesquisa_marca,
FROM proc_resp
```

- Atende às Necessidades

```sql
WITH proc_class AS(
    SELECT
        * EXCEPT(cd_label, ds_label, nm_indicador, ds_classificacao, ds_classificacao_aux, dt_processamento),
        CASE WHEN ds_classificacao_aux = ds_resposta AND ARRAY_LENGTH(ds_classificacao) <= 1 THEN NULL
            ELSE ds_classificacao_aux
            END AS ds_classificacao_expl
    FROM gglobo-audiencia-hdg-prd.prep_monitor_marcas_masterbrand.tb_necessidades,
        UNNEST(ds_classificacao) AS ds_classificacao_aux
)
SELECT
    * ,
    CONCAT(cd_pessoa,dt_mes_inicio,dt_mes_fim) as id_pesquisa,
    CONCAT(cd_pessoa,dt_mes_inicio,dt_mes_fim,nm_marca) as id_pesquisa_marca
FROM proc_class
WHERE (ds_classificacao_expl != ds_resposta OR ds_classificacao_expl IS NULL)
```

- NPS

```sql
WITH proc_class AS(
    SELECT
        * EXCEPT(cd_label, ds_label, nm_indicador, ds_classificacao, ds_classificacao_aux, dt_processamento),
        CASE WHEN ds_classificacao_aux = ds_resposta AND ARRAY_LENGTH(ds_classificacao) <= 1 THEN NULL
            ELSE ds_classificacao_aux
            END AS ds_classificacao_expl
    FROM `gglobo-audiencia-hdg-prd.prep_monitor_marcas_masterbrand.tb_nps`,
        UNNEST(ds_classificacao) AS ds_classificacao_aux
)
SELECT
    *,
    CONCAT(cd_pessoa,dt_mes_inicio,dt_mes_fim) as id_pesquisa,
    CONCAT(cd_pessoa,dt_mes_inicio,dt_mes_fim,nm_marca) as id_pesquisa_marca,
    CONCAT(cast(extract(year from dt_mes_inicio) as STRING), format_date('%Q', dt_mes_fim)) as quarter_onda,
    format_date('%y%m', dt_entrevista) AS mes_ano_nr_entrevista,
    extract(year from dt_entrevista) as Ano,
    CASE WHEN extract(month from dt_entrevista) in (1, 2, 3, 4, 5, 6) THEN CONCAT('1S ', cast(extract(year from dt_entrevista) as string))
        ELSE CONCAT('2S ', cast(extract(year from dt_entrevista) as string))
        END Semestre,
    CONCAT(CAST(extract(quarter from dt_entrevista) AS STRING), "T ", cast(extract(year from dt_entrevista) as string)) as Trimestre,
    CASE WHEN DATE_DIFF(dt_mes_fim, dt_mes_inicio, MONTH) IN (0, 2) THEN ds_onda
        ELSE NULL
        END Trimestral,
    CASE WHEN ds_periodo = "Jul'2022" THEN ds_onda
        WHEN ds_periodo = "Ago'2022-Out'2022" THEN "Ago'2022-Dez'2022"
        WHEN ds_periodo = "Nov'2022" THEN "Ago'2022-Dez'2022"
        WHEN ds_periodo = "Dez'2022" THEN "Ago'2022-Dez'2022"
        WHEN extract(month from dt_entrevista) in (1, 2, 3, 4, 5, 6) THEN CONCAT("Jan'", CAST(EXTRACT(year from dt_entrevista) as STRING), "-Jun'", CAST(EXTRACT(year from dt_entrevista) as STRING))
        WHEN extract(month from dt_entrevista) in (7, 8, 9, 10, 11, 12) THEN CONCAT("Jul'", CAST(EXTRACT(year from dt_entrevista) as STRING), "-Dez'", CAST(EXTRACT(year from dt_entrevista) as STRING))
        END AS Semestral,
    CASE WHEN ds_periodo = "Jul'2022" THEN dt_mes_inicio
        WHEN ds_periodo = "Ago'2022-Out'2022" THEN DATE(CONCAT(cast(extract(year from dt_entrevista) AS STRING), "-08", "-01"))
        WHEN ds_periodo = "Nov'2022" THEN DATE(CONCAT(cast(extract(year from dt_entrevista) AS STRING), "-08", "-01"))
        WHEN ds_periodo = "Dez'2022" THEN DATE(CONCAT(cast(extract(year from dt_entrevista) AS STRING), "-08", "-01"))
        WHEN extract(month from dt_entrevista) in (1, 2, 3, 4, 5, 6) THEN DATE(CONCAT(cast(extract(year from dt_entrevista) AS STRING), "-01", "-01"))
        WHEN extract(month from dt_entrevista) in (7, 8, 9, 10, 11, 12) THEN DATE(CONCAT(cast(extract(year from dt_entrevista) AS STRING), "-07", "-02"))
        END as Ordem_Semestral,
    CASE WHEN ds_onda = "Jul'2022" THEN "20221"
        WHEN extract(month from dt_entrevista) in (1, 2, 3, 4, 5, 6) THEN CONCAT(CAST(EXTRACT(year from dt_entrevista) as STRING), "1")
        WHEN extract(month from dt_entrevista) in (7, 8, 9, 10, 11, 12) THEN CONCAT(CAST(EXTRACT(year from dt_entrevista) as STRING), "2")
        END nr_semestre_nps,
    CASE WHEN ds_onda = "Out'2022-Dez'2022" THEN "20225"
        ELSE CONCAT(cast(extract(year from dt_mes_inicio) as STRING), format_date('%Q', dt_mes_fim))
        END quarter_onda_nova,
    format_date('%h %y', dt_entrevista) AS mes_ano_entrevista,
FROM proc_class
WHERE (ds_classificacao_expl != ds_resposta OR ds_classificacao_expl IS NULL)
```

- Preferência

```sql
SELECT
    * EXCEPT(dt_processamento), CONCAT(cd_pessoa,dt_mes_inicio,dt_mes_fim) as id_pesquisa,
    CONCAT(cd_pessoa,dt_mes_inicio,dt_mes_fim,nm_marca) as id_pesquisa_marca
FROM gglobo-audiencia-hdg-prd.prep_monitor_marcas_masterbrand.tb_preferencia
```

```sql
WITH proc_class AS(
SELECT * EXCEPT(cd_label, ds_label, cd_resposta, nm_indicador, ds_classificacao, ds_classificacao_aux, dt_processamento),
CASE WHEN ds_classificacao_aux = ds_resposta AND ARRAY_LENGTH(ds_classificacao) <= 1 THEN NULL ELSE ds_classificacao_aux END AS ds_classificacao_expl
FROM gglobo-audiencia-hdg-prd.prep_monitor_marcas_masterbrand.tb_afinidade,
UNNEST(ds_classificacao) AS ds_classificacao_aux
)
SELECT * FROM proc_class
WHERE (ds_classificacao_expl != ds_resposta OR ds_classificacao_expl IS NULL)
```

Os indicadores sem query de extração listada são importados diretamente como estão nas suas tabelas de origem.

Existem ainda duas outras tabelas, referentes a filtros necessários para as visualizações, que também devem ser importadas, com queries diferentes:

- Filtros Demográficos

```sql
SELECT
    * EXCEPT(dt_processamento),
    CONCAT(cd_pessoa,dt_mes_inicio,dt_mes_fim) as id_pesquisa
FROM `gglobo-audiencia-hdg-prd.prep_monitor_marcas_masterbrand.tb_filtro_demografico`
```

- Filtros de Assinantes por Plataforma

```sql
WITH assinantes_antigo_base AS(
    SELECT DISTINCT
        nm_categoria,
        cd_pessoa,
        dt_mes_inicio,
        dt_mes_fim,
        "S" AS ds_classificacao_expl
    FROM `gglobo-audiencia-hdg-prd.prep_monitor_marcas_masterbrand.tb_filtro_consumo_meios`
    WHERE "Canais de TV por assinatura" IN UNNEST(ds_classificacao)
        AND dt_mes_inicio < "2023-01-01"
)
,assinantes_antigo AS(
    SELECT
        * EXCEPT(ds_consumo_meios,ds_classificacao,dt_processamento,ds_classificacao_expl),
        CONCAT(cd_pessoa,dt_mes_inicio,dt_mes_fim) as id_pesquisa,
        CASE WHEN ds_classificacao_expl IS NULL THEN "N"
            ELSE ds_classificacao_expl
            END AS ds_classificacao_expl
    FROM `gglobo-audiencia-hdg-prd.prep_monitor_marcas_masterbrand.tb_filtro_consumo_meios`
        LEFT JOIN assinantes_antigo_base
        USING (nm_categoria, cd_pessoa, dt_mes_inicio, dt_mes_fim)
    WHERE dt_mes_inicio < "2023-01-01"
)
,assinantes_novo AS(
    SELECT
        * EXCEPT(ds_consumo_meios,ds_classificacao,dt_processamento),
        CONCAT(cd_pessoa,dt_mes_inicio,dt_mes_fim) as id_pesquisa
    FROM `gglobo-audiencia-hdg-prd.prep_monitor_marcas_masterbrand.tb_filtro_consumo_meios`,
        UNNEST(ds_classificacao) AS ds_classificacao_expl
    WHERE dt_mes_inicio >= "2023-01-01"
)
SELECT
    cd_pessoa,
    ds_periodo,
    dt_entrevista,
    nm_categoria,
    dt_mes_inicio,
    dt_mes_fim,
    ds_onda,
    id_pesquisa,
    ds_classificacao_expl
FROM assinantes_antigo
UNION ALL
SELECT
    cd_pessoa,
    ds_periodo,
    dt_entrevista,
    nm_categoria,
    dt_mes_inicio,
    dt_mes_fim,
    ds_onda,
    id_pesquisa,
    ds_classificacao_expl
FROM assinantes_novo
```

Após essa importação, é feito o join da base de cada indicador com as seguintes outras tabelas, usando algumas colunas como chave:

- tb_filtro_demografico -> Colunas de join: "nm_categoria", "id_pesquisa"
- tb_filtro_consumo_meios -> Colunas de join: "nm_categoria", "id_pesquisa"
- tb_familiaridade -> Colunas de join: "nm_categoria", "id_pesquisa", "nm_marca"
- tb_nps -> Colunas de join: "nm_categoria", "id_pesquisa", "nm_marca"

A exceção para esse padrão são os indicadores de Familiaridade e NPS:

- Familiaridade
  - Não possui join com "tb_familiaridade", pois são os dados do próprio indicador
- NPS
  - Não possui join com "tb_nps", pois são os dados do próprio indicador

### Métricas

Para todos os indicadores do questionário, a métrica calculada é o pecentual distinto de "cd_pessoa".

Essa contagem distinta considera as colunas do resultado da query de importação para o PBI que contêm a resposta dada para a pergunta pelo respondente e as possíveis classificações dessa resposta conforme as regras de negócio definidas. A coluna utilizada varia dependendo do indicador, podendo ser uma das seguintes:

- "ds_resposta"
- "ds_classificacao_expl"
- "ds_classificacao_aux"

Especificamente para o indicador de preferência, a métrica segue a mesma lógica, porém acessando apenas uma outra coluna:

- "cd_preferencia"

Além das colunas de respostas e classificações, é considerada também apenas uma dentre as seguintes colunas, dependendo do tipo de visualização selecionado:

- "nm_marca"
- "ds_onda"
- a extração do mês/ano de "dt_entrevista"

Além da métrica percentual de pessoas, apenas o indicador do NPS tem uma métrica adicional gerada no PBI, que é o Índice NPS.

O índice é calculado a partir da métrica percentual de pessoas para algumas classificações específicas de resposta, aplicando a seguinte regra:

> [% de pessoas classificadas como "Promotores"] - [% de pessoas classificadas como "Detratores"]

Com essa diferença sendo exibida em pontos percentuais.
Ex: 50% de Promotores - 30% de Detratores -> Índice NPS = 20

### Granularidade de visualização

A nível da visualização, existem duas granularidades de tempo nas quais as métricas são calculadas:

- Por Onda -> usando a coluna "ds_onda"
- Por Mês/Trimestre/Semestre -> extraindo o mês e ano da coluna "dt_entrevista" e agrupando conforme a periodicidade desejada

Para cada uma dessas granularidades de cálculo, existem duas visões principais desejadas:

- Multi marca -> Passando "nm_marca" no eixo X e a Onda ou Mês como filtro
- Multi período -> Passando a Onda ou Mês no eixo X e "nm_marca" como filtro

### Filtros

As visualizações da maioria dos indicadores (com exceção dos indicadores proprietários e alguns outros casos pontuais) apresentam também os seguintes filtros:

- "Consumidor" -> Corresponde ao indicador de Familiaridade. Conta com todas as opções da coluna "ds_classificacao_expl" da "tb_familiaridade" importada pela query especificada
- "NPS" -> Corresponde ao indicador de NPS. Conta com todas as opções da coluna "ds_classificacao_expl" da "tb_nps" importada pela query especificada
- "Assinantes por Plataforma" -> Conta com todas as opções da coluna "ds_classificacao_expl" da "tb_filtro_consumo_meios" importada pela query especificada
- "Sexo" -> Conta com todas as opções da coluna "ds_sexo" da "tb_filtro_demografico"
- "Região" -> Conta com todas as opções da coluna "ds_regiao" da "tb_filtro_demografico"
- "Idade" -> Conta com todas as opções da coluna "ds_faixa_etaria" da "tb_filtro_demografico"
- "Classe" -> Conta com todas as opções da coluna "ds_classe_social" da "tb_filtro_demografico"

As exceções para esse padrão são o indicador de Familiaridade (que não apresenta o filtro "Consumidor") e o indicador de NPS ("que não apresenta o filtro "NPS").

As visualizações do indicador NPS também não apresentam o filtro "Consumidor", pois o indicador é separado nas duas visões específicas de "NPS Consumidores" e "NPS Conhecedores", que já são aplicações desse filtro para valores específicos (respectivamene "Consumidores" e "Conhecedores").

## Arquivo Power BI - Monitor de Marcas


Os dashboards de power BI foram desenvolvidos no arquivo: [Indicadores Masterbrand](https://app.powerbi.com/groups/15413a9c-2f8e-4a3b-bfa9-d2a4a61f486d/reports/1af43e5a-b7d7-4cb6-aa55-73f09c9646fe?experience=power-bi.pbix) que fica no workspace Premium “Pesquisa de Marcas”.

### Agendamento de carga

Os arquivos da Kantar tem previsão de disponibilidade para carga no dia 16 do mês seguinte ao término de cada trimestre. Pela característica do power bi de agendamentos diários ou semanais, cadastramos a opção de atualização dos dados todas ás segundas-feiras a partir das 9:30am. As cargas costumam durar em torno de 10 min.

### Gerando link para embed dos dashboards do Monitor de Marcas

Usamos o link das abas do dashboard para o “embed” no sistema desenvolvido pela equipe de Soluções – Infra sob responsabilidade do Roberto Moulin (desenvolvido em Node.js / Vue).

Para gerar o link siga os passos abaixo:

1 – Publicar o dashboard no power bi desktop com a primeira aba (Multi Brand Gráficos) do indicador desejado sem que esteja oculta;

![Imagem](documentacao/imagem1.png)

2 – Após o arquivo publicado, acessamos o workspace no navegador e abrimos o arquivo de Indicadores_Masterbrand para acessar, no menu Arquivo -- Inserir Relatório --  site ou portal, e copiar o “Link para inserir este conteúdo”.

![Imagem](documentacao/imagem2.png)

Exemplo de link gerado: https://app.powerbi.com/reportEmbed?reportId=1af43e5a-b7d7-4cb6-aa55-73f09c9646fe&autoAuth=true&ctid=a7cdc447-3b29-4b41-b73e-8a2cb54b06c6 

3 – Copiar em seguida o Report Section a partir do link do relatório que aparece na barra de endereço do navegador.

![Imagem](documentacao/imagem3.png)

4 - Colocar no final do ”Link para inserir este conteúdo” a tag, &pageName= mais a parte do ReportSection (sem a parte do “?experience=power-bi”)

Exemplo de link final:

https://app.powerbi.com/reportEmbed?reportId=f78bd0cc-b8c3-4f54-b1c6-365853ddad77&autoAuth=true&ctid=a7cdc447-3b29-4b41-b73e-8a2cb54b06c6&pageName=ReportSection3acdff340de9d3199e6a

5 - Testar o link completo em uma nova aba do navegador. Em seguida, no power bi desktop, ocultar a aba do indicador e publicar de novo o dashboard.

### Filtros de período

Solução para funcionamento dos filtros de período

Por solicitação do time cliente, a periodicidade de consulta aos dados dos indicadores pode ser: trimestral ou semestral.

É possível fazer essa seleção junto aos filtros principais de cada dashboard no topo de cada aba. Na combo nomeada Tipo de Período temos as opções Trimestre e Semestre, e na combo nomeada Período temos os ranges de datas disponíveis para consulta.

![Imagem](documentacao/imagem4.png)

## Solução dos filtros de período para os Indicadores não proprietários

Para os indicadores não proprietários (que não foram criados pela Kantar), os dados das pesquisas chegam em periodicidade trimestral. Sendo os dados semestrais uma soma de 2 trimestres calculada dentro do power bi.

Ao longo do desenvolvimento desses cálculos, notamos que era possível que a Kantar enviasse os dados de um determinado trimestre antes que o trimestre seguinte também estivesse disponível para compor os valores totais do semestre. Nesses casos, o novo trimestre deveria aparecer no filtro da opção “Trimestre”, contudo o semestre incompleto não poderia estar na combo “Período” para “Semestre”. Para tratar essa questão criamos as tabelas de controle abaixo:

Tb_filtro_trimestral_nao_proprietario: Tabela contendo os trimestres das pesquisas(campo ds_onda), ordem dos trimestres e quantidade de trimestres por onda dos indicadores não proprietários (tb_familiaridade, tb_preferencia, tb_afinidade, tb_necessidades, tb_diferente, tb_dita_tendencias, tb_confianca, tb_consideracao, tb_nps).

Tb_filtro_semestral_nao_proprietario: Tabela contendo os semestres, a ordem dos semestres e a quantidade de trimestres que compõe aquele semestre encontrados na base dos indicadores não proprietários (tb_familiaridade, tb_preferencia, tb_afinidade, tb_necessidades, tb_diferente, tb_dita_tendencias, tb_confianca, tb_consideracao, tb_nps.).

A combo “Tipo de Período” oferece as opções Trimestre (que exibe os dados da Tb_filtro_trimestral_nao_proprietario na combo Período) e Semestre (que exibe os dados da Tb_filtro_semestral_nao_proprietario na combo Período).

![Imagem](documentacao/imagem5.png)

Em seguida, na combo “Período”, usamos o campo Filtra Semestre para que não apareça o semestre incompleto (que só possui parte dos dados) como opção de seleção.

![Imagem](documentacao/imagem6.png)

As demais tabelas abaixo são usadas para as combos da data de indicadores proprietários. Esses são disponibilizados pela Kantar em periodicidade semestral, geralmente no mês seguinte ao encerramento de cada semestre.

Tb_filtro_trimestral: Tabela contendo os períodos e as datas de início de todos os trimestres na base do indicador Power (tb_power_dimensoes).

Tb_filtro_trimestral_BIP: Tabela contendo os períodos e as datas de início de todos os trimestres na base do indicador Bip (tb_bip_relativo).

Tb_filtro_semestral: Tabela contendo os períodos e as datas de início de todos os semestres na base do indicador Power (tb_power_dimensoes).

Tb_filtro_semestral_BIP: Tabela contendo os períodos e as datas de início de todos os semestres na base do indicador BIP (tb_bip_relativo).

## Solução de período para Matrizes das páginas “Multi Period tabela”

Nas páginas do tipo “Multi Period tabela”, que temos em cada indicador, exibimos matrizes com os dados das respostas dos questionários, a base de respondentes e a classificação das respostas (Top2box, top2bottom).

Ao implementar a solução de retirar o semestre incompleto das combos de período, nos deparamos com um problema. Ao selecionar a opção “Todos” na combo de período, quando o “Tipo de período” era “Semestre”, mesmo sem o semestre incompleto constar na combo, ele montava a matriz com uma coluna a mais de período em branco.

Para solucionar essa questão, implementamos os valores na matriz através de fórmula Dax nos moldes abaixo, substituindo pelos campos de cada indicador. Toda tabela com os dados do indicador tem algumas fórmulas iniciadas pelo caractere “*” com a finalidade de trazer os dados das matrizes.

Exemplo de cálculo dos percentuais de classificação das respostas (Top2box, top2bottom), usada na matriz da página do indicador Diferente multi period tabela:

## Fórmulas DAX - Indicador "Diferente"

### 1. *Nome do campo: * Diferente*

```DAX
SWITCH ( 
    TRUE (), 
    SELECTEDVALUE ( 'Parâmetro Diferente'[Parâmetro Pedido] ) = 2, 
        CALCULATE ( 
            [% ParticipaçãoD Top2NW], 
            tb_filtro_semestral_nao_proprietario[semestre] <> BLANK () 
        ), 
    SELECTEDVALUE ( 'Parâmetro Diferente'[Parâmetro Pedido] ) = 3, [% ParticipaçãoD Top2NW] 
)
```

### *Descrição*
```
Calcula o percentual de cada classificação do questionário (Top2box, Top2bottom, Neutros) em relação ao total de respondentes (Base).
Se os filtros aplicados não gerarem dados para o cálculo, retorna 0.
Exclui períodos em branco, considerando semestres com dados incompletos.
```
---
### 2. *Nome do campo: ** Diferente*

```DAX
SWITCH ( 
    TRUE (), 
    SELECTEDVALUE ( 'Parâmetro Diferente'[Parâmetro Pedido] ) = 2, 
        CALCULATE ( 
            [Qtd de PessoasD 0], 
            tb_filtro_semestral_nao_proprietario[semestre] <> BLANK () 
        ), 
    SELECTEDVALUE ( 'Parâmetro Diferente'[Parâmetro Pedido]  ) = 3, 
        [Qtd de PessoasD 0] 
)
```

### *Descrição*
```
Calcula a quantidade de pessoas que responderam ao questionário no período selecionado (Base).
Se os filtros aplicados não gerarem dados para o cálculo, retorna 0.
Exclui períodos em branco para semestres com dados incompletos.
```
---
### 3. *Nome do campo: *** Diferente*
```DAX
VAR total = 
    CALCULATE ( 
        [Qtd de PessoasD 0], 
        ALLSELECTED ( 'tb_diferente'[ds_resposta] ), 
        ALLSELECTED ( 'tb_diferente'[cd_resposta] ) 
    ) 
RETURN 
SWITCH ( 
    TRUE (), 
    SELECTEDVALUE ( 'Parâmetro Diferente'[Parâmetro Pedido] ) = 2, 
        CALCULATE ( 
            DIVIDE ( 
                [Qtd de PessoasD 0], 
                total, 
                0 
            ), 
            tb_filtro_semestral_nao_proprietario[semestre] <> BLANK () 
        ), 
    SELECTEDVALUE ( 'Parâmetro Diferente'[Parâmetro Pedido] ) = 3, 
        DIVIDE ( 
            [Qtd de PessoasD 0], 
            total, 
            0 
        ) 
)
```

### *Descrição*
```
Calcula o percentual de pessoas que responderam a cada opção de resposta do questionário no período selecionado (Base).
Se os filtros aplicados não gerarem dados para o cálculo, retorna 0.
Também exclui períodos em branco, considerando semestres com dados incompletos.
```

### Solução de período para tratar primeira pesquisa de Julho-2022

A primeira pesquisa encomendada a Kantar corresponde ao período de Julho de 2022. Essa primeira pesquisa teve algumas características diferentes das demais e por isso, a pedido do time cliente, nós utilizamos ela para comparação tanto com períodos de “Trimestre”, quanto com os de “Semestre”.

Para gerar os dados de comparação com os indicadores proprietários criamos tabelas no pbi apenas com dados de Julho-22 que depois são mescladas aos dados originais. Exemplo para a tabela de BIP abaixo:

![Imagem](documentacao/imagem7.png)

![Imagem](documentacao/imagem8.png)

Obs: O indicador Power se tornou exceção em Julho de 2025, pois o time cliente solicitou que apenas os dados de “Semestre” fossem exibidos no filtro de “Período”.

Para os indicadores não proprietários essa questão foi resolvida dentro das queries das tabelas Tb_filtro_semestral_nao_proprietario e Tb_filtro_trimestral_nao_proprietario. Seguem as queries delas abaixo:


## Query: tb_filtro_trimestral_nao_proprietario

```sql
WITH TRIMESTRAL AS (
  SELECT DISTINCT 
    ds_onda, 
    ds_periodo, 
    dt_mes_inicio, 
    CONCAT(EXTRACT(YEAR FROM dt_mes_inicio), EXTRACT(QUARTER FROM dt_mes_fim)) AS ordem_trimestral
  FROM `gglobo-audiencia-hdg-prd.prep_monitor_marcas_masterbrand.tb_afinidade`

  UNION ALL

  SELECT DISTINCT 
    ds_onda, 
    ds_periodo, 
    dt_mes_inicio, 
    CONCAT(EXTRACT(YEAR FROM dt_mes_inicio), EXTRACT(QUARTER FROM dt_mes_fim)) AS ordem_trimestral
  FROM `gglobo-audiencia-hdg-prd.prep_monitor_marcas_masterbrand.tb_necessidades`

  UNION ALL

  SELECT DISTINCT 
    ds_onda, 
    ds_periodo, 
    dt_mes_inicio, 
    CONCAT(EXTRACT(YEAR FROM dt_mes_inicio), EXTRACT(QUARTER FROM dt_mes_fim)) AS ordem_trimestral
  FROM `gglobo-audiencia-hdg-prd.prep_monitor_marcas_masterbrand.tb_diferente`

  UNION ALL

  SELECT DISTINCT 
    ds_onda, 
    ds_periodo, 
    dt_mes_inicio, 
    CONCAT(EXTRACT(YEAR FROM dt_mes_inicio), EXTRACT(QUARTER FROM dt_mes_fim)) AS ordem_trimestral
  FROM `gglobo-audiencia-hdg-prd.prep_monitor_marcas_masterbrand.tb_dita_tendencias`

  UNION ALL

  SELECT DISTINCT 
    ds_onda, 
    ds_periodo, 
    dt_mes_inicio, 
    CONCAT(EXTRACT(YEAR FROM dt_mes_inicio), EXTRACT(QUARTER FROM dt_mes_fim)) AS ordem_trimestral
  FROM `gglobo-audiencia-hdg-prd.prep_monitor_marcas_masterbrand.tb_confianca`

  UNION ALL

  SELECT DISTINCT 
    ds_onda, 
    ds_periodo, 
    dt_mes_inicio, 
    CONCAT(EXTRACT(YEAR FROM dt_mes_inicio), EXTRACT(QUARTER FROM dt_mes_fim)) AS ordem_trimestral
  FROM `gglobo-audiencia-hdg-prd.prep_monitor_marcas_masterbrand.tb_consideracao`

  UNION ALL

  SELECT DISTINCT 
    ds_onda, 
    ds_periodo, 
    dt_mes_inicio, 
    CONCAT(EXTRACT(YEAR FROM dt_mes_inicio), EXTRACT(QUARTER FROM dt_mes_fim)) AS ordem_trimestral
  FROM `gglobo-audiencia-hdg-prd.prep_monitor_marcas_masterbrand.tb_nps`

  UNION ALL

  SELECT DISTINCT 
    ds_onda, 
    ds_periodo, 
    dt_mes_inicio, 
    CONCAT(EXTRACT(YEAR FROM dt_mes_inicio), EXTRACT(QUARTER FROM dt_mes_fim)) AS ordem_trimestral
  FROM `gglobo-audiencia-hdg-prd.prep_monitor_marcas_masterbrand.tb_familiaridade`

  UNION ALL

  SELECT DISTINCT 
    ds_onda, 
    ds_periodo, 
    dt_mes_inicio, 
    CONCAT(EXTRACT(YEAR FROM dt_mes_inicio), EXTRACT(QUARTER FROM dt_mes_fim)) AS ordem_trimestral
  FROM `gglobo-audiencia-hdg-prd.prep_monitor_marcas_masterbrand.tb_preferencia`
)
SELECT DISTINCT 
  ds_onda, 
  ordem_trimestral, 
  CASE  
    WHEN ds_onda = "Jul'2022" THEN 2  
    ELSE COUNT(DISTINCT(ds_periodo))  
  END AS qnt_trimestres 
FROM TRIMESTRAL
GROUP BY ALL
ORDER BY ordem_trimestral ASC;
```

### **Descrição:**
```
Tabela contendo os trimestres das pesquisas (`ds_onda`), a ordem dos trimestres e a quantidade de trimestres por onda dos indicadores **não proprietários**. Dados são extraídos das tabelas: `tb_familiaridade`, `tb_preferencia`, `tb_afinidade`, `tb_necessidades`, `tb_diferente`, `tb_dita_tendencias`, `tb_confianca`, `tb_consideracao`, `tb_nps`.
```

---

## Query: tb_filtro_semestral_nao_proprietario

```sql
WITH SEMESTRAL AS (
  SELECT DISTINCT 
    ds_periodo, 
    dt_mes_inicio, 
    CASE
      WHEN ds_periodo = "Jul'2022" THEN ds_onda
      WHEN ds_periodo IN ("Ago'2022-Out'2022", "Nov'2022", "Dez'2022") THEN "Ago'2022-Dez'2022"
      WHEN EXTRACT(MONTH FROM dt_entrevista) IN (1,2,3,4,5,6) THEN CONCAT("Jan'", EXTRACT(YEAR FROM dt_entrevista), "-Jun'", EXTRACT(YEAR FROM dt_entrevista))
      ELSE CONCAT("Jul'", EXTRACT(YEAR FROM dt_entrevista), "-Dez'", EXTRACT(YEAR FROM dt_entrevista))
    END AS semestre,
    CASE
      WHEN ds_periodo = "Jul'2022" THEN dt_mes_inicio
      WHEN ds_periodo IN ("Ago'2022-Out'2022", "Nov'2022", "Dez'2022") THEN DATE(EXTRACT(YEAR FROM dt_entrevista),8,1)
      WHEN EXTRACT(MONTH FROM dt_entrevista) IN (1,2,3,4,5,6) THEN DATE(EXTRACT(YEAR FROM dt_entrevista),1,1)
      ELSE DATE(EXTRACT(YEAR FROM dt_entrevista),7,1)
    END AS ordem_semestral
  FROM `gglobo-audiencia-hdg-prd.prep_monitor_marcas_masterbrand.tb_afinidade`

  UNION ALL

  SELECT DISTINCT 
    ds_periodo, 
    dt_mes_inicio, 
    CASE
      WHEN ds_periodo = "Jul'2022" THEN ds_onda
      WHEN ds_periodo IN ("Ago'2022-Out'2022", "Nov'2022", "Dez'2022") THEN "Ago'2022-Dez'2022"
      WHEN EXTRACT(MONTH FROM dt_entrevista) IN (1,2,3,4,5,6) THEN CONCAT("Jan'", EXTRACT(YEAR FROM dt_entrevista), "-Jun'", EXTRACT(YEAR FROM dt_entrevista))
      ELSE CONCAT("Jul'", EXTRACT(YEAR FROM dt_entrevista), "-Dez'", EXTRACT(YEAR FROM dt_entrevista))
    END AS semestre,
    CASE
      WHEN ds_periodo = "Jul'2022" THEN dt_mes_inicio
      WHEN ds_periodo IN ("Ago'2022-Out'2022", "Nov'2022", "Dez'2022") THEN DATE(EXTRACT(YEAR FROM dt_entrevista),8,1)
      WHEN EXTRACT(MONTH FROM dt_entrevista) IN (1,2,3,4,5,6) THEN DATE(EXTRACT(YEAR FROM dt_entrevista),1,1)
      ELSE DATE(EXTRACT(YEAR FROM dt_entrevista),7,1)
    END AS ordem_semestral
  FROM `gglobo-audiencia-hdg-prd.prep_monitor_marcas_masterbrand.tb_necessidades`

  UNION ALL

  SELECT DISTINCT 
    ds_periodo, 
    dt_mes_inicio, 
    CASE
      WHEN ds_periodo = "Jul'2022" THEN ds_onda
      WHEN ds_periodo IN ("Ago'2022-Out'2022", "Nov'2022", "Dez'2022") THEN "Ago'2022-Dez'2022"
      WHEN EXTRACT(MONTH FROM dt_entrevista) IN (1,2,3,4,5,6) THEN CONCAT("Jan'", EXTRACT(YEAR FROM dt_entrevista), "-Jun'", EXTRACT(YEAR FROM dt_entrevista))
      ELSE CONCAT("Jul'", EXTRACT(YEAR FROM dt_entrevista), "-Dez'", EXTRACT(YEAR FROM dt_entrevista))
    END AS semestre,
    CASE
      WHEN ds_periodo = "Jul'2022" THEN dt_mes_inicio
      WHEN ds_periodo IN ("Ago'2022-Out'2022", "Nov'2022", "Dez'2022") THEN DATE(EXTRACT(YEAR FROM dt_entrevista),8,1)
      WHEN EXTRACT(MONTH FROM dt_entrevista) IN (1,2,3,4,5,6) THEN DATE(EXTRACT(YEAR FROM dt_entrevista),1,1)
      ELSE DATE(EXTRACT(YEAR FROM dt_entrevista),7,1)
    END AS ordem_semestral
  FROM `gglobo-audiencia-hdg-prd.prep_monitor_marcas_masterbrand.tb_diferente`

  UNION ALL

  SELECT DISTINCT 
    ds_periodo, 
    dt_mes_inicio, 
    CASE
      WHEN ds_periodo = "Jul'2022" THEN ds_onda
      WHEN ds_periodo IN ("Ago'2022-Out'2022", "Nov'2022", "Dez'2022") THEN "Ago'2022-Dez'2022"
      WHEN EXTRACT(MONTH FROM dt_entrevista) IN (1,2,3,4,5,6) THEN CONCAT("Jan'", EXTRACT(YEAR FROM dt_entrevista), "-Jun'", EXTRACT(YEAR FROM dt_entrevista))
      ELSE CONCAT("Jul'", EXTRACT(YEAR FROM dt_entrevista), "-Dez'", EXTRACT(YEAR FROM dt_entrevista))
    END AS semestre,
    CASE
      WHEN ds_periodo = "Jul'2022" THEN dt_mes_inicio
      WHEN ds_periodo IN ("Ago'2022-Out'2022", "Nov'2022", "Dez'2022") THEN DATE(EXTRACT(YEAR FROM dt_entrevista),8,1)
      WHEN EXTRACT(MONTH FROM dt_entrevista) IN (1,2,3,4,5,6) THEN DATE(EXTRACT(YEAR FROM dt_entrevista),1,1)
      ELSE DATE(EXTRACT(YEAR FROM dt_entrevista),7,1)
    END AS ordem_semestral
  FROM `gglobo-audiencia-hdg-prd.prep_monitor_marcas_masterbrand.tb_dita_tendencias`

  UNION ALL

  SELECT DISTINCT 
    ds_periodo, 
    dt_mes_inicio, 
    CASE
      WHEN ds_periodo = "Jul'2022" THEN ds_onda
      WHEN ds_periodo IN ("Ago'2022-Out'2022", "Nov'2022", "Dez'2022") THEN "Ago'2022-Dez'2022"
      WHEN EXTRACT(MONTH FROM dt_entrevista) IN (1,2,3,4,5,6) THEN CONCAT("Jan'", EXTRACT(YEAR FROM dt_entrevista), "-Jun'", EXTRACT(YEAR FROM dt_entrevista))
      ELSE CONCAT("Jul'", EXTRACT(YEAR FROM dt_entrevista), "-Dez'", EXTRACT(YEAR FROM dt_entrevista))
    END AS semestre,
    CASE
      WHEN ds_periodo = "Jul'2022" THEN dt_mes_inicio
      WHEN ds_periodo IN ("Ago'2022-Out'2022", "Nov'2022", "Dez'2022") THEN DATE(EXTRACT(YEAR FROM dt_entrevista),8,1)
      WHEN EXTRACT(MONTH FROM dt_entrevista) IN (1,2,3,4,5,6) THEN DATE(EXTRACT(YEAR FROM dt_entrevista),1,1)
      ELSE DATE(EXTRACT(YEAR FROM dt_entrevista),7,1)
    END AS ordem_semestral
  FROM `gglobo-audiencia-hdg-prd.prep_monitor_marcas_masterbrand.tb_confianca`

  UNION ALL

  SELECT DISTINCT 
    ds_periodo, 
    dt_mes_inicio, 
    CASE
      WHEN ds_periodo = "Jul'2022" THEN ds_onda
      WHEN ds_periodo IN ("Ago'2022-Out'2022", "Nov'2022", "Dez'2022") THEN "Ago'2022-Dez'2022"
      WHEN EXTRACT(MONTH FROM dt_entrevista) IN (1,2,3,4,5,6) THEN CONCAT("Jan'", EXTRACT(YEAR FROM dt_entrevista), "-Jun'", EXTRACT(YEAR FROM dt_entrevista))
      ELSE CONCAT("Jul'", EXTRACT(YEAR FROM dt_entrevista), "-Dez'", EXTRACT(YEAR FROM dt_entrevista))
    END AS semestre,
    CASE
      WHEN ds_periodo = "Jul'2022" THEN dt_mes_inicio
      WHEN ds_periodo IN ("Ago'2022-Out'2022", "Nov'2022", "Dez'2022") THEN DATE(EXTRACT(YEAR FROM dt_entrevista),8,1)
      WHEN EXTRACT(MONTH FROM dt_entrevista) IN (1,2,3,4,5,6) THEN DATE(EXTRACT(YEAR FROM dt_entrevista),1,1)
      ELSE DATE(EXTRACT(YEAR FROM dt_entrevista),7,1)
    END AS ordem_semestral
  FROM `gglobo-audiencia-hdg-prd.prep_monitor_marcas_masterbrand.tb_consideracao`

  UNION ALL

  SELECT DISTINCT 
    ds_periodo, 
    dt_mes_inicio, 
    CASE
      WHEN ds_periodo = "Jul'2022" THEN ds_onda
      WHEN ds_periodo IN ("Ago'2022-Out'2022", "Nov'2022", "Dez'2022") THEN "Ago'2022-Dez'2022"
      WHEN EXTRACT(MONTH FROM dt_entrevista) IN (1,2,3,4,5,6) THEN CONCAT("Jan'", EXTRACT(YEAR FROM dt_entrevista), "-Jun'", EXTRACT(YEAR FROM dt_entrevista))
      ELSE CONCAT("Jul'", EXTRACT(YEAR FROM dt_entrevista), "-Dez'", EXTRACT(YEAR FROM dt_entrevista))
    END AS semestre,
    CASE
      WHEN ds_periodo = "Jul'2022" THEN dt_mes_inicio
      WHEN ds_periodo IN ("Ago'2022-Out'2022", "Nov'2022", "Dez'2022") THEN DATE(EXTRACT(YEAR FROM dt_entrevista),8,1)
      WHEN EXTRACT(MONTH FROM dt_entrevista) IN (1,2,3,4,5,6) THEN DATE(EXTRACT(YEAR FROM dt_entrevista),1,1)
      ELSE DATE(EXTRACT(YEAR FROM dt_entrevista),7,1)
    END AS ordem_semestral
  FROM `gglobo-audiencia-hdg-prd.prep_monitor_marcas_masterbrand.tb_nps`

  UNION ALL

  SELECT DISTINCT 
    ds_periodo, 
    dt_mes_inicio, 
    CASE
      WHEN ds_periodo = "Jul'2022" THEN ds_onda
      WHEN ds_periodo IN ("Ago'2022-Out'2022", "Nov'2022", "Dez'2022") THEN "Ago'2022-Dez'2022"
      WHEN EXTRACT(MONTH FROM dt_entrevista) IN (1,2,3,4,5,6) THEN CONCAT("Jan'", EXTRACT(YEAR FROM dt_entrevista), "-Jun'", EXTRACT(YEAR FROM dt_entrevista))
      ELSE CONCAT("Jul'", EXTRACT(YEAR FROM dt_entrevista), "-Dez'", EXTRACT(YEAR FROM dt_entrevista))
    END AS semestre,
    CASE
      WHEN ds_periodo = "Jul'2022" THEN dt_mes_inicio
      WHEN ds_periodo IN ("Ago'2022-Out'2022", "Nov'2022", "Dez'2022") THEN DATE(EXTRACT(YEAR FROM dt_entrevista),8,1)
      WHEN EXTRACT(MONTH FROM dt_entrevista) IN (1,2,3,4,5,6) THEN DATE(EXTRACT(YEAR FROM dt_entrevista),1,1)
      ELSE DATE(EXTRACT(YEAR FROM dt_entrevista),7,1)
    END AS ordem_semestral
  FROM `gglobo-audiencia-hdg-prd.prep_monitor_marcas_masterbrand.tb_familiaridade`

UNION ALL

  SELECT DISTINCT 
    ds_periodo, 
    dt_mes_inicio, 
    CASE
      WHEN ds_periodo = "Jul'2022" THEN ds_onda
      WHEN ds_periodo IN ("Ago'2022-Out'2022", "Nov'2022", "Dez'2022") THEN "Ago'2022-Dez'2022"
      WHEN EXTRACT(MONTH FROM dt_entrevista) IN (1,2,3,4,5,6) THEN CONCAT("Jan'", EXTRACT(YEAR FROM dt_entrevista), "-Jun'", EXTRACT(YEAR FROM dt_entrevista))
      ELSE CONCAT("Jul'", EXTRACT(YEAR FROM dt_entrevista), "-Dez'", EXTRACT(YEAR FROM dt_entrevista))
    END AS semestre,
    CASE
      WHEN ds_periodo = "Jul'2022" THEN dt_mes_inicio
      WHEN ds_periodo IN ("Ago'2022-Out'2022", "Nov'2022", "Dez'2022") THEN DATE(EXTRACT(YEAR FROM dt_entrevista),8,1)
      WHEN EXTRACT(MONTH FROM dt_entrevista) IN (1,2,3,4,5,6) THEN DATE(EXTRACT(YEAR FROM dt_entrevista),1,1)
      ELSE DATE(EXTRACT(YEAR FROM dt_entrevista),7,1)
    END AS ordem_semestral
  FROM `gglobo-audiencia-hdg-prd.prep_monitor_marcas_masterbrand.tb_preferencia`
)
SELECT 
  semestre, 
  ordem_semestral, 
  CASE  
    WHEN semestre = "Jul'2022" THEN 2  
    ELSE COUNT(DISTINCT(ds_periodo))  
  END AS qnt_trimestres 
FROM SEMESTRAL
GROUP BY ALL;
```

**Descrição:**
```
Tabela contendo os semestres, a ordem dos semestres e a quantidade de trimestres que compõe aquele semestre encontrados na base dos indicadores não proprietários (tb_familiaridade, tb_preferencia, tb_afinidade, tb_necessidades, tb_diferente, tb_dita_tendencias, tb_confianca, tb_consideracao, tb_nps.). 
```

## Dashboards Amor à Marca

Nomes alternativos do indicador: "Afinidade".

Tabela no BigQuery: "tb_necessidades"

Diagrama de relacionamento da tb_afinidade no Power BI

![Imagem](documentacao/imagem9.png)

Aba: Afinidade – Multi Brand Gráficos

![Imagem](documentacao/imagem10.png)

Aba: Afinidade – Multi Brand Tabela

![Imagem](documentacao/imagem11.png)

Aba: Afinidade – Multi Period Gráficos

![Imagem](documentacao/imagem12.png)

Aba: Afinidade – Multi Period Tabela

![Imagem](documentacao/imagem13.png)

### Fórmulas Dax Amor á Marca

**Legenda Abas:**  
**MBG** – Multi Brand Gráficos  
**MBT** – Multi Brand Tabela  
**MPG** – Multi Period Gráficos  
**MPT** – Multi Period Tabela  
**EX** – Exportação

---

### Nome Campo: Qtd de Pessoas
**Aba:** MBG  
**Fórmula DAX:**
```DAX
DISTINCTCOUNT(tb_afinidade[cd_pessoa])
```

**Descrição:** 
```
Calcula quantidade de pessoas que responderam ao questionário (Respondentes). Utilizado frequentemente para medir a base de pessoas da pesquisa em um período.
```
---

### Nome Campo: % Top2box
**Aba:** MBG  
**Fórmula DAX:**
```DAX
Var QtdPessoas = [Qtd de Pessoas]
Var TotalPessoas = CALCULATE(COUNT(tb_afinidade[cd_pessoa]), tb_afinidade[cd_resposta] in {6,7})
Return DIVIDE(TotalPessoas, QtdPessoas, 0)
```
**Descrição:** 
```
Calcula percentual de respostas mais positivas ("6" ou "7 - Eu amo") em relação ao total de respondentes. Campo usado geralmente para ordenar gráficos.
```
---

### Nome Campo: % Eu Amo
**Aba:** MBG  
**Fórmula DAX:**
```DAX
Var QtdPessoas = [Qtd de Pessoas]
Var TotalPessoas = CALCULATE(COUNT(tb_afinidade[cd_pessoa]), tb_afinidade[cd_resposta] = 7)
Return DIVIDE(TotalPessoas, QtdPessoas, 0)
```
**Descrição:** 
```
Calcula o percentual de pessoas que responderam nota máxima ("7 - Eu amo") no questionário.
```
---

### Nome Campo: % Participação Respostas
**Aba:** MBG  
**Fórmula DAX:**
```DAX
Var QtdPessoas = IF(ISBLANK([Qtd de Pessoas]), 0, [Qtd de Pessoas])
Var TotalPessoas = CALCULATE([Qtd de Pessoas], ALL('tb_afinidade'[ds_resposta], 'tb_afinidade'[cd_resposta]))
Return DIVIDE(QtdPessoas, TotalPessoas, 0)
```
**Descrição:** 
```
Calcula o percentual de participação de cada resposta entre todos os respondentes.
``` 
--- 

### Nome Campo: nw_ds_classificacao_expl
**Aba:** MBG  
**Fórmula DAX:** 
```
(campo auxiliar, sem fórmula associada)
```
**Descrição:** 
```
Campo descritivo usado como dimensão nas análises.
``` 
---

### Nome Campo: % Participação Top2NW
**Aba:** MBG  
**Fórmula DAX:**
```DAX
Var QtdPessoas = IF(ISBLANK([Qtd de Pessoas]), 0, [Qtd de Pessoas])
Var TotalPessoas = CALCULATE([Qtd de Pessoas], ALL('tb_afinidade'[nw_ds_classificacao_expl], 'tb_afinidade'[nw_cd_classificacao_expl]))
Return COALESCE(DIVIDE(QtdPessoas, TotalPessoas, 0), 0)
```
**Descrição:** 
```
Calcula a participação das respostas agrupadas por classificação (Top2box, Neutros, Top2bottom) sobre o total selecionado.
``` 
---

### Nome Campo: Qtd de Pessoas 0
**Aba:** MBG  
**Fórmula DAX:**
```DAX
IF(ISBLANK(DISTINCTCOUNT(tb_afinidade[cd_pessoa])), 0, DISTINCTCOUNT(tb_afinidade[cd_pessoa]))
```
**Descrição:** 
```
Versão segura do campo Qtd de Pessoas para evitar valores nulos.
``` 

---

### Nome Campo: Qtd de Pessoas Formatada
**Aba:** MBG  
**Fórmula DAX:**
```DAX
Var QndPessoas = [Qtd de Pessoas]
Var Formatacao =
    SWITCH(TRUE(),
        ([% Participação Respostas] < 0.005), "#999999",
        ([*** Afinidade] < 0.005), "#999999",
        SELECTEDVALUE(tb_afinidade[cd_resposta]) in {1,2}, "#EE4549",
        SELECTEDVALUE(tb_afinidade[cd_resposta]) in {3,4,5}, "#1B1B1B",
        SELECTEDVALUE(tb_afinidade[cd_resposta]) in {6,7}, "#3BB537",
        "#999999")
Return Formatacao
```
**Descrição:**
```
Define a cor para o valor de Qtd de Pessoas baseado em regras de classificação e participação.
``` 
---

### Nome Campo: Qtd de Pessoas Formatada Top2
**Aba:** MBG  
**Fórmula DAX:**
```DAX
Var Formatacao =
    SWITCH(TRUE(),
        SELECTEDVALUE('Parâmetro Afinidade'[Parâmetro Afinidade Pedido]) = BLANK(), "#0ffffff",
        ([% Participação Top2NW] < 0.005), "#999999",
        ([* Afinidade] < 0.005), "#999999",
        SELECTEDVALUE(tb_afinidade[ds_classificacao_expl]) = "TOP2BOTTOM", "#EE4549",
        SELECTEDVALUE(tb_afinidade[ds_classificacao_expl]) = "Outros", "#1B1B1B",
        SELECTEDVALUE(tb_afinidade[ds_classificacao_expl]) = "Neutros", "#1B1B1B",
        SELECTEDVALUE(tb_afinidade[ds_classificacao_expl]) = "TOP2BOX", "#3BB537",
        "#999999")
Return Formatacao
```
**Descrição:** 
```
Define a cor para o valor da classificação Top2 com base nos parâmetros e na classificação da resposta.
``` 
---

### Nome Campo: % Participação Top2
**Aba:** MBG  
**Fórmula DAX:**
```DAX
Var QtdPessoas = [Qtd de Pessoas]
Var TotalPessoas = CALCULATE([Qtd de Pessoas], ALL('tb_afinidade'[ds_classificacao_expl], 'tb_afinidade'[cd_classificacao_expl]))
Return DIVIDE(QtdPessoas, TotalPessoas, 0)
```
**Descrição:** 
```
Calcula a proporção da classificação Top2 em relação ao total de respondentes.
``` 
---

### Nome Campo: * Afinidade
**Aba:** MBG  
**Fórmula DAX:**
```DAX
VAR total = CALCULATE([
    Qtd de Pessoas 0],
    ALLSELECTED('tb_afinidade'[cd_classificacao_expl]),
    ALLSELECTED('tb_afinidade'[ds_classificacao_expl]))
RETURN SWITCH(TRUE(),
    SELECTEDVALUE('Parâmetro Afinidade'[Parâmetro Afinidade Pedido]) = 2,
        CALCULATE(DIVIDE([Qtd de pessoas 0], total, 0), tb_filtro_semestral_nao_proprietario[semestre] <> BLANK()),
    SELECTEDVALUE('Parâmetro Afinidade'[Parâmetro Afinidade Pedido]) = 3,
        DIVIDE([Qtd de Pessoas 0], total, 0))
```
**Descrição:** 
```
Calcula o percentual de respondentes por classificação levando em conta o parâmetro selecionado.
``` 
---

### Nome Campo: ** Afinidade
**Aba:** MBG  
**Fórmula DAX:**
```DAX
SWITCH(TRUE(),
    SELECTEDVALUE('Parâmetro Afinidade'[Parâmetro Afinidade Pedido]) = 2,
        CALCULATE([Qtd de Pessoas 0], tb_filtro_semestral_nao_proprietario[semestre] <> BLANK()),
    SELECTEDVALUE('Parâmetro Afinidade'[Parâmetro Afinidade Pedido]) = 3,
        [Qtd de Pessoas 0])
```
**Descrição:** 
```
Traz a quantidade de pessoas respondentes com base na lógica de parâmetro do período.
``` 
---

### Nome Campo: *** Afinidade
**Aba:** MBG  
**Fórmula DAX:**
```DAX
VAR total = CALCULATE([
    Qtd de pessoas 0],
    ALLSELECTED('tb_afinidade'[ds_resposta]),
    ALLSELECTED('tb_afinidade'[cd_resposta]))
RETURN SWITCH(TRUE(),
    SELECTEDVALUE('Parâmetro Afinidade'[Parâmetro Afinidade Pedido]) = 2,
        CALCULATE(DIVIDE([Qtd de Pessoas 0], total, 0), tb_filtro_semestral_nao_proprietario[semestre] <> BLANK()),
    SELECTEDVALUE('Parâmetro Afinidade'[Parâmetro Afinidade Pedido]) = 3,
        DIVIDE([Qtd de Pessoas 0], total, 0))
```
**Descrição:** 
```
Calcula a participação por resposta, respeitando o filtro de parâmetro de afinidade.
``` 
---

### Nome Campo: CorBaseAfinidade
**Aba:** MBG  
**Fórmula DAX:**
```DAX
Var vlCorBaseA = SWITCH(TRUE(),
    tb_afinidade[Qtd de Pessoas] >= 70, "#1C1C1C",
    "#DB082C")
Return vlCorBaseA
```
**Descrição:** 
```
Aplica uma formatação condicional de cor com base no número de respondentes.
``` 

### Nome Campo: % Participacao Base
**Aba:** MBG  
**Fórmula DAX:**
```DAX
VAR qnt_pessoas = [Qtd de Pessoas]
VAR total = CALCULATE([
    Qtd de Pessoas],
    ALLSELECTED('tb_afinidade'[ds_resposta]),
    ALLSELECTED('tb_afinidade'[cd_resposta]),
    ALLSELECTED('tb_afinidade'[ds_classificacao_expl]),
    ALLSELECTED('tb_afinidade'[cd_classificacao_expl]))
RETURN SWITCH(TRUE(),
    SELECTEDVALUE('Parâmetro Afinidade'[Parâmetro Afinidade Pedido]) = 2,
        CALCULATE(DIVIDE([Qtd de Pessoas], total, 0), tb_filtro_semestral_nao_proprietario[semestre] <> BLANK()),
    SELECTEDVALUE('Parâmetro Afinidade'[Parâmetro Afinidade Pedido]) = 3,
        DIVIDE([Qtd de Pessoas], total, 0))
```
**Descrição:** 
```
Percentual da base de respondentes considerando filtros de afinidade e parâmetros semestrais.
``` 
---


## Dashboards Atende às Necessidades

Nomes alternativos do indicador: "Atende as minhas necessidades", "Necessidades".

Tabela no BigQuery: "tb_necessidades"

Diagrama de relacionamento da tb_necessidades no Power BI

![Imagem](documentacao/imagem14.png)

Aba: AtendeNecessidades – Multi Brand Gráficos

![Imagem](documentacao/imagem15.png)

Aba: AtendeNecessidades – Multi Brand Tabela

![Imagem](documentacao/imagem16.png)

Aba: AtendeNecessidades – Multi Period Gráficos

![Imagem](documentacao/imagem18.png)

Aba: AtendeNecessidades – Multi Period Tabela

![Imagem](documentacao/imagem19.png)

### Fórmulas Dax Atende às necessidades

**Legenda Abas:**  
**MBG** – Multi Brand Gráficos  
**MBT** – Multi Brand Tabela  
**MPG** – Multi Period Gráficos  
**MPT** – Multi Period Tabela  
**EX** – Exportação

---

### Nome Campo: Qtd de PessoasN  
**Aba:** MBG  
**Fórmula DAX:**
```DAX
DISTINCTCOUNT(tb_necessidades[cd_pessoa])
```
**Descrição:**  
```
Calcula quantidade de pessoas que responderam ao questionário (Respondentes). Utilizado frequentemente para medir a base de pessoas da pesquisa em um período.
```

---

### Nome Campo: % Top2box N  
**Aba:** MBG  
**Fórmula DAX:**
```DAX
Var QtdPessoas = [Qtd de PessoasN]    
Var TotalPessoas = CALCULATE(COUNT(tb_necessidades[cd_pessoa]), tb_necessidades[cd_resposta] in {6,7})  
Return DIVIDE(TotalPessoas, QtdPessoas, 0)
```
**Descrição:**  
```
Calcula percentual de respostas mais positivas, “6” ou “7 - Atende muito bem as minhas necessidades”, do questionário em relação ao total de respondentes. Campo usado geralmente para ordenar gráficos.
```

---

### Nome Campo: % Atende muito bem  
**Aba:** MBG  
**Fórmula DAX:**
```DAX
Var QtdPessoas = [Qtd de PessoasN]    
Var TotalPessoas = CALCULATE(COUNT(tb_necessidades[cd_pessoa]), tb_necessidades[cd_resposta] = 7)  
Return DIVIDE(TotalPessoas, QtdPessoas, 0)
```
**Descrição:**  
```
Calcula percentual da resposta “7 - Atende muito bem as minhas necessidades” do questionário em relação ao total de respondentes. Campo usado geralmente para ordenar gráficos.
```

---

### Nome Campo: % Participação Atende  
**Aba:** MBT  
**Fórmula DAX:**
```DAX
Var QtdPessoas = [Qtd de PessoasN 0]  
Var TotalPessoas = CALCULATE([Qtd de PessoasN], ALL('tb_necessidades'[ds_resposta], 'tb_necessidades'[cd_resposta]))  
Return DIVIDE(QtdPessoas, TotalPessoas, 0)
```
**Descrição:**  
```
Calcula percentual de cada resposta do questionário em relação ao total de respondentes. Se os filtros aplicados não gerarem dados para o cálculo, ele retorna 0.
```

---

### Nome Campo: % ParticipaçãoN Top2NW  
**Aba:** MBT  
**Fórmula DAX:**
```DAX
Var QtdPessoas = [Qtd de PessoasN 0]  
Var TotalPessoas = CALCULATE([Qtd de PessoasN], ALL('tb_necessidades'[nw_ds_classificacao_expl], 'tb_necessidades'[nw_cd_classificacao_expl]))  
Return DIVIDE(QtdPessoas, TotalPessoas, 0)
```
**Descrição:**  
```
Calcula percentual de cada classificação (Top2box, Neutros, Top2bottom) em relação ao total de respondentes, com ordenação baseada nos campos auxiliares nw_*.
```

---

### Nome Campo: Qtd de PessoasN 0  
**Aba:** MBT  
**Fórmula DAX:**
```DAX
IF(ISBLANK(DISTINCTCOUNT(tb_necessidades[cd_pessoa])), 0, DISTINCTCOUNT(tb_necessidades[cd_pessoa]))
```
**Descrição:**  
```
Versão segura da Qtd de Pessoas para evitar valores nulos. Retorna 0 quando não houver respondentes filtrados.
```
---

### Nome Campo: Qtd de PessoasN Formatada  
**Aba:** MBT MPT  
**Fórmula DAX:**
```DAX
Var Formatacao =  
    SWITCH(TRUE(), 
        ([% Participação Atende] < 0.005), "#999999", 
        ([*** Necessidades]  < 0.005), "#999999", 
        SELECTEDVALUE(tb_necessidades[cd_resposta]) in {1,2}, "#EE4549", 
        SELECTEDVALUE(tb_necessidades[cd_resposta]) in {3,4,5}, "#1C1C1C", 
        SELECTEDVALUE(tb_necessidades[cd_resposta]) in {6,7}, "#3BB537", 
        "#999999")  
Return Formatacao
```
**Descrição:**  
```
Regra de formatação aplicada para as matrizes contendo os percentuais de cada resposta do indicador. Percentuais das respostas mais positivas em cor verde, neutras em preto e menos positivas em vermelho. Todos os zeros em cinza.
```

---

### Nome Campo: Qtd de PessoasN Formatada Top2NW  
**Aba:** MBT MPT  
**Fórmula DAX:**
```DAX
Var Formatacao =  
    SWITCH(TRUE(), 
        ([% ParticipaçãoN Top2NW] < 0.005), "#999999", 
        ([* Necessidades]  < 0.005), "#999999", 
        SELECTEDVALUE(tb_necessidades[nw_ds_classificacao_expl]) = "TOP2BOTTOM", "#EE4549", 
        SELECTEDVALUE(tb_necessidades[nw_ds_classificacao_expl]) = "Neutros", "#1B1B1B", 
        SELECTEDVALUE(tb_necessidades[nw_ds_classificacao_expl]) = "TOP2BOX", "#3BB537", 
        "#999999")  
Return Formatacao
```
**Descrição:**  
```
Regra de formatação aplicada para as matrizes contendo os percentuais de classificação de resposta do indicador (Top2box, Top2bottom, Neutros). Percentuais das respostas mais positivas em cor verde, neutras em preto e menos positivas em vermelho. Todos os zeros em cinza.
```

---

### Nome Campo: % ParticipaçãoN Top2  
**Aba:** MPG  
**Fórmula DAX:**
```DAX
Var QtdPessoas = [Qtd de PessoasN]  
Var TotalPessoas = CALCULATE([Qtd de PessoasN], ALL('tb_necessidades'[ds_classificacao_expl], 'tb_necessidades'[cd_classificacao_expl]))  
Return DIVIDE(QtdPessoas, TotalPessoas, 0)
```
**Descrição:**  
```
Calcula percentual de cada classificação (Top2box, Top2bottom, Neutros) das respostas do indicador em relação ao total de respondentes. Baseado no campo ds_classificacao_expl.
```

---

### Nome Campo: * Necessidades  
**Aba:** MPT  
**Fórmula DAX:**
```DAX
VAR total = 
    CALCULATE([Qtd de PessoasN 0], ALLSELECTED('tb_necessidades'[ds_classificacao_expl]), ALLSELECTED('tb_necessidades'[cd_classificacao_expl]))
RETURN 
    SWITCH(TRUE(), 
        SELECTEDVALUE('Parâmetro Necessidades'[Parâmetro Pedido]) = 2,
            CALCULATE(DIVIDE([Qtd de PessoasN 0], total, 0), tb_filtro_semestral_nao_proprietario[semestre] <> BLANK()),
        SELECTEDVALUE('Parâmetro Necessidades'[Parâmetro Pedido]) = 3,
            DIVIDE([Qtd de PessoasN 0], total, 0))
```
**Descrição:**  
```
Calcula percentual de cada classificação do questionário em relação ao total de respondentes (Base). Exclui períodos em branco. Criado para uso em matriz multiperíodo.
```

---

### Nome Campo: ** Necessidades  
**Aba:** MPT  
**Fórmula DAX:**
```DAX
SWITCH(TRUE(),
    SELECTEDVALUE('Parâmetro Necessidades'[Parâmetro Pedido]) = 2,
        CALCULATE([Qtd de PessoasN 0], tb_filtro_semestral_nao_proprietario[semestre] <> BLANK()),
    SELECTEDVALUE('Parâmetro Necessidades'[Parâmetro Pedido]) = 3,
        [Qtd de PessoasN 0])
```
**Descrição:**  
```
Calcula quantidade de pessoas que responderam ao questionário no período selecionado (Base). Exclui períodos em branco.
```

---

### Nome Campo: *** Necessidades  
**Aba:** MPT  
**Fórmula DAX:**
```DAX
VAR qnt_pessoas = [Qtd de PessoasN]
VAR total = 
    CALCULATE([Qtd de PessoasN 0], ALLSELECTED('tb_necessidades'[ds_resposta]), ALLSELECTED('tb_necessidades'[cd_resposta]))
RETURN 
    SWITCH(TRUE(),
        SELECTEDVALUE('Parâmetro Necessidades'[Parâmetro Pedido]) = 2,
            CALCULATE(DIVIDE([Qtd de PessoasN 0], total, 0), tb_filtro_semestral_nao_proprietario[semestre] <> BLANK()),
        SELECTEDVALUE('Parâmetro Necessidades'[Parâmetro Pedido]) = 3,
            DIVIDE([Qtd de PessoasN 0], total, 0))
```
**Descrição:**  
```
Calcula percentual de pessoas que responderam cada opção de resposta (ds_resposta) no período selecionado. Exclui períodos em branco. Criado para uso em matriz multiperíodo.
```

---

### Nome Campo: CorBaseNecessidades  
**Aba:** ALL  
**Fórmula DAX:**
```DAX
Var vlCorBaseN =  
    SWITCH(TRUE(), 
        tb_necessidades[Qtd de PessoasN] > 70, "#1C1C1C", 
        "#DB082C")
Return vlCorBaseN
```
**Descrição:**  
```
Se o valor da Base de pessoas que responderam ao questionário for menor do que 70 então a cor do número de base deve ser vermelha para destacar.
```
---

## Dashboards Confiança

Tabela no BigQuery: "tb_confianca"

Diagrama de relacionamento da tb_confianca no Power BI

![Imagem](documentacao/imagem20.png)

Aba: Confiança – Multi Brand Gráficos

![Imagem](documentacao/imagem21.png)

Aba: Confiança – Multi Brand Tabela

![Imagem](documentacao/imagem22.png)

Aba: Confiança – Multi Period Gráficos

![Imagem](documentacao/imagem23.png)

Aba: Confiança – Multi Period Tabela

![Imagem](documentacao/imagem24.png)

### Fórmulas Dax Confiança

**Legenda Abas:**  
**MBG** – Multi Brand Gráficos  
**MBT** – Multi Brand Tabela  
**MPG** – Multi Period Gráficos  
**MPT** – Multi Period Tabela  
**EX** – Exportação

---

### Nome Campo: Qtd de Pessoas Cf  
**Aba:** MBG  
**Fórmula DAX:**
```DAX
DISTINCTCOUNT(tb_confianca[cd_pessoa])
```
**Descrição:**  
```
Calcula quantidade de pessoas que responderam ao questionário (Respondentes). Utilizado frequentemente para medir a Base de pessoas da pesquisa em um período.
```

---

### Nome Campo: % TOPBOX  
**Aba:** MBG  
**Fórmula DAX:**
```DAX
Var QtdPessoas = [Qtd de Pessoas Cf]    
Var TotalPessoas = CALCULATE(COUNT(tb_confianca[cd_pessoa]), tb_confianca[cd_resposta] = 7)  
Return DIVIDE(TotalPessoas, QtdPessoas, 0)
```
**Descrição:**  
```
Calcula percentual da resposta mais positiva “7 - Confio totalmente”, do indicador em relação ao total de respondentes. Campo usado geralmente para ordenar gráficos. Exceção do indicador Confiança que utiliza apenas Topbox.
```

---

### Nome Campo: % Participação Confiança 0  
**Aba:** MBT  
**Fórmula DAX:**
```DAX
Var QtdPessoas = [Qtd de Pessoas Cf 0]  
Var TotalPessoas = CALCULATE([Qtd de Pessoas Cf], ALL('tb_confianca'[ds_resposta], 'tb_confianca'[cd_resposta]))  
Return DIVIDE(QtdPessoas, TotalPessoas, 0)
```
**Descrição:**  
```
Calcula percentual de cada resposta do indicador em relação ao total de respondentes. Se os filtros aplicados não gerarem dados para o cálculo, ele retorna 0.
```

---

### Nome Campo: Qtd de Pessoas Cf 0  
**Aba:** MBT  
**Fórmula DAX:**
```DAX
IF(ISBLANK(DISTINCTCOUNT(tb_confianca[cd_pessoa])), 0, DISTINCTCOUNT(tb_confianca[cd_pessoa]))
```
**Descrição:**  
```
Versão segura da Qtd de Pessoas Cf para evitar valores nulos.
```

---

### Nome Campo: Qtd de PessoasCf Formatada  
**Aba:** MBT MPT  
**Fórmula DAX:**
```DAX
Var QndPessoas = [Qtd de Pessoas Cf]  
Var Formatacao =  
    SWITCH(TRUE(), 
        ([% Participação Confiança 0] < 0.005), "#999999",  
        ([*** Confiança] < 0.005), "#999999", 
        SELECTEDVALUE(tb_confianca[cd_resposta]) in {1,2}, "#EE4549", 
        SELECTEDVALUE(tb_confianca[cd_resposta]) in {3,4,5}, "#1B1B1B", 
        SELECTEDVALUE(tb_confianca[cd_resposta]) in {6,7}, "#3BB537", "#999999")  
Return Formatacao
```
**Descrição:**  
```
Regra de formatação para matrizes com percentuais de resposta. Positivas em verde, neutras em preto e negativas em vermelho. Zeros em cinza.
```

---

### Nome Campo: % Participação Cf Top2  
**Aba:** MPG  
**Fórmula DAX:**
```DAX
Var QtdPessoas = [Qtd de Pessoas Cf]  
Var TotalPessoas = CALCULATE([Qtd de Pessoas Cf], ALL('tb_confianca'[nw_ds_top2], 'tb_confianca'[nw_cd_top2]))  
Return DIVIDE(QtdPessoas, TotalPessoas, 0)
```
**Descrição:**  
```
Calcula participação de classificações (Topbox, Neutros, Top2bottom) com ordenação customizada via campos nw_ds_top2/nw_cd_top2.
```

---

### Nome Campo: ** Confiança  
**Aba:** MPT  
**Fórmula DAX:**
```DAX
SWITCH( 
    TRUE(), 
    SELECTEDVALUE('Parâmetro Confiança'[Parâmetro Confiança Pedido]) = 2, 
        CALCULATE([Qtd de Pessoas Cf 0], tb_filtro_semestral_nao_proprietario[semestre] <> BLANK()), 
    SELECTEDVALUE('Parâmetro Confiança'[Parâmetro Confiança Pedido]) = 3, 
        [Qtd de Pessoas Cf 0]
)
```
**Descrição:**  
```
Retorna o número de respondentes com base no período selecionado. Ignora períodos sem dados.
```

---

### Nome Campo: *** Confiança  
**Aba:** MPT  
**Fórmula DAX:**
```DAX
VAR qnt_pessoas = [Qtd de Pessoas Cf]  
VAR total =  
    CALCULATE([Qtd de Pessoas Cf 0],  
        ALLSELECTED('tb_confianca'[ds_resposta]),  
        ALLSELECTED('tb_confianca'[cd_resposta]))  
RETURN  
    SWITCH(TRUE(),  
        SELECTEDVALUE('Parâmetro Confiança'[Parâmetro Confiança Pedido]) = 2,  
            CALCULATE(DIVIDE([Qtd de Pessoas Cf 0], total, 0), tb_filtro_semestral_nao_proprietario[semestre] <> BLANK()),  
        SELECTEDVALUE('Parâmetro Confiança'[Parâmetro Confiança Pedido]) = 3,  
            DIVIDE([Qtd de Pessoas Cf 0], total, 0))
```
**Descrição:**  
```
Calcula percentual de respostas por alternativa, baseado no parâmetro selecionado e respeitando o filtro de semestre.
```

---

### Nome Campo: CorBaseConfianca  
**Aba:** ALL  
**Fórmula DAX:**
```DAX
Var vlCorBaseCf =  
    SWITCH(TRUE(), 
        tb_confianca[Qtd de Pessoas Cf] >= 70, "#1C1C1C", 
        "#DB082C")  
Return vlCorBaseCf
```
**Descrição:**  
```
Aplica cor à base de respondentes: vermelho se inferior a 70 e preto caso contrário.
```

## Dashboards Consideração

Tabela no BigQuery: "tb_consideracao"

Diagrama de relacionamento da tb_afinidade no Power BI

![Imagem](documentacao/imagem25.png)

Aba: Consideração – Multi Brand Gráficos

![Imagem](documentacao/imagem26.png)

Aba: Consideração – Multi Brand Tabela

![Imagem](documentacao/imagem27.png)

Aba: Consideração – Multi Period Gráficos

![Imagem](documentacao/imagem28.png)

Aba: Consideração – Multi Period Tabela

![Imagem](documentacao/imagem29.png)

### Fórmulas Dax Consideração

**Legenda Abas:**  
**MBG** – Multi Brand Gráficos  
**MBT** – Multi Brand Tabela  
**MPG** – Multi Period Gráficos  
**MPT** – Multi Period Tabela  
**EX** – Exportação

---

### Nome Campo: Qtd de Pessoas Cs  
**Aba:** MBG  
**Fórmula DAX:**
```DAX
DISTINCTCOUNT(tb_consideracao[cd_pessoa])
```
**Descrição:**  
```
Calcula quantidade de pessoas que responderam ao questionário (Respondentes). Utilizado frequentemente para medir a Base de pessoas da pesquisa em um período.
```

---

### Nome Campo: % Top2box Cs  
**Aba:** MBG  
**Fórmula DAX:**
```DAX
Var QtdPessoas = [Qtd de Pessoas Cs]    
Var TotalPessoas = CALCULATE(COUNT(tb_consideracao[cd_pessoa]), tb_consideracao[cd_resposta] in {1,2} )  
Return DIVIDE((TotalPessoas),QtdPessoas,0)
```
**Descrição:**  
```
Calcula percentual de respostas mais positivas, “1 Seria a minha primeira escolha” ou “2 Eu consideraria seriamente”, do questionário em relação ao total de respondentes. Campo usado geralmente para ordenar gráficos.
```

---

### Nome Campo: % Minha primeira escolha  
**Aba:** MBG  
**Fórmula DAX:**
```DAX
Var QtdPessoas = [Qtd de Pessoas Cs]    
Var TotalPessoas = CALCULATE(COUNT(tb_consideracao[cd_pessoa]), tb_consideracao[cd_resposta] = 1 )  
Return DIVIDE((TotalPessoas),QtdPessoas,0)
```
**Descrição:**  
```
Calcula percentual da resposta “1 Seria a minha primeira escolha” do indicador em relação ao total de respondentes. Campo usado geralmente para ordenar gráficos.
```

---

### Nome Campo: % Participação Consideração 0  
**Aba:** MBT  
**Fórmula DAX:**
```DAX
Var QtdPessoas = [Qtd de Pessoas Cs 0]  
Var TotalPessoas = CALCULATE([Qtd de Pessoas Cs],ALL('tb_consideracao'[ds_resposta], 'tb_consideracao'[cd_resposta]))  
Return DIVIDE(QtdPessoas, TotalPessoas,0)
```
**Descrição:**  
```
Calcula percentual de cada resposta do indicador em relação ao total de respondentes. Se os filtros aplicados não gerarem dados para o cálculo, ele retorna 0.
```

---

### Nome Campo: % Participação Cs Top2 0  
**Aba:** MBT  
**Fórmula DAX:**
```DAX
Var QtdPessoas = [Qtd de Pessoas Cs 0]  
Var TotalPessoas = CALCULATE([Qtd de Pessoas Cs],ALL('tb_consideracao'[nw_ds_classificacao_expl], 'tb_consideracao'[nw_cd_classificacao_expl]))  
Return DIVIDE(QtdPessoas, TotalPessoas,0)
```
**Descrição:**  
```
Calcula percentual de cada classificação do indicador (Topbox, Eu poderia considerar, Eu não consideraria) em relação ao total de respondentes (Base). Se os filtros aplicados não gerarem dados para o cálculo, ele retorna 0.
```

---

### Nome Campo: Qtd de Pessoas Cs 0  
**Aba:** MBT  
**Fórmula DAX:**
```DAX
IF(ISBLANK(DISTINCTCOUNT(tb_consideracao[cd_pessoa])), 0, DISTINCTCOUNT(tb_consideracao[cd_pessoa]))
```
**Descrição:**  
```
Calcula quantidade de pessoas que responderam ao questionário (Respondentes). Se os filtros aplicados não gerarem dados para o cálculo, ele retorna 0.
```

---

### Nome Campo: Qtd de PessoasCs Formatada  
**Aba:** MBT, MPT  
**Fórmula DAX:**
```DAX
Var Formatacao =  
    SWITCH(TRUE(), 
        ([% Participação Consideração 0] < 0.005), "#999999",   
        ([*** Consideração]  < 0.005), "#999999", 
        SELECTEDVALUE(tb_consideracao[cd_resposta]) in {4}, "#EE4549", 
        SELECTEDVALUE(tb_consideracao[cd_resposta]) in {3}, "#1B1B1B", 
        SELECTEDVALUE(tb_consideracao[cd_resposta]) in {1,2}, "#3BB537", "#999999")  
Return Formatacao
```
**Descrição:**  
```
Aplica regras de cor às matrizes com base na classificação das respostas. Zeros em cinza, positivas em verde, neutras em preto e negativas em vermelho.
```

---

### Nome Campo: Qtd de Pessoas Cs Formatada Top2  
**Aba:** MBT, MPT  
**Fórmula DAX:**
```DAX
Var QndPessoas = [Qtd de Pessoas Cs]  
Var Formatacao =  
    SWITCH(TRUE(), 
        ([% Participação Cs Top2 0] < 0.005), "#999999",   
        ([* Consideração]  < 0.005), "#999999", 
        SELECTEDVALUE(tb_consideracao[nw_ds_classificacao_expl]) = "Eu não consideraria", "#EE4549", 
        SELECTEDVALUE(tb_consideracao[nw_ds_classificacao_expl]) = "Eu poderia considerar", "#1B1B1B", 
        SELECTEDVALUE(tb_consideracao[nw_ds_classificacao_expl]) = "TOPBOX", "#3BB537", "#999999")  
Return Formatacao
```
**Descrição:**  
```
Aplica regras de cor às matrizes para classificações alternativas do indicador (TOPBOX, Eu poderia considerar, Eu não consideraria).
```

---

### Nome Campo: % Participação Cs Top2  
**Aba:** MPG  
**Fórmula DAX:**
```DAX
Var QtdPessoas = [Qtd de Pessoas Cs]  
Var TotalPessoas = CALCULATE([Qtd de Pessoas Cs],ALL('tb_consideracao'[ds_classificacao_expl], 'tb_consideracao'[cd_classificacao_expl]))  
Return DIVIDE(QtdPessoas, TotalPessoas,0)
```
**Descrição:**  
```
Calcula percentual de cada classificação (Topbox, Eu poderia considerar, Eu não consiseraria) das respostas em relação ao total de respondentes.
```

---

### Nome Campo: * Consideração  
**Aba:** MPT  
**Fórmula DAX:**
```DAX
VAR total = 
    CALCULATE ( 
        [Qtd de pessoas Cs 0], 
        ALLSELECTED ( 'tb_consideracao'[nw_ds_classificacao_expl] ), 
        ALLSELECTED ( 'tb_consideracao'[nw_cd_classificacao_expl] )     
    ) 
RETURN 
    SWITCH ( 
        TRUE (), 
        SELECTEDVALUE ( 'Parâmetro Consideração'[Parâmetro Consideração Pedido] ) = 2, 
            CALCULATE ( 
                DIVIDE ( 
                    [Qtd de Pessoas Cs 0], 
                    total, 
                    0 
                ), 
                tb_filtro_semestral_nao_proprietario[semestre] <> BLANK () 
            ), 
        SELECTEDVALUE ( 'Parâmetro Consideração'[Parâmetro Consideração Pedido]  ) = 3, 
            DIVIDE ( 
               [Qtd de Pessoas Cs 0], 
                total, 
                0 
            ) 
    )
```
**Descrição:**  
```
Calcula percentual de classificações do indicador em relação ao total. Remove períodos incompletos e é usado em matrizes multiperíodo.
```

---

### Nome Campo: ** Consideração  
**Aba:** MPT  
**Fórmula DAX:**
```DAX
SWITCH ( 
    TRUE (), 
    SELECTEDVALUE ( 'Parâmetro Consideração'[Parâmetro Consideração Pedido] ) = 2, 
        CALCULATE ( 
            [Qtd de Pessoas Cs 0], 
            tb_filtro_semestral_nao_proprietario[semestre] <> BLANK () 
        ), 
    SELECTEDVALUE ( 'Parâmetro Consideração'[Parâmetro Consideração Pedido] ) = 3, 
        [Qtd de Pessoas Cs 0] 
)
```
**Descrição:**  
```
Calcula quantidade de pessoas que responderam ao questionário no período selecionado (Base). Se os filtros aplicados não gerarem dados para o cálculo, ele retorna 0. Exclui períodos em branco, para o caso de semestres onde os dados ainda estão incompletos
```

---

### Nome Campo: *** Consideração  
**Aba:** MPT  
**Fórmula DAX:**
```DAX
VAR total = 
    CALCULATE ( 
       [Qtd de Pessoas Cs 0], 
        ALLSELECTED ( 'tb_consideracao'[ds_resposta] ), 
        ALLSELECTED ( 'tb_consideracao'[cd_resposta] ) 
    ) 
RETURN 
    SWITCH ( 
        TRUE (), 
        SELECTEDVALUE ( 'Parâmetro Consideração'[Parâmetro Consideração Pedido] ) = 2, 
            CALCULATE ( 
                DIVIDE ( 
                    [Qtd de Pessoas Cs 0], 
                    total, 
                    0 
                ), 
                tb_filtro_semestral_nao_proprietario[semestre] <> BLANK () 
            ), 
        SELECTEDVALUE ( 'Parâmetro Consideração'[Parâmetro Consideração Pedido]  ) = 3, 
            DIVIDE ( 
                [Qtd de Pessoas Cs 0], 
                total, 
                0 
            ) 
    )
```
**Descrição:**  
```
Calcula percentual de pessoas que responderam cada opção de resposta (ds_resposta) do questionário no período selecionado. Se os filtros aplicados não gerarem dados para o cálculo, ele retorna 0. Exclui períodos em branco, para o caso de semestres onde os dados ainda estão incompletos.Criado para uso em matriz multiperiodo.
```

---

### Nome Campo: CorBaseConsideração  
**Aba:** All  
**Fórmula DAX:**
```DAX
Var vlCorBaseCs =  
    SWITCH (TRUE(), 
        tb_consideracao[Qtd de Pessoas Cs] >= 70, "#1C1C1C", 
        "#DB082C")  
Return vlCorBaseCs
```
**Descrição:**  
```
Se o valor da Base de pessoas que responderam ao questionário for menor do que  70 então a cor do número de base deve ser vermelha para destacar
```


## Dashboards Diferente

Nomes alternativos: "Única".

Tabela no BigQuery: "tb_diferente"

Diagrama de relacionamento da tb_diferente no Power BI

![Imagem](documentacao/imagem30.png)

Aba: Diferente – Multi Brand Gráficos

![Imagem](documentacao/imagem31.png)

Aba: Diferente – Multi Brand Tabela

![Imagem](documentacao/imagem32.png)

Aba: Diferente – Multi Period Gráficos

![Imagem](documentacao/imagem33.png)

Aba: Diferente – Multi Period Tabela

![Imagem](documentacao/imagem34.png)

---

### Fórmulas Dax Diferente

**Legenda Abas:**  
**MBG** – Multi Brand Gráficos  
**MBT** – Multi Brand Tabela  
**MPG** – Multi Period Gráficos  
**MPT** – Multi Period Tabela  
**EX** – Exportação


### Nome Campo: Qtd de PessoasD
**Aba:** MBG  
**Fórmula DAX:**
```DAX
DISTINCTCOUNT(tb_diferente[cd_pessoa])
```
**Descrição:** 
```
Calcula quantidade de pessoas que responderam ao questionário (Respondentes). Utilizado frequentemente para medir a Base de pessoas da pesquisa em um período.
``` 
---

### Nome Campo: % Top2box D  
**Aba:** MBG  
**Fórmula DAX:**
```DAX
Var QtdPessoas = [Qtd de PessoasD]    
Var TotalPessoas = CALCULATE(COUNT(tb_diferente[cd_pessoa]), tb_diferente[cd_resposta] in {7,6}) 
Return 
DIVIDE((TotalPessoas),QtdPessoas,0)
```
**Descrição:**
```
Calcula percentual de respostas mais positivas, “6” ou “7 Muito diferente”, do questionário em relação ao total de respondentes. Campo usado geralmente para ordenar gráficos.
``` 
---

### Nome Campo: % Muito diferente  
**Aba:** MBG  
**Fórmula DAX:**
```DAX
Var QtdPessoas = [Qtd de PessoasD]    
Var TotalPessoas = CALCULATE(COUNT(tb_diferente[cd_pessoa]), tb_diferente[cd_resposta] = 7) 
Return 
DIVIDE((TotalPessoas),QtdPessoas,0)
```
**Descrição:** 
```
Calcula percentual da resposta “7 Muito diferente” do questionário em relação ao total de respondentes. Campo usado geralmente para ordenar gráficos.
``` 
---

### Nome Campo: % Participação Diferente  
**Aba:** MBT  
**Fórmula DAX:**
```DAX
Var QtdPessoas = [Qtd de PessoasD 0] 
Var TotalPessoas = CALCULATE([Qtd de PessoasD],ALL('tb_diferente'[ds_resposta], 'tb_diferente'[cd_resposta])) 
Return 
DIVIDE(QtdPessoas, TotalPessoas,0)
```
**Descrição:**
```
Calcula percentual de cada resposta do questionário em relação ao total de respondentes. Se os filtros aplicados não gerarem dados para o cálculo, ele retorna 0.
``` 
---

### Nome Campo: % ParticipaçãoD Top2NW  
**Aba:** MBT  
**Fórmula DAX:**
```DAX
VAR qnt_pessoas = [Qtd de PessoasD 0] 
VAR total = 
    CALCULATE ( 
        [Qtd de PessoasD 0], 
        ALL( 'tb_diferente'[ds_classificacao_expl] ), 
        ALL( 'tb_diferente'[cd_classificacao_expl] ), 
        ALL( tb_diferente[nw_cd_classificacao_expl]), 
        ALL( tb_diferente[nw_ds_classificacao_expl]) 
    ) 
RETURN 
   DIVIDE( 
        [Qtd de PessoasD 0], 
        total, 
        0)
```
**Descrição:**
``` 
Calcula percentual de cada classificação do indicador (Top2box, Top2bottom, Neutros) em relação ao total de respondentes (Base). Se os filtros aplicados não gerarem dados para o cálculo, ele retorna 0. Baseado no campo nw_ds_classificacao_expl para trazer as informações em ordem diferente do campo original de classificacao(ds_classificacao_expl ). Usamos o nw_cd_classificacao_expl para essa nova ordenação.
``` 
---

### Nome Campo: Qtd de PessoasD 0  
**Aba:** MBT  
**Fórmula DAX:**
```DAX
IF(ISBLANK(DISTINCTCOUNT(tb_diferente[cd_pessoa])), 0, DISTINCTCOUNT(tb_diferente[cd_pessoa]))
```
**Descrição:**
```
Calcula quantidade de pessoas que responderam ao questionário (Respondentes). Utilizado frequentemente para medir a Base de pessoas da pesquisa em um período. Se os filtros aplicados não gerarem dados para o cálculo, ele retorna 0.
``` 
---

### Nome Campo: Qtd de PessoasD Formatada  
**Aba:** MBT MPT  
**Fórmula DAX:**
```DAX
Var QndPessoas = [Qtd de PessoasD] 
Var Formatacao =  
            SWITCH(TRUE(), 
                    ([% Participação Diferente] < 0.005), "#999999",   
                    ([*** Diferente]  < 0.005), "#999999", 
                    SELECTEDVALUE(tb_diferente[cd_resposta]) in {1,2}, "#EE4549", 
                    SELECTEDVALUE(tb_diferente[cd_resposta]) in {3,4,5}, "#1B1B1B", 
                    SELECTEDVALUE(tb_diferente[cd_resposta]) in {6,7}, "#3BB537", "#999999") 
Return  
Formatacao
```
**Descrição:**
```
Regra de formatação aplicada para as matrizes contendo os percentuais de cada resposta do indicador. Percentuais das respostas mais positivas em cor verde, neutras em preto e menos positivas em vermelho. Todos os zeros em cinza.
``` 
---

### Nome Campo: Qtd de PessoasD Formatada Top2  
**Aba:** MBT MPT  
**Fórmula DAX:**
```DAX
Var QndPessoas = [Qtd de Pessoas] 
Var Formatacao =  
            SWITCH(TRUE(), 
                    ([% ParticipaçãoD Top2NW] < 0.005), "#999999",   
                    ([* Diferente]  < 0.005), "#999999", 
                    SELECTEDVALUE(tb_diferente[nw_ds_classificacao_expl]) = "TOP2BOTTOM" , "#EE4549", 
                    SELECTEDVALUE(tb_diferente[nw_ds_classificacao_expl]) = "OUTROS", "#1B1B1B", 
                    SELECTEDVALUE(tb_diferente[nw_ds_classificacao_expl]) = "TOP2BOX", "#3BB537", "#999999") 
Return  
Formatacao
```
**Descrição:**
```
Regra de formatação aplicada para as matrizes contendo os percentuais de classificação de resposta do indicador (Top2box, Top2bottom, Neutros). Percentuais das respostas mais positivas em cor verde, neutras em preto e menos positivas em vermelho. Todos os zeros em cinza.
```

---

### Nome Campo: % ParticipaçãoD Top2  
**Aba:** MPG  
**Fórmula DAX:**
```DAX
VAR total = 
    CALCULATE ( 
        [Qtd de PessoasD], 
        ALL( 'tb_diferente'[ds_classificacao_expl] ), 
        ALL( 'tb_diferente'[cd_classificacao_expl] ), 
        ALL( tb_diferente[nw_cd_classificacao_expl]), 
        ALL( tb_diferente[nw_ds_classificacao_expl]) 
    ) 
RETURN 
   DIVIDE( 
        [Qtd de PessoasD], 
        total, 
        0)
```
**Descrição:**
```
Calcula percentual de cada classificação (Top2box, Top2bottom, Neutros) das repostas do indicador em relação ao total de respondentes. Baseado no campo ds_classificacao_expl.
``` 
---

### Nome Campo: * Diferente
**Aba:** MPT  
**Fórmula DAX:**
```DAX
SWITCH ( 
    TRUE (), 
    SELECTEDVALUE ( 'Parâmetro Diferente'[Parâmetro Pedido] ) = 2, 
        CALCULATE ( 
            [% ParticipaçãoD Top2NW], 
            tb_filtro_semestral_nao_proprietario[semestre] <> BLANK () 
        ), 
    SELECTEDVALUE ( 'Parâmetro Diferente'[Parâmetro Pedido] ) = 3, [% ParticipaçãoD Top2NW] 
)
```
**Descrição:**  
```
Calcula percentual de cada classificação do questionário (Top2box, Top2bottom, Neutros) em relação ao total de respondentes (Base). Se os filtros aplicados não gerarem dados para o cálculo, ele retorna 0. Exclui períodos em branco, para o caso de semestres onde os dados ainda estão incompletos. Criado para uso em matriz multiperiodo.
```

---

### Nome Campo: ** Diferente
**Aba:** MPT  
**Fórmula DAX:**
```DAX
SWITCH ( 
    TRUE (), 
    SELECTEDVALUE ( 'Parâmetro Diferente'[Parâmetro Pedido] ) = 2, 
        CALCULATE ( 
            [Qtd de PessoasD 0], 
            tb_filtro_semestral_nao_proprietario[semestre] <> BLANK () 
        ), 
    SELECTEDVALUE ( 'Parâmetro Diferente'[Parâmetro Pedido] ) = 3, 
            [Qtd de PessoasD 0] 
)
```
**Descrição:**  
```
Calcula quantidade de pessoas que responderam ao questionário no período selecionado (Base). Se os filtros aplicados não gerarem dados para o cálculo, ele retorna 0. Exclui períodos em branco, para o caso de semestres onde os dados ainda estão incompletos.
```

---

### Nome Campo: *** Diferente
**Aba:** MPT  
**Fórmula DAX:**
```DAX
VAR total = 
    CALCULATE ( 
       [Qtd de PessoasD 0], 
        ALLSELECTED ( 'tb_diferente'[ds_resposta] ), 
        ALLSELECTED ( 'tb_diferente'[cd_resposta] ) 
    ) 
RETURN 
    SWITCH ( 
        TRUE (), 
        SELECTEDVALUE ( 'Parâmetro Diferente'[Parâmetro Pedido] ) = 2, 
            CALCULATE ( 
                DIVIDE ( 
                    [Qtd de PessoasD 0], 
                    total, 
                    0 
                ), 
                tb_filtro_semestral_nao_proprietario[semestre] <> BLANK () 
            ), 
        SELECTEDVALUE ( 'Parâmetro Diferente'[Parâmetro Pedido] ) = 3, 
            DIVIDE ( 
                [Qtd de PessoasD 0], 
                total, 
                0 
            ) 
    )
```
**Descrição:**  
```
Calcula percentual de pessoas que responderam cada opção de resposta (ds_resposta) do questionário no período selecionado. Se os filtros aplicados não gerarem dados para o cálculo, ele retorna 0. Exclui períodos em branco, para o caso de semestres onde os dados ainda estão incompletos. Criado para uso em matriz multiperiodo.
```

---

### Nome Campo: CorBaseDiferente
**Aba:** All  
**Fórmula DAX:**
```DAX
Var vlCorBaseD =  
    SWITCH (TRUE(), 
        tb_diferente[Qtd de PessoasD] >= 70, "#1C1C1C", 
        "#DB082C"
    )  
Return  
    vlCorBaseD
```
**Descrição:**  
```
Se o valor da Base de pessoas que responderam ao questionário for menor do que 70 então a cor do número de base deve ser vermelha para destacar.
```
---


## Dashboards Dita Tendências

Nomes alternativos: "Dita/Lança tendências", "Dinâmica", "Dinamismo".

Tabela no BigQuery: "tb_dita_tendencias"

Diagrama de relacionamento da tb_dita_tendencias no Power BI

![Imagem](documentacao/imagem35.png)

Aba: Dita Tendências – Multi Brand Gráficos

![Imagem](documentacao/imagem36.png)

Aba: Dita Tendências – Multi Brand Tabela

![Imagem](documentacao/imagem37.png)

Aba: Dita Tendências – Multi Period Gráficos

![Imagem](documentacao/imagem38.png)

Aba: Dita Tendências – Multi Period Tabela

![Imagem](documentacao/imagem39.png)

### Fórmulas Dax Dita Tendências

**Legenda Abas:**  
**MBG** – Multi Brand Gráficos  
**MBT** – Multi Brand Tabela  
**MPG** – Multi Period Gráficos  
**MPT** – Multi Period Tabela  
**EX** – Exportação

---

### Nome Campo: Qtd de PessoasT  
**Aba:** MBG  
**Fórmula DAX:**
```DAX
DISTINCTCOUNT(tb_dita_tendencias[cd_pessoa])
```
**Descrição:**  
```
Calcula quantidade de pessoas que responderam ao questionário (Respondentes). Utilizado frequentemente para medir a Base de pessoas da pesquisa em um período.
```

---

### Nome Campo: % Top2box T  
**Aba:** MBG  
**Fórmula DAX:**
```DAX
Var QtdPessoas = [Qtd de PessoasT]    
Var TotalPessoas = CALCULATE(COUNT(tb_dita_tendencias[cd_pessoa]), tb_dita_tendencias[cd_resposta] in {7,6})  
Return DIVIDE((TotalPessoas),QtdPessoas,0)
```
**Descrição:**  
```
Calcula percentual de respostas mais positivas, “6” ou “7 Dita/Lança Tendências”, do questionário em relação ao total de respondentes. Campo usado geralmente para ordenar gráficos.
```

---

### Nome Campo: % Dita/lança tendências  
**Aba:** MBG  
**Fórmula DAX:**
```DAX
Var QtdPessoas = [Qtd de PessoasT]    
Var TotalPessoas = CALCULATE(COUNT(tb_dita_tendencias[cd_pessoa]), tb_dita_tendencias[cd_resposta] = 7)  
Return DIVIDE((TotalPessoas),QtdPessoas,0)
```
**Descrição:**  
```
Calcula percentual da resposta “7 Dita/Lança Tendências” do indicador em relação ao total de respondentes. Campo usado geralmente para ordenar gráficos.
```

---

### Nome Campo: % Participação Dita 0  
**Aba:** MBT  
**Fórmula DAX:**
```DAX
Var QtdPessoas = [Qtd de PessoasT 0]  
Var TotalPessoas = CALCULATE([Qtd de PessoasT],ALL('tb_dita_tendencias'[ds_resposta], 'tb_dita_tendencias'[cd_resposta]))  
Return DIVIDE(QtdPessoas, TotalPessoas,0)
```
**Descrição:**  
```
Calcula percentual de cada resposta do indicador em relação ao total de respondentes. Se os filtros aplicados não gerarem dados para o cálculo, ele retorna 0.
```

---

### Nome Campo: % ParticipaçãoT Top2NW  
**Aba:** MBT  
**Fórmula DAX:**
```DAX
Var QtdPessoas = [Qtd de PessoasT 0]  
Var TotalPessoas = CALCULATE([Qtd de PessoasT],ALL('tb_dita_tendencias'[nw_ds_classificacao_expl], 'tb_dita_tendencias'[nw_cd_classificacao_expl]))  
Return DIVIDE(QtdPessoas, TotalPessoas,0)
```
**Descrição:**  
```
Calcula percentual de cada classificação do indicador (Top2box, Top2bottom, Neutros) em relação ao total de respondentes (Base). Se os filtros aplicados não gerarem dados para o cálculo, ele retorna 0. Baseado no campo nw_ds_classificacao_expl para trazer as informações em ordem diferente do campo original de classificacao(ds_classificacao_expl ). Usamos o nw_cd_classificacao_expl para essa nova ordenação.
```
---
### Nome Campo: Qtd de PessoasT 0
**Aba:** MBT  
**Fórmula DAX:**
```DAX
IF(ISBLANK(DISTINCTCOUNT(tb_dita_tendencias[cd_pessoa])), 0, DISTINCTCOUNT(tb_dita_tendencias[cd_pessoa]))
```
**Descrição:**
```
Calcula quantidade de pessoas que responderam ao questionário (Respondentes). Utilizado frequentemente para medir a Base de pessoas da pesquisa em um período. Se os filtros aplicados não gerarem dados para o cálculo, ele retorna 0.
````

---

### Nome Campo: Qtd de PessoasT Formatada
**Aba:** MBT MPT  
**Fórmula DAX:**
```DAX
Var Formatacao =  
    SWITCH(TRUE(), 
        ([% Participação Dita 0] < 0.005), "#999999",   
        ([*** Dita]  < 0.005), "#999999", 
        SELECTEDVALUE(tb_dita_tendencias[cd_resposta]) in {1,2}, "#EE4549", 
        SELECTEDVALUE(tb_dita_tendencias[cd_resposta]) in {3,4,5}, "#1B1B1B", 
        SELECTEDVALUE(tb_dita_tendencias[cd_resposta]) in {6,7}, "#3BB537", "#999999") 
Return  
    Formatacao
```
**Descrição:** 
```
Regra de formatação aplicada para as matrizes contendo os percentuais de cada resposta do indicador. Percentuais das respostas mais positivas em cor verde, neutras em preto e menos positivas em vermelho. Todos os zeros em cinza.
``` 
---

### Nome Campo: Qtd de PessoasT Formatada Top2
**Aba:** MBT MPT  
**Fórmula DAX:**
```DAX
Var QndPessoas = [Qtd de PessoasT] 
Var Formatacao =  
    SWITCH(TRUE(), 
        ([% ParticipaçãoT Top2NW] < 0.005), "#999999",   
        ([* Dita]  < 0.005), "#999999", 
        SELECTEDVALUE(tb_dita_tendencias[nw_ds_classificacao_expl]) = "TOP2BOTTOM" , "#EE4549", 
        SELECTEDVALUE(tb_dita_tendencias[nw_ds_classificacao_expl]) = "Neutros", "#1B1B1B", 
        SELECTEDVALUE(tb_dita_tendencias[nw_ds_classificacao_expl]) = "TOP2BOX", "#3BB537", "#999999") 
Return  
    Formatacao
```
**Descrição:** 
```
Regra de formatação aplicada para as matrizes contendo os percentuais de classificação de resposta do indicador (Top2box, Top2bottom, Neutros). Percentuais das respostas mais positivas em cor verde, neutras em preto e menos positivas em vermelho. Todos os zeros em cinza.
````

---

### Nome Campo: % ParticipaçãoT Top2
**Aba:** MPG  
**Fórmula DAX:**
```DAX
Var QtdPessoas = [Qtd de PessoasT] 
Var TotalPessoas = CALCULATE([Qtd de PessoasT],ALL('tb_dita_tendencias'[ds_classificacao_expl], 'tb_dita_tendencias'[cd_classificacao_expl])) 
Return 
    DIVIDE(QtdPessoas, TotalPessoas,0)
```
**Descrição:**
```
Calcula percentual de cada classificação (Top2box, Top2bottom, Neutros) das repostas do indicador em relação ao total de respondentes. Baseado no campo ds_classificacao_expl.
``` 
---

### Nome Campo: * Dita
**Aba:** MPT  
**Fórmula DAX:**
```DAX
VAR total = 
    CALCULATE ( 
        [Qtd de PessoasT 0], 
        ALLSELECTED ( 'tb_dita_tendencias'[ds_classificacao_expl] ), 
        ALLSELECTED ( 'tb_dita_tendencias'[cd_classificacao_expl] ) 
    )
RETURN 
    SWITCH ( 
        TRUE (), 
        SELECTEDVALUE ( 'Parâmetro Dita Tendências'[Parâmetro Dita Tendencias Pedido] ) = 2, 
            CALCULATE ( 
                DIVIDE ( 
                    [Qtd de PessoasT 0], 
                    total, 
                    0 
                ), 
                tb_filtro_semestral_nao_proprietario[semestre] <> BLANK () 
            ), 
        SELECTEDVALUE ( 'Parâmetro Dita Tendências'[Parâmetro Dita Tendencias Pedido]  ) = 3, 
            DIVIDE ( 
                [Qtd de PessoasT 0], 
                total, 
                0 
            ) 
    )
```
**Descrição:**
```
Calcula percentual de cada classificação do questionário (Top2box, Top2bottom, Neutros) em relação ao total de respondentes (Base). Se os filtros aplicados não gerarem dados para o cálculo, ele retorna 0. Exclui períodos em branco, para o caso de semestres onde os dados ainda estão incompletos. Criado para uso em matriz multiperiodo.
``` 
---

### Nome Campo: ** Dita
**Aba:** MPT  
**Fórmula DAX:**
```DAX
SWITCH ( 
    TRUE (), 
    SELECTEDVALUE ( 'Parâmetro Dita Tendências'[Parâmetro Dita Tendencias Pedido] ) = 2, 
        CALCULATE ( 
            [Qtd de PessoasT 0], 
            tb_filtro_semestral_nao_proprietario[semestre] <> BLANK () 
        ), 
    SELECTEDVALUE ( 'Parâmetro Dita Tendências'[Parâmetro Dita Tendencias Pedido]  ) = 3, 
            [Qtd de PessoasT 0] 
)
```
**Descrição:**
```
Calcula quantidade de pessoas que responderam ao questionário no período selecionado (Base). Se os filtros aplicados não gerarem dados para o cálculo, ele retorna 0. Exclui períodos em branco, para o caso de semestres onde os dados ainda estão incompletos.
``` 

---

### Nome Campo: *** Dita
**Aba:** MPT  
**Fórmula DAX:**
```DAX
VAR total = 
    CALCULATE ( 
        [Qtd de PessoasT 0], 
        ALLSELECTED ( 'tb_dita_tendencias'[ds_resposta] ), 
        ALLSELECTED ( 'tb_dita_tendencias'[cd_resposta] ) 
    )
RETURN 
    SWITCH ( 
        TRUE (), 
        SELECTEDVALUE ( 'Parâmetro Dita Tendências'[Parâmetro Dita Tendencias Pedido] ) = 2, 
            CALCULATE ( 
                DIVIDE ( 
                    [Qtd de PessoasT 0], 
                    total, 
                    0 
                ), 
                tb_filtro_semestral_nao_proprietario[semestre] <> BLANK () 
            ), 
        SELECTEDVALUE ( 'Parâmetro Dita Tendências'[Parâmetro Dita Tendencias Pedido] ) = 3, 
            DIVIDE ( 
                [Qtd de PessoasT 0], 
                total, 
                0 
            ) 
    )
```
**Descrição:**
```
Calcula percentual de pessoas que responderam cada opção de resposta (ds_resposta) do questionário no período selecionado. Se os filtros aplicados não gerarem dados para o cálculo, ele retorna 0. Exclui períodos em branco, para o caso de semestres onde os dados ainda estão incompletos. Criado para uso em matriz multiperiodo.
``` 
---

### Nome Campo: CorBaseDitaTendencias
**Aba:** All  
**Fórmula DAX:**
```DAX
Var vlCorBaseT =  
    SWITCH (TRUE(), 
        tb_dita_tendencias[Qtd de PessoasT] >= 70, "#1C1C1C", 
        "#DB082C")  
Return  
    vlCorBaseT
```
**Descrição:** 
```
Se o valor da Base de pessoas que responderam ao questionário for menor do que 70 então a cor do número de base deve ser vermelha para destacar.
``` 

---

## Dashboards NPS

Nomes alternativos: "Recomendação".

Tabela no BigQuery: "tb_nps"

Diagrama de relacionamento da tb_nps no Power BI

![Imagem](documentacao/imagem40.png)

Aba: NPS – Multi Brand Gráficos

![Imagem](documentacao/imagem41.png)

Aba: NPS – Multi Brand Tabela

![Imagem](documentacao/imagem42.png)

Aba: NPS – Multi Period Gráficos

![Imagem](documentacao/imagem43.png)

Aba: NPS – Multi Period Tabela

![Imagem](documentacao/imagem44.png)

### Fórmulas Dax NPS

**Legenda Abas:**  
**MBG** – Multi Brand Gráficos  
**MBT** – Multi Brand Tabela  
**MPG** – Multi Period Gráficos  
**MPT** – Multi Period Tabela  
**EX** – Exportação


### Nome Campo: Qtd de PessoasNPS
**Aba:** MBG  
**Fórmula DAX:**
```DAX
DISTINCTCOUNT(tb_nps[cd_pessoa])
```
**Descrição:**
```
Calcula quantidade de pessoas que responderam ao questionário (Respondentes). Utilizado frequentemente para medir a Base de pessoas da pesquisa em um período.
``` 
---

### Nome Campo: Índice NPS Dec  
**Aba:** MBG  
**Fórmula DAX:**
```DAX
Var Qtd_Promo = CALCULATE([Qtd de PessoasNPS],FILTER('tb_nps','tb_nps'[ds_classificacao_expl]="Promotores"))
Var Qtd_Detra = CALCULATE([Qtd de PessoasNPS],FILTER('tb_nps','tb_nps'[ds_classificacao_expl]="Detratores"))
Var Total_Pessoas = CALCULATE([Qtd de PessoasNPS],ALL('tb_nps'[ds_resposta], 'tb_nps'[cd_resposta]))
Var Perc_Promo = DIVIDE(Qtd_Promo, Total_Pessoas,0)
Var Perc_Detra = DIVIDE(Qtd_Detra, Total_Pessoas,0)
Return (Perc_Promo - Perc_Detra) *100
```
**Descrição:**
```
Cálculo do valor do índice NPS (% de promotores - % de detratores) com 2 casas decimais.
``` 
---

### Nome Campo: CorZonasNPS P2  
**Aba:** MBG  
**Fórmula DAX:**
```DAX
SWITCH(TRUE(),
    (tb_nps[Índice NPS] < 70 && tb_nps[Índice NPS] > 49), "#008DA1",
    (tb_nps[Índice NPS] > -1 && tb_nps[Índice NPS] < 50), "#DB6F02",
    (tb_nps[Índice NPS] >= 70), "#0E2B63",
    (tb_nps[Índice NPS] < 0), "#7A0237"
)
```
**Descrição:**
```
Formatação que aplica cor aos valores do índice NPS de acordo com as zonas de classificação: excelência, qualidade, melhoria e crítica.
``` 
---

### Nome Campo: % Participação NPS  
**Aba:** (não especificada)  
**Fórmula DAX:**
```DAX
Var QtdPessoas = [Qtd de PessoasNPS 0]
Var TotalPessoas = CALCULATE([Qtd de PessoasNPS 0],ALL('tb_nps'[ds_resposta], 'tb_nps'[cd_resposta]))
RETURN DIVIDE(QtdPessoas, TotalPessoas, 0)
```
**Descrição:**
```
Calcula percentual de cada resposta do indicador em relação ao total de respondentes. Retorna 0 caso não haja dados.
``` 

---

### Nome Campo: Qtd de PessoasNPS 0  
**Aba:** MBT  
**Fórmula DAX:**
```DAX
DISTINCTCOUNT(tb_nps[cd_pessoa])
```
**Descrição:** 
```
Calcula quantidade de pessoas que responderam ao questionário. Retorna 0 se não houver dados.
```

---

### Nome Campo: Índice NPS  
**Aba:** MBT  
**Fórmula DAX:**
```DAX
Var Qtd_Promo = CALCULATE([Qtd de PessoasNPS 0],FILTER('tb_nps','tb_nps'[ds_classificacao_expl]="Promotores"))
Var Qtd_Detra = CALCULATE([Qtd de PessoasNPS 0],FILTER('tb_nps','tb_nps'[ds_classificacao_expl]="Detratores"))
Var Total_Pessoas = CALCULATE([Qtd de PessoasNPS 0],ALL('tb_nps'[ds_resposta], 'tb_nps'[cd_resposta]))
Var Perc_Promo = DIVIDE(Qtd_Promo, Total_Pessoas,0)
Var Perc_Detra = DIVIDE(Qtd_Detra, Total_Pessoas,0)
Var Result = (Perc_Promo - Perc_Detra) *100
Return IF ( [Qtd de PessoasNPS] = BLANK(), 0, IF( (Result < 1 && Result > -1) , 1, Result ) )
```
**Descrição:** 
``` 
Cálculo do valor do índice NPS. Retorna 1 se o resultado for muito próximo de zero.
``` 
---

### Nome Campo: % Participação NPS por Marca  
**Aba:** (não especificada)  
**Fórmula DAX:**
```DAX
Var QtdPessoas = [Qtd de PessoasNPS]
Var TotalPessoas = CALCULATE([Qtd de PessoasNPS],ALL('tb_nps'[ds_classificacao_expl]))
Return DIVIDE(QtdPessoas, TotalPessoas,0)
```
**Descrição:**
```
Calcula o percentual de respondentes por perfil (Promotores, Detratores, Neutros) por marca.
``` 
---

### Nome Campo: ** NPS  
**Aba:** MPT  
**Fórmula DAX:**
```DAX
SWITCH (
    TRUE (),
    SELECTEDVALUE ( 'Parâmetro NPS'[Parâmetro NPS Pedido] ) = 2,
        IF(CALCULATE (
            [Índice NPS],
            tb_filtro_semestral_nao_proprietario[semestre] <> BLANK ()
        ) = 1, BLANK(),[Índice NPS]),
    SELECTEDVALUE ( 'Parâmetro NPS'[Parâmetro NPS Pedido] ) = 3,
            [Índice NPS]
)
```
**Descrição:**
```
Cálculo do índice NPS para matriz multiperíodo, excluindo períodos incompletos.
``` 
---

### Nome Campo: ** Base NPS  
**Aba:** MPT  
**Fórmula DAX:**
```DAX
SWITCH (
    TRUE (),
    SELECTEDVALUE ( 'Parâmetro NPS'[Parâmetro NPS Pedido] ) = 2,
        CALCULATE (
            [Qtd de PessoasNPS 0],
            tb_filtro_semestral_nao_proprietario[semestre] <> BLANK ()
        ),
    SELECTEDVALUE ( 'Parâmetro NPS'[Parâmetro NPS Pedido] ) = 3,
           [Qtd de PessoasNPS 0]
)
```
**Descrição:**
```
Calcula a base de respondentes por período, excluindo semestres com dados incompletos.
``` 
---

### Nome Campo: *** NPS  
**Aba:** MPT  
**Fórmula DAX:**
```DAX
VAR total =
    CALCULATE (
        [Qtd de PessoasNPS 0],
        ALLSELECTED ( 'tb_nps'[ds_resposta] ),
        ALLSELECTED ( 'tb_nps'[cd_resposta] )
    )
RETURN
    SWITCH (
        TRUE (),
        SELECTEDVALUE ( 'Parâmetro NPS'[Parâmetro NPS Pedido] ) = 2,
            CALCULATE (
                DIVIDE (
                    [Qtd de PessoasNPS 0],
                    total,
                    0
                ),
                tb_filtro_semestral_nao_proprietario[semestre] <> BLANK ()
            ),
        SELECTEDVALUE ( 'Parâmetro NPS'[Parâmetro NPS Pedido]  ) = 3,
            DIVIDE (
                [Qtd de PessoasNPS 0],
                total,
                0
            )
    )
```
**Descrição:** 
```
Calcula percentual de respondentes por opção de resposta do indicador, para matriz multiperíodo.
``` 
---

## Dashboards Power e dimensões

Tabela no BigQuery: "tb_power_dimensoes"

Diagrama de relacionamento da "tb_power_dimensoes" no Power BI

![Imagem](documentacao/imagem45.png)

Aba: Power – Multi Brand Gráficos

![Imagem](documentacao/imagem46.png)

Aba: Power – Multi Brand Tabela

![Imagem](documentacao/imagem47.png)

Aba: Power – Multi Period Gráficos

![Imagem](documentacao/imagem48.png)

Aba: Power – Multi Period Tabela

![Imagem](documentacao/imagem49.png)

### Fórmulas Dax Power e dimensões

**Legenda Abas:**  
**MBG** – Multi Brand Gráficos  
**MBT** – Multi Brand Tabela  
**MPG** – Multi Period Gráficos  
**MPT** – Multi Period Tabela  
**EX** – Exportação


### Nome Campo: Power %  
**Aba:** MBG  
**Fórmula DAX:**
```DAX
CALCULATE(SUM(tb_power_dimensoes[vl_metrica]), tb_power_dimensoes[ds_metrica] = "Power")
```
**Descrição:**  
```
Calcula o power da Marca em relação ao período selecionado.
```
---

### Nome Campo: RankingDesempatePower  
**Aba:** MBG  
**Fórmula DAX:**
```DAX
[Power] + [vl_diferenciação] + [vl_significancia]
```
**Descrição:**  
```
Se o valor de Power de 2 marcas for igual, soma o peso da diferenciação e da significância para definir a ordem correta do ranking.
```
---

### Nome Campo: Power  
**Aba:** MBG/ MBT/ MPT  
**Fórmula DAX:**
```DAX
CALCULATE(SUM(tb_power_dimensoes[vl_metrica]), tb_power_dimensoes[ds_metrica] = "Power")*100
```
**Descrição:**  
```
Calcula o percentual de Power da Marca em relação ao período selecionado.
```
---

### Nome Campo: vl_diferenciação  
**Aba:** MBG  
**Fórmula DAX:**
```DAX
CALCULATE(SUM(tb_power_dimensoes[vl_metrica]), tb_power_dimensoes[id_metrica] = 2 ) * 0.001
```
**Descrição:**  
```
Calcula o valor da dimensão diferenciação em relação ao peso de desempate para o indicador.
```
---

### Nome Campo: vl_significancia  
**Aba:** MBG  
**Fórmula DAX:**
```DAX
vl_significancia = CALCULATE(SUM(tb_power_dimensoes[vl_metrica]), tb_power_dimensoes[id_metrica] in { 1 }) * 0.01
```
**Descrição:**  
```
Calcula o valor da dimensão significância em relação ao peso de desempate para o indicador.
```
---

### Nome Campo: Top Power Cards  
**Aba:** MBG  
**Fórmula DAX:**
```DAX
SWITCH(TRUE(), 
SELECTEDVALUE('tb_top_power'[Filtro]) = "Top 3", [Top 3 Power],  
SELECTEDVALUE('tb_top_power'[Filtro]) = "Top 5", [Top 5 Power],  
SELECTEDVALUE('tb_top_power'[Filtro]) = "Top 10", [Top 10 Power],  
tb_power_dimensoes[Power])
```
**Descrição:**  
```
A partir da entrada do filtro de TOP (Marcas melhores colocadas) em tela, contendo as opções, Top 3, Top 5, Top 10 ou todas, ele chama o cálculo para o ranking de marcas com maior Power nessas posições. Voltado ao funcionamento do gráfico de Dimensões em barras que parece com cards de Power em cinza.
```
---

### Nome Campo: Top 3 Power
**Aba:** MBG  
**Fórmula DAX:**
```DAX
Var Ranking =  RANKX( 
    ALL( tb_power_dimensoes[nm_marca]), 
    CALCULATE( [RankingDesempatePower], ALL( tb_power_dimensoes[ds_metrica] ), ALL(tb_power_dimensoes[id_metrica] ) ), 
    CALCULATE( [RankingDesempatePower], ALL( tb_power_dimensoes[ds_metrica] ), ALL(tb_power_dimensoes[id_metrica] ) ), 
    , 
    DENSE 
) 
Var Metrica = tb_power_dimensoes[Power] 
RETURN 
IF(Ranking < 4, Metrica, BLANK())
```

**Descrição:** 
```
Calcula o ranking das 3 marcas com maior power no período selecionado.
``` 
---

### Nome Campo: Top 5 Power
**Aba:** MBG  
**Fórmula DAX:**
```DAX
Var Ranking =  RANKX( 
    ALL( tb_power_dimensoes[nm_marca]), 
    CALCULATE( [RankingDesempatePower], ALL( tb_power_dimensoes[ds_metrica] ), ALL(tb_power_dimensoes[id_metrica] ) ), 
    CALCULATE( [RankingDesempatePower], ALL( tb_power_dimensoes[ds_metrica] ), ALL(tb_power_dimensoes[id_metrica] ) ), 
    , 
    DENSE 
) 
Var Metrica = tb_power_dimensoes[Power] 
RETURN 
IF(Ranking < 6, Metrica, BLANK())
```

**Descrição:** 
```
Calcula o ranking das 5 marcas com maior power no período selecionado.
``` 
---

### Nome Campo: Top 10 Power
**Aba:** MBG  
**Fórmula DAX:**
```DAX
Var Ranking =  RANKX( 
    ALL( tb_power_dimensoes[nm_marca]), 
    CALCULATE( [RankingDesempatePower], ALL( tb_power_dimensoes[ds_metrica] ), ALL(tb_power_dimensoes[id_metrica] ) ), 
    CALCULATE( [RankingDesempatePower], ALL( tb_power_dimensoes[ds_metrica] ), ALL(tb_power_dimensoes[id_metrica] ) ), 
    , 
    DENSE 
) 
Var Metrica = tb_power_dimensoes[Power] 
RETURN 
IF(Ranking < 11, Metrica, BLANK())
```

**Descrição:**  
```
Calcula o ranking das 10 marcas com maior power no período selecionado.
``` 
---

### Nome Campo: Top Power Gráfico
**Aba:** MBG  
**Fórmula DAX:**
```DAX
SWITCH ( 
    TRUE (), 
    SELECTEDVALUE ( 'tb_top_power'[Filtro] ) = "Top 3", [Top 3 vl_metrica], 
    SELECTEDVALUE ( 'tb_top_power'[Filtro] ) = "Top 5", [Top 5 vl_metrica], 
    SELECTEDVALUE ( 'tb_top_power'[Filtro] ) = "Top 10", [Top 10 vl_metrica], 
    SUM ( tb_power_dimensoes[vl_metrica] ) 
)
```
**Descrição:**  
```
A partir da entrada do filtro de TOP (Marcas melhores colocadas) em tela, contendo as opções, Top 3, Top 5, Top 10 ou todas, ele chama o cálculo para o ranking de marcas com melhor Power nessas posições. Voltado ao funcionamento do gráfico de Dimensões em barras coloridas com valores de Significância, Diferenciação e Saliência.
```
---

### Nome Campo: Top 3 vl_metrica
**Aba:** MBG  
**Fórmula DAX:**
```DAX
Var Ranking = RANKX(
    ALL(tb_power_dimensoes[nm_marca]),
    CALCULATE([RankingDesempatePower], ALL(tb_power_dimensoes[ds_metrica]), ALL(tb_power_dimensoes[id_metrica])),
    CALCULATE([RankingDesempatePower], ALL(tb_power_dimensoes[ds_metrica]), ALL(tb_power_dimensoes[id_metrica])),
    ,
    DENSE
)
Var Metrica = SUM(tb_power_dimensoes[vl_metrica])
RETURN IF(Ranking < 4, Metrica, BLANK())
```
**Descrição:**  
```
Calcula o ranking para as 3 marcas com maior power no período selecionado. Usado para filtrar e ordenar o gráfico de barras colorido de Dimensões do power.
```
---

### Nome Campo: Top 5 vl_metrica
**Aba:** MBG  
**Fórmula DAX:**
```DAX
Var Ranking = RANKX(
    ALL(tb_power_dimensoes[nm_marca]),
    CALCULATE([RankingDesempatePower], ALL(tb_power_dimensoes[ds_metrica]), ALL(tb_power_dimensoes[id_metrica])),
    CALCULATE([RankingDesempatePower], ALL(tb_power_dimensoes[ds_metrica]), ALL(tb_power_dimensoes[id_metrica])),
    ,
    DENSE
)
Var Metrica = SUM(tb_power_dimensoes[vl_metrica])
RETURN IF(Ranking < 6, Metrica, BLANK())
```
**Descrição:**  
```
Calcula o ranking para as 5 marcas com maior power no período selecionado. Usado para filtrar e ordenar o gráfico de barras colorido de Dimensões do power.
```
---

### Nome Campo: Top 10 vl_metrica
**Aba:** MBG  
**Fórmula DAX:**
```DAX
Var Ranking = RANKX(
    ALL(tb_power_dimensoes[nm_marca]),
    CALCULATE([RankingDesempatePower], ALL(tb_power_dimensoes[ds_metrica]), ALL(tb_power_dimensoes[id_metrica])),
    CALCULATE([RankingDesempatePower], ALL(tb_power_dimensoes[ds_metrica]), ALL(tb_power_dimensoes[id_metrica])),
    ,
    DENSE
)
Var Metrica = SUM(tb_power_dimensoes[vl_metrica])
RETURN IF(Ranking < 11, Metrica, BLANK())
```
**Descrição:**  
```
Calcula o ranking para as 10 marcas com maior power no período selecionado. Usado para filtrar e ordenar o gráfico de barras colorido de Dimensões do power.
```
---

### Nome Campo: CorPowerGlobo
**Aba:** MBG  
**Fórmula DAX:**
```DAX
Var vlColorG = IF(tb_power_dimensoes[Marca] = "Globo", "#1a1a1a", "#605E5C")
Return vlColorG
```
**Descrição:**  
```
Usado para destacar a marca Globo nos gráficos de Power.
```
---

### Nome Campo: Significância
**Aba:** MBT MPT  
**Fórmula DAX:**
```DAX
CALCULATE(SUM(tb_power_dimensoes[vl_metrica]), tb_power_dimensoes[ds_metrica] = "Significância")
```
**Descrição:**  
```
Calcula o índice da dimensão Significância em relação ao período e marcas selecionados.
```
---

### Nome Campo: Diferenciação
**Aba:** MBT MPT  
**Fórmula DAX:**
```DAX
CALCULATE(SUM(tb_power_dimensoes[vl_metrica]), tb_power_dimensoes[ds_metrica] = "Diferenciação")
```
**Descrição:**  
```
Calcula o índice da dimensão Diferenciação em relação ao período e marcas selecionados.
```
---

### Nome Campo: Saliência
**Aba:** MBT MPT  
**Fórmula DAX:**
```DAX
CALCULATE(SUM(tb_power_dimensoes[vl_metrica]), tb_power_dimensoes[ds_metrica] = "Saliência")
```
**Descrição:**  
```
Calcula o índice da dimensão Saliência em relação ao período e marcas selecionados.
```
---

### Nome Campo: vl_metrica_formatada
**Aba:** MBT MPT  
**Fórmula DAX:**
```DAX
SWITCH(TRUE(),
    SELECTEDVALUE(tb_power_dimensoes[ds_metrica]) in { "Significância", "Diferenciação", "Saliência", "Base"}, FORMAT(SUM(tb_power_dimensoes[vl_metrica]),"#,##"),
    SELECTEDVALUE(tb_power_dimensoes[ds_metrica]) in { "Power"}, FORMAT(tb_power_dimensoes[Power],"#,##.0")
)
```
**Descrição:**  
```
Aplica máscara de formatação numérica no dado dependendo da métrica exibida (Power ou Significância, Saliência e Diferenciação).
```
---

## Dashboards Contribuição das Dimensões para o Power

Tabela no BigQuery: "tb_contribuicao_power"

Diagrama de relacionamento da tb_contribuicao_power no Power BI: Mesmo do indicador Power.

Obs: Para acessar o indicador na aplicação do Monitor de marcas, é preciso clicar no botão “Entenda a importância das dimensões” que está localizado nas páginas de gráficos do indicador Power (Multimarcas e Multiperíodos).

![Imagem](documentacao/imagem50.png)

Aba: Power Importância – Multi Period Gráficos

![Imagem](documentacao/imagem51.png)

## Fórmulas DAX Contribuição das Dimensões para o Power


### Tabela de Fórmula DAX - % Contribuição

**Legenda Abas:**  
**PI** – Power Importancia 

### Nome Campo: % Contribuição  
**Aba:** PI  
**Fórmula DAX:**
```DAX
SUM(tb_contribuicao_power[pc_contribuicao])
```

**Descrição:**  
```
Calcula o percentual de contribuição para o Power em relação à Dimensão e aos períodos selecionados.
```
---

## Dashboards BIP - Brand Image Profile

Nomes alternativos: "Imagem/BIP (associação relativa)", "Brand Image Profile", "Imagem relativa".

Tabela no BigQuery: "tb_bip_relativo"

Diagrama de relacionamento da tb_bip_relativo no Power BI

![Imagem](documentacao/imagem52.png)

Aba: BIP– Multi Brand Gráficos

![Imagem](documentacao/imagem53.png)

Aba: BIP– Multi Brand Tabela

![Imagem](documentacao/imagem54.png)

Aba: BIP– Multi Period Gráficos

![Imagem](documentacao/imagem55.png)

Aba: BIP– Multi Period Tabela

![Imagem](documentacao/imagem56.png)

## Dashboards Agrupamentos de Atributos BIP e Contribuição para o Power

Tabela no BigQuery: "tb_peso_atributos"

Parte dos dashboards do indicador BIP- Brand Image Profile

![Imagem](documentacao/imagem57.png)

Aba: BIP– Multi Period Gráficos

![Imagem](documentacao/imagem58.png)

## Links e referências

Aplicação desenvolvida pelo time parceiro:
[Monitor de Marcas](https://monitordemarcas.g.globo/)
