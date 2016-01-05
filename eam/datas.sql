/*==============================================================*/
/* 修改为自增长、ID改为number类型、列的取舍、是否为空           */
/* dbms name:      mysql 5.0                                    */
/* created on:     2015/12/22 9:25:18                           */
/*==============================================================*/

drop database ciseam;
create database ciseam DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
use ciseam;

drop table if exists eam_asset;

drop table if exists eam_attributes;

drop table if exists eam_maintenance;

drop table if exists eam_usagerecord;

drop table if exists eam_user;

/*==============================================================*/
/* table: user                                                  */
/*==============================================================*/
create table eam_user
(
   id                   int(8) not null auto_increment,
   user_name            varchar(10) not null,
   tel                  numeric(11,0),
   qq                   numeric(15,0),
   email                varchar(50),
   user_comment         varchar(3000),
   primary key (id)
) engine=innodb;

/*==============================================================*/
/* table: asset                                                 */
/*==============================================================*/
create table eam_asset
(
   id                   int(8) not null auto_increment,
   asset_mark           varchar(300) not null,
   asset_name           varchar(300) not null,
   intake_date          date,
   warranty_period      varchar(50),
   price                numeric(10,2),
   primary key (id)
) engine=innodb;

/*==============================================================*/
/* table: attributes                                            */
/*==============================================================*/
create table eam_attributes
(
   id                   int(8) not null auto_increment,
   asset_id             int(8) not null,
   attribute_key        varchar(300) not null,
   attribute_value      varchar(300) not null,
   primary key (id)
) engine=innodb;

/*==============================================================*/
/* table: usage_record                                          */
/*==============================================================*/
create table eam_usagerecord
(
   id                   int(8) not null auto_increment,
   asset_id             int(8) not null,
   user_id              int(8) not null,
   begin_date           date not null,
   end_date             date,
   primary key (id)
) engine=innodb;

/*==============================================================*/
/* table: maintenance                                           */
/*==============================================================*/
create table eam_maintenance
(
   id                   int(8) not null auto_increment,
   user_id              int(8),
   asset_id             int(8) not null,
   fault_cause          varchar(3000) not null,
   occur_date           date not null,
   repair_date          date,
   repair_result        varchar(500),
   primary key (id)
) engine=innodb;

alter table eam_attributes add constraint fk_asset_attributes foreign key (asset_id)
      references eam_asset (id) on delete cascade on update cascade;

alter table eam_maintenance add constraint fk_asset_maintenance foreign key (asset_id)
      references eam_asset (id) on delete cascade on update cascade;

alter table eam_maintenance add constraint fk_user_maintenance foreign key (user_id)
      references eam_user (id) on delete cascade on update cascade;

alter table eam_usagerecord add constraint fk_asset_usage foreign key (asset_id)
      references eam_asset (id) on delete cascade on update cascade;

alter table eam_usagerecord add constraint fk_user_usage foreign key (user_id)
      references eam_user (id) on delete cascade on update cascade;

/*------------------------------------------------------*/

/*向用户表中插入数据*/
insert into eam_user(user_name,tel,user_comment) values('刘一',18312123434,'长得帅');
insert into eam_user(user_name,tel,user_comment) values('陈二',18312123434,'长得帅');
insert into eam_user(user_name,tel,user_comment) values('张三',18312123434,'长得帅');
insert into eam_user(user_name,tel,user_comment) values('李四',18312123434,'长得帅');
insert into eam_user(user_name,tel,user_comment) values('王五',18312123434,'长得帅');
insert into eam_user(user_name,tel,user_comment) values('赵六',18312123434,'长得帅');
insert into eam_user(user_name,tel,user_comment) values('孙七',18312123434,'长得帅');
insert into eam_user(user_name,tel,user_comment) values('周八',18312123434,'长得帅');
insert into eam_user(user_name,tel,user_comment) values('吴九',18312123434,'长得帅');
insert into eam_user(user_name,tel,user_comment) values('郑十',18312123434,'长得帅');

/*向资产表中插入数据*/
insert into eam_asset(asset_name,asset_mark) values('联想笔记本电脑','L-1');
insert into eam_asset(asset_name,asset_mark) values('联想笔记本电脑','L-2');
insert into eam_asset(asset_name,asset_mark) values('联想笔记本电脑','L-3');
insert into eam_asset(asset_name,asset_mark) values('联想笔记本电脑','L-4');
insert into eam_asset(asset_name,asset_mark) values('联想笔记本电脑','L-5');
insert into eam_asset(asset_name,asset_mark) values('联想笔记本电脑','L-6');
insert into eam_asset(asset_name,asset_mark) values('联想笔记本电脑','L-7');
insert into eam_asset(asset_name,asset_mark) values('联想笔记本电脑','L-8');
insert into eam_asset(asset_name,asset_mark) values('联想笔记本电脑','L-9');
insert into eam_asset(asset_name,asset_mark) values('联想笔记本电脑','L-10');

