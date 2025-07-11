# 🚀 Projeto GCP - Pipeline de Dados

## Sumário
- [Visão Geral](#visão-geral)
- [Contexto do Negócio](#contexto-do-negócio)
- [Arquitetura da Solução](#arquitetura-da-solução)
- [Camadas de Dados](#camadas-de-dados)
- [Componentes GCP Utilizados](#componentes-gcp-utilizados)
- [Execução e Orquestração](#execução-e-orquestração)
- [Governança e Segurança](#governança-e-segurança)
- [Scripts e Padrões](#scripts-e-padrões)
- [Monitoramento e Logs](#monitoramento-e-logs)
- [Como Executar Manualmente](#como-executar-manualmente)
- [Como Contribuir](#como-contribuir)
- [Licença](#licença)
- [Contato](#contato)

---

## Visão Geral
Este projeto implementa um pipeline completo na **Google Cloud Platform (GCP)** para ingestão, processamento, validação e carga de dados analíticos, permitindo criar uma base consolidada para geração de relatórios e dashboards.

---

## Contexto do Negócio
Muitas empresas precisam monitorar, transformar e disponibilizar dados de diferentes fontes para análises estratégicas. Este pipeline resolve:

- Centralizar dados em um **Data Lakehouse (BigQuery)**.
- Automatizar tarefas repetitivas, como ingestão e tratamento de arquivos.
- Garantir dados prontos para análises em tempo hábil, reduzindo custo operacional.

---

## Arquitetura da Solução
```plaintext
┌─────────────────────────────┐
│     Fonte de Dados          │
│ (CSV, Parquet, JSON, API)   │
└─────────────┬───────────────┘
              │
              ▼
┌─────────────────────────────┐
│     Cloud Storage (GCS)      │
│ - lnd/ : camada landing      │
└─────────────┬───────────────┘
              │
              ▼
┌─────────────────────────────┐
│        Dataproc (Spark)      │
│ - Transformação e limpeza    │
└─────────────┬───────────────┘
              │
              ▼
┌─────────────────────────────┐
│         BigQuery             │
│ - raw.dataset.tables         │
│ - prep.dataset.tables        │
└─────────────┬───────────────┘
              │
              ▼
┌─────────────────────────────┐
│     Data Studio / Looker     │
│    Dashboards e relatórios   │
└─────────────────────────────┘

## Execução Manual
Exemplo de payload JSON para publicar manualmente no tópico Pub/Sub:


{
  "project_id": "seu-projeto-gcp",
  "region": "us-central1",
  "workflow_template": "pipeline-transform",
  "parameters": {
    "DELTA_DAY": "D-1",
    "DATA_INICIO": "2025-07-01",
    "DATA_FIM": "2025-07-10",
    "RUN_LIST": "step1,step2,step3"
  }
}


Governança e Segurança
Uso de Service Accounts específicas, com papéis restritos, seguindo o princípio do menor privilégio.

Dados criptografados em trânsito (TLS) e em repouso.

Auditoria completa via Cloud Audit Logs.

Scripts e Padrões
Scripts Spark desenvolvidos em PySpark, versionados neste repositório.

Padrões de nomenclatura:

Buckets: projeto-solucao-lnd-<ambiente>

Datasets: raw_<projeto>, prep_<projeto>

Tabelas: tb_<entidade>_<detalhe>

Monitoramento e Logs
Stackdriver Logging centraliza logs do Dataproc, Functions e Scheduler.

BigQuery Audit Logs para rastrear quem acessou ou modificou datasets.

Alertas configurados para falhas críticas ou uso anômalo de recursos.

Como Executar Manualmente
Publicação de mensagem diretamente pelo terminal com gcloud:


gcloud pubsub topics publish foundation-start-dataproc-workflow \
  --message='{
    "project_id":"seu-projeto-gcp",
    "region":"us-central1",
    "workflow_template":"pipeline-transform",
    "parameters":{
      "DELTA_DAY":"D-1",
      "DATA_INICIO":"2025-07-01",
      "DATA_FIM":"2025-07-10",
      "RUN_LIST":"step1,step2"
    }
  }'



Como Contribuir
Clone o repositório:


git clone https://github.com/sua-org/seu-projeto-gcp.git
Crie uma branch para suas alterações:


git checkout -b feature/minha-nova-feature
Realize commits e envie seu Pull Request.

Licença
Este projeto é licenciado sob a licença MIT. Para mais detalhes, consulte o arquivo LICENSE.

Contato
Nome	Função	Contato
Valter Lafuente	Data Engineer / Owner	valter.lafuente@exemplo.com
Equipe Analytics	Suporte Técnico	analytics@empresa.com.br

