# Executando o backend

Para poder rodar o backend do `MedLembre` é necessário ter o Docker instalado na sua máquina. Caso não tenha, siga as instruções de instalação no site oficial do [Docker](https://docs.docker.com/get-docker/).

Após a instalação do Docker, clone o repositório do `MedLembre` e entre na pasta clonada com os seguintes comandos:

```bash
git clone {url ou ssh do repositorio}
cd med-lembre-back
```

Agora, para rodar o backend, execute o seguinte comando:

```bash
docker-compose up
```

## Resolvendo problemas

 - Erro ao iniciar a api do back pelo `docker-compose up`;
   entre no arquivo banco/\_\_init\_\_.py e altere essas linhas:
   ```python
   engine = create_async_engine(
       "postgresql+asyncpg://postgres:postgres@localhost:5432/postgres",
   )
   ```
   para:
   ```python
   engine = create_async_engine(
       "postgresql+asyncpg://postgres:postgres@{nome do pod do postgres que o docker cria, exemplo: med-lembre-back-db-1}:5432/postgres",
   )
   ```
