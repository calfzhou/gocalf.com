---
title: Database Migration Tools
notebook: notes
tags:
  - it/database
date: 2024-06-29 17:08:06
updated: 2024-06-29 17:18:24
---
## golang-migrate

[golang-migrate/migrate: Database migrations. CLI and Golang library.](https://github.com/golang-migrate/migrate)

{% badge_github golang-migrate migrate release:true %}

``` bash
curl -OL https://github.com/golang-migrate/migrate/releases/download/v4.15.0/migrate.linux-amd64.tar.gz
tar -zxf migrate.linux-amd64.tar.gz
mv migrate /usr/local/bin/
rm migrate.linux-amd64.tar.gz LICENSE README.md
migrate --version
# 4.15.0
```

golang-migrate 会在目标库中创建一张 `schema_migrations` 表，记录当前的版本信息。表中只有一行数据，记录最后的版本号。

``` bash
migrate create -seq -ext sql -dir PATH/TO/MIGRATION/FOLDER MIGRATION_NAME

migrate -path PATH/TO/MIGRATION/FOLDER -database URI version
migrate -path PATH/TO/MIGRATION/FOLDER -database URI -verbose up 1
migrate -path PATH/TO/MIGRATION/FOLDER -database URI -verbose down 1
migrate -path PATH/TO/MIGRATION/FOLDER -database URI -verbose force N
```

常用命令：

``` text
Commands:
  create [-ext E] [-dir D] [-seq] [-digits N] [-format] [-tz] NAME
        Create a set of timestamped up/down migrations titled NAME, in directory D with extension E.
        Use -seq option to generate sequential up/down migrations with N digits.
        Use -format option to specify a Go time format string. Note: migrations with the same time cause "duplicate migration version" error.
        Use -tz option to specify the timezone that will be used when generating non-sequential migrations (defaults: UTC).

  goto V       Migrate to version V
  up [N]       Apply all or N up migrations
  down [N] [-all]    Apply all or N down migrations
        Use -all to apply all down migrations
  drop [-f]    Drop everything inside database
        Use -f to bypass confirmation
  force V      Set version V but don't run migration (ignores dirty state)
  version      Print current migration version
```

- 已知的小遗憾是不太适配 ByteDance 出的 ByteHouse CDW（云数仓版），因为 ByteHouse CDW 的 `SHOW TABLES FROM "db" LIKE '...'` 语句查询的结果不正确。
- 不确定用在 ClickHouse 的时候是否支持 multi-statements。

## goose

[pressly/goose: A database migration tool. Supports SQL migrations and Go functions.](https://github.com/pressly/goose)

{% badge_github pressly goose release:true %}

``` bash
brew install goose
goose -version
# goose version: v3.21.1
```

``` bash
GOOSE_VERSION=3.21.1
curl -fsSL https://raw.githubusercontent.com/pressly/goose/master/install.sh | sh -s v${GOOSE_VERSION}
```

goose 会在目标数据库中创建一张 `goose_db_version` 表，用来记录执行过的版本变更列表。表里首先会初始化一条 `version = 0` 的初始数据，之后每个版本都会增加一条对应的数据。

``` bash
goose -dir PATH/TO/MIGRATION/FOLDER -s create NAME sql
goose -dir PATH/TO/MIGRATION/FOLDER URI status
```

最终进入代码版本控制的 migration 文件应该用 sequential versions。参见 [Hybrid Versioning](https://github.com/pressly/goose?tab=readme-ov-file#hybrid-versioning)。

> Migrations created during the development process are timestamped and sequential versions are ran on production.
> We believe this method will prevent the problem of conflicting versions when writing software in a team environment.

常用命令：

``` text
Commands:
    up                   Migrate the DB to the most recent version available
    up-by-one            Migrate the DB up by 1
    up-to VERSION        Migrate the DB to a specific VERSION
    down                 Roll back the version by 1
    down-to VERSION      Roll back to a specific VERSION
    redo                 Re-run the latest migration
    reset                Roll back all migrations
    status               Dump the migration status for the current DB
    version              Print the current version of the database
    create NAME [sql|go] Creates new migration file with the current timestamp
    fix                  Apply sequential ordering to migrations
    validate             Check migration files without running them
```

- 在 ByteHouse CDW v2+ 上可以正常使用。

## 其他

[Homepage - Flyway](https://flywaydb.org/)

免费版不支持 rollback；免费版不支持 PostgreSQL 9.4。

[Liquibase | Open Source Version Control for Your Database](https://www.liquibase.org/)

设计的很诡异，看起来很难用。

Flyway and Liquibase both deliver version control for your database - which makes schema migrations more simple.
