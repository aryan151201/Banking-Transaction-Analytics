CREATE DATABASE BankingTransactionDB;
GO

USE BankingTransactionDB;
GO


CREATE TABLE banking_transactions
(
    transaction_id VARCHAR(20) PRIMARY KEY,
    transaction_date DATE,
    transaction_time TIME,
    transaction_type VARCHAR(10),
    sender_bank VARCHAR(100),
    receiver_bank VARCHAR(100),
    amount DECIMAL(15,2),
    status VARCHAR(20),
    failure_reason VARCHAR(50),
    processing_time_seconds DECIMAL(10,2),
    channel VARCHAR(30),
    region VARCHAR(50)
);
GO


SELECT *
FROM banking_transactions;

USE BankingTransactionDB;
GO

BULK INSERT dbo.banking_transactions
FROM 'C:\Users\aryan\OneDrive\Desktop\Banking-Transaction-Analytics\data\raw\banking_transactions.csv'
WITH
(
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDQUOTE = '"',
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '0x0a',
    CODEPAGE = '65001'
);
GO

SELECT COUNT(*) AS total_transactions
FROM dbo.banking_transactions;

SELECT TOP 10 *
FROM dbo.banking_transactions;

select status ,
count(*) as transaction_count,
cast(count(*)*100.0/(select count(*)from banking_transactions) as decimal(5,2))as percentage
from dbo.banking_transactions
group by status
ORDER BY percentage DESC;

select transaction_type,
count(*) as transaction_count,
cast(count(*)*100.0/(select count (*) from banking_transactions)as decimal(5,2) )as percentage 
from dbo.banking_transactions
group by transaction_type;

select transaction_type,
count (*) as total_transaction,
sum(case when status='success' then 1
else 0
end)as succesfull_transaction,
cast(sum(case when status='success' then 1 
else 0
end)*100.0/count(*) as decimal(5,2)) as sucess_rate 
from banking_transactions
group by transaction_type;


select sender_bank, 
sum( case 
        when status <> 'success' then 1
        else 0
        end) as unsucessful_transaction,
cast(sum( case 
        when status <> 'success' then 1
        else 0
        end) * 100.0/count(*) as decimal(5,2))as failure_rate 

from banking_transactions
group by sender_bank  
order by unsucessful_transaction desc;



select sender_bank, 
sum( case 
        when status <> 'success' then 1
        else 0
        end) as unsucessful_transaction,
cast(sum( case 
        when status <> 'success' then 1
        else 0
        end) * 100.0/count(*) as decimal(5,2))as failure_rate 

from banking_transactions
group by sender_bank  
having sum( case 
        when status <> 'success' then 1
        else 0
        end) * 100.0/count(*)>12
order by unsucessful_transaction desc;


select failure_reason,
count(*) as transaction_count 
from banking_transactions
where status<>'success'
group by failure_reason
order  by transaction_count desc


