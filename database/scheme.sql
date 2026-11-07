create table if not exists cliente (
    id_cliente int auto_increment primary key,
    nome varchar(100) not null,
    cpf varchar(14) not null unique,
    telefone varchar(20) not null,
    email varchar(100)
);

create table if not exists servico (
    id_servico int auto_increment primary key,
    nome_servico varchar(100) not null,
    descricao varchar(255),
    preco_padrao decimal(10, 2) not null,

    constraint ck_servico_preco
    check (preco_padrao >= 0)
);

create table if not exists ordem_servico (
    id_os int auto_increment primary key,
    id_cliente int not null,
    id_servico int not null,
    data_abertura date not null default (current_date),
    valor_cobrado decimal(10, 2) not null,
    status varchar(20) not null default 'Aberta',

    constraint fk_os_cliente
    foreign key (id_cliente)
    references cliente(id_cliente),

    constraint fk_os_servico
    foreign key (id_servico)
    references servico(id_servico),

    constraint ck_os_valor
    check (valor_cobrado >= 0),

    constraint ck_os_status
    check (status in ('Aberta', 'Em Andamento', 'Concluída'))
);