/*向资产属性表中插入数据*/
select @asset_id := (select id from eam_asset where asset_mark='L-1');
insert into eam_attributes(asset_id,attribute_key,attribute_value) values(@asset_id,'CPU','8Core');
insert into eam_attributes(asset_id,attribute_key,attribute_value) values(@asset_id,'MEM','8G');

select @asset_id := (select id from eam_asset where asset_mark='L-2');
insert into eam_attributes(asset_id,attribute_key,attribute_value) values(@asset_id,'CPU','8Core');
insert into eam_attributes(asset_id,attribute_key,attribute_value) values(@asset_id,'MEM','8G');

/*向使用记录表中插入数据*/
select @begin_date := date("2011-12-29");
select @end_date := date("2015-12-19");

select @asset_id := (select id from eam_asset where asset_mark='L-1');
select @user_id := (select id from eam_user where user_name='刘一');
insert into eam_usagerecord(asset_id,user_id,begin_date,end_date) values(@asset_id,@user_id,@begin_date,@end_date);

select @asset_id := (select id from eam_asset where asset_mark='L-2');
select @user_id := (select id from eam_user where user_name='陈二');
insert into eam_usagerecord(asset_id,user_id,begin_date,end_date) values(@asset_id,@user_id,@begin_date,@end_date);

select @asset_id := (select id from eam_asset where asset_mark='L-3');
select @user_id := (select id from eam_user where user_name='张三');
insert into eam_usagerecord(asset_id,user_id,begin_date,end_date) values(@asset_id,@user_id,@begin_date,@end_date);

select @asset_id := (select id from eam_asset where asset_mark='L-4');
select @user_id := (select id from eam_user where user_name='李四');
insert into eam_usagerecord(asset_id,user_id,begin_date,end_date) values(@asset_id,@user_id,@begin_date,@end_date);

select @asset_id := (select id from eam_asset where asset_mark='L-5');
select @user_id := (select id from eam_user where user_name='王五');
insert into eam_usagerecord(asset_id,user_id,begin_date,end_date) values(@asset_id,@user_id,@begin_date,@end_date);

select @asset_id := (select id from eam_asset where asset_mark='L-6');
select @user_id := (select id from eam_user where user_name='赵六');
insert into eam_usagerecord(asset_id,user_id,begin_date,end_date) values(@asset_id,@user_id,@begin_date,@end_date);

select @asset_id := (select id from eam_asset where asset_mark='L-7');
select @user_id := (select id from eam_user where user_name='孙七');
insert into eam_usagerecord(asset_id,user_id,begin_date,end_date) values(@asset_id,@user_id,@begin_date,@end_date);

select @asset_id := (select id from eam_asset where asset_mark='L-8');
select @user_id := (select id from eam_user where user_name='周八');
insert into eam_usagerecord(asset_id,user_id,begin_date,end_date) values(@asset_id,@user_id,@begin_date,@end_date);

select @asset_id := (select id from eam_asset where asset_mark='L-9');
select @user_id := (select id from eam_user where user_name='吴九');
insert into eam_usagerecord(asset_id,user_id,begin_date,end_date) values(@asset_id,@user_id,@begin_date,@end_date);

select @asset_id := (select id from eam_asset where asset_mark='L-10');
select @user_id := (select id from eam_user where user_name='郑十');
insert into eam_usagerecord(asset_id,user_id,begin_date,end_date) values(@asset_id,@user_id,@begin_date,@end_date);


/*向维修记录表中插入数据*/
select @occur_date := date("2012-12-29");
select @asset_id := (select id from eam_asset where asset_mark='L-2');
select @user_id := (select id from eam_user where user_name='王五');
insert into eam_maintenance(asset_id,user_id,fault_cause,occur_date) values(@asset_id,@user_id,'王五踹了陈二的电脑一脚',@occur_date);

select @occur_date := date("2013-1-2");
select @asset_id := (select id from eam_asset where asset_mark='L-5');
insert into eam_maintenance(asset_id,fault_cause,occur_date) values(@asset_id,'自己死机了',@occur_date);

/*------------------------------------------------------*/

/*查询数据*/
select * from eam_user;
select * from eam_asset;
select * from eam_attributes;
select * from eam_usagerecord;
select * from eam_maintenance;

/*测试外键约束*/
insert into eam_maintenance(asset_id) values('11');
