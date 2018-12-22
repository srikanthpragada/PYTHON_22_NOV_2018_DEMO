CREATE TABLE jobs (
    id     INTEGER   PRIMARY KEY AUTOINCREMENT,
    title  TEXT (30) NOT NULL,
    minsal INTEGER,
    maxsal INTEGER
);

insert into jobs(title,minsal,maxsal) values('Programmer',10000,50000);
insert into jobs(title,minsal,maxsal) values('Tester',5000,25000);
insert into jobs(title,minsal,maxsal) values('DBA',15000,75000);
insert into jobs(title,minsal,maxsal) values('Data Scientist',20000,75000)

