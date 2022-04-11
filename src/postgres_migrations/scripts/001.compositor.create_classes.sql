create role classes with login password 'classes123';
create database classes with owner = classes encoding = 'UTF8' connection limit = -1;
alter database classes set time zone 'Europe/Moscow';
grant all on database classes to classes;
revoke all on database classes from public;
revoke create on schema public from public;