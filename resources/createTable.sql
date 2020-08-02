create table if not exists hk_stock_list(
    id int  not null auto_increment  primary key,
    symbol varchar(8) not null,
    name varchar(30) not null,
    engname varchar(50) not null,
    tradetype varchar(10) not null
    );

create table if not exists stock_list_exist(
    id int  not null auto_increment  primary key,
    symbolstr text not null,
    type varchar(30) not null,
    count int(10) not null
    );

create table if not exists us_stock_list(
    id int  not null auto_increment  primary key,
    name varchar(100) not null,
    cname varchar(100) not null,
    type varchar(30) not null,
    symbol varchar(10) not null,
    market varchar(10) not null
    );

create table if not exists hk_stock_daily(
    id int  not null auto_increment  primary key,
    symbol varchar(8) not null,
    date date not null,
    open float not null,
    high float not null,
    low float not null,
    close float not null,
    volume float not null
    );

create table if not exists us_stock_daily(
    id int  not null auto_increment  primary key,
    symbol varchar(8) not null,
    date date not null,
    open float not null,
    high float not null,
    low float not null,
    close float not null,
    volume float not null
    );

create table if not exists stock_index_daily(
    id int  not null auto_increment  primary key,
    indexname varchar(30) not null,
    date date not null,
    open float(10,2) not null,
    high float(10,2) not null,
    low float(10,2) not null,
    close float(10,2) not null,
    volume float not null
    );