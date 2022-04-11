create role battles with login password 'battles123';
create database battles with owner = battles encoding = 'UTF8' connection limit = -1;
alter database battles set time zone 'Europe/Moscow';
grant all on database battles to battles;
revoke all on database battles from public;
revoke create on schema public from public;