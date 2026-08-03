# Cloud SQL Provisioner API

API em **FastAPI** que provisiona instâncias **Cloud SQL MySQL** sob demanda, exposta ao **Tsuru** como um serviço plugável. Um time solicita um banco pelo Tsuru, o Tsuru chama esta API, ela cria a instância no GCP e devolve o status (sem que o solicitante precise tocar no console do GCP)


## Arquitetura

```
┌─────────────────────┐                    ┌─────────────────────────────────────────────┐
│  Cluster Kind Local │                    │            Google Cloud Platform            │
│                     │                    │                                             │
│      ┌────────┐     │   HTTP POST        │   ┌──────────────┐      ┌────────────────┐  │
│      │ Tsuru  │─────┼───/resources──────►│   │ Cluster GKE  │      │   Cloud SQL    │  │
│      └────────┘     │                    │   │   ┌──────┐   │  WI  │  ┌──────────┐  │  │
│                     │                    │   │   │ POD  │───┼─────►│  │ Instância│  │  │
└─────────────────────┘                    │   │   │ API  │   │      │  │  MySQL   │  │  │
                                           │   │   └──────┘   │      │  └──────────┘  │  │
                                           │   └──────▲───────┘      └────────────────┘  │
                                           │          │                                  │
                                           └──────────┼──────────────────────────────────┘
                                                      │
                                                 ┌────┴────┐
                                                 │Terraform│  (provisiona GKE, SA, binding WI)
                                                 └─────────┘
```


- **Tsuru** (no cluster kind local) é o cliente: repassa pedidos de criação de banco via contrato HTTP.
- **API FastAPI** (num Pod no GKE) é o servidor: contém toda a lógica de Cloud SQL.
- **Workload Identity** liga a identidade do Pod à Service Account do GCP.
- **Cloud SQL** é onde a instância MySQL de fato nasce, num projeto centralizado da plataforma.
- **Terraform** provisiona a infraestrutura de auth e o cluster.

## Fluxo de ponta a ponta

1. Um usuário roda `tsuru service instance add cloud-sql minha-instancia -t meu-time`.
2. O Tsuru autentica via **HTTP Basic** e faz `POST /resources` na API.
3. A API valida a credencial, traduz o pedido e chama a **Cloud SQL Admin API**.
4. Como a criação é assíncrona, a API responde na hora; 


## Estrutura do projeto

```
app/
  resourcess/   # endpoints do serviço (routes, schema, services, models, tests)
  auth/          # Basic Auth: valida que quem chama é o Tsuru
connections/
  cloud_sql.py      # única camada que fala com a Cloud SQL Admin API
terraform/
  main.tf           # cluster GKE, Service Account, binding KSA→GSA, APIs
  variables.tf
  outputs.tf
  ...
main.py
requirements.txt
```

A separação em camadas (`routes` → `services` → `connections`) é o que permitiu trocar a fonte de credencial (chave JSON → Workload Identity) e o formato do contrato (REST → Tsuru) sem reescrever a lógica de negócio.

