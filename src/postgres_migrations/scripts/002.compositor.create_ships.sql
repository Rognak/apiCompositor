create role ships with login password 'ships123';
create database ships with owner = ships encoding = 'UTF8' connection limit = -1;
alter database ships set time zone 'Europe/Moscow';
grant all on database ships to ships;
revoke all on database ships from public;
revoke create on schema public from public;