create user 'pwn' identified with mysql_native_password by '';
create database flag_gopher_isnt_s3cur3;
grant select on flag_gopher_isnt_s3cur3.* to pwn;