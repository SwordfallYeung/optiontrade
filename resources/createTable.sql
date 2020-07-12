create table if not exists hk_stock_list(
    id int  not null auto_increment  primary key,
    symbol varchar(8) not null,
    name varchar(30) not null,
    engname varchar(50) not null,
    tradetype varchar(10) not null
    );

create table if not exists hk_stock_list_exist(
    id int  not null auto_increment  primary key,
    symbolstr text not null,
    count int(10) not null
    );