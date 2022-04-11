create role outcomes with login password 'outcomes123';
create database outcomes with owner = outcomes encoding = 'UTF8' connection limit = -1;
alter database outcomes set time zone 'Europe/Moscow';
grant all on database outcomes to outcomes;
revoke all on database outcomes from public;
revoke create on schema public from public;