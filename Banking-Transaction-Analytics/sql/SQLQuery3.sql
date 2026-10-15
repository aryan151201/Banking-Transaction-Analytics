
CREATE TABLE bank_details
(
    bank_id INT IDENTITY(1,1) PRIMARY KEY,
    bank_name VARCHAR(100),
    bank_type VARCHAR(50),
    headquarters_region VARCHAR(50)
);


select * from bank_details;

INSERT INTO bank_details
    (bank_name, bank_type, headquarters_region)
VALUES
    ('SBI', 'Public', 'Mumbai'),
    ('Bank of Baroda', 'Public', 'Mumbai'),
    ('Punjab National Bank', 'Public', 'New Delhi'),
    ('HDFC Bank', 'Private', 'Mumbai'),
    ('ICICI Bank', 'Private', 'Mumbai'),
    ('Axis Bank', 'Private', 'Mumbai'),
    ('Kotak Bank', 'Private', 'Mumbai'),
    ('IndusInd Bank', 'Private', 'Mumbai'),
    ('Yes Bank', 'Private', 'Mumbai'),
    ('IDFC First Bank', 'Private', 'Mumbai');


    select b.bank_type,
    count(*) as transaction_count 
    from banking_transactions t
    inner join bank_details b
    on t.sender_bank =b.bank_name   
    group by b.bank_type
    order by transaction_count desc;

    SELECT *
FROM bank_details;


SELECT
    b.bank_type,

    COUNT(*) AS total_transactions,

    SUM(
        CASE
            WHEN t.status <> 'SUCCESS' THEN 1
            ELSE 0
        END
    ) AS unsuccessful_transactions,

    CAST(
        SUM(
            CASE
                WHEN t.status <> 'SUCCESS' THEN 1
                ELSE 0
            END
        ) * 100.0 / COUNT(*)
        AS DECIMAL(10,2)
    ) AS failure_rate

FROM banking_transactions t

INNER JOIN bank_details b
    ON t.sender_bank = b.bank_name

GROUP BY b.bank_type

ORDER BY failure_rate DESC;




INSERT INTO bank_details
    (bank_name, bank_type, headquarters_region)
VALUES
    ('Federal Bank', 'Private', 'Kochi');



select b.bank_name ,
count(t.transaction_id) as transaction_count 
from bank_details b
left join banking_transactions t
on t.sender_bank = b.bank_name
group by b.bank_name
order by  transaction_count


SELECT * FROM bank_details;

SELECT bank_name ,bank_type
from bank_details ;

select b.bank_name,
count(t.transaction_id )as transaction_no 
from bank_details b
left join banking_transactions t
on t.sender_bank= b.bank_name
group by b.bank_name 
order by transaction_no

select b.bank_name,
count(t.transaction_id )as transaction_no 
from bank_details b
left join banking_transactions t
on t.sender_bank= b.bank_name
where status='success'
group by b.bank_name 
order by transaction_no

select b.bank_name,
count(t.transaction_id )as transaction_no 
from bank_details b
left join banking_transactions t
on t.sender_bank= b.bank_name
where status='success'
group by b.bank_name 
order by transaction_no
select * from banking_transactions;


select bank_name,
count(t.transaction_id )as transaction_no ,
cast(
sum
(case 
when t.status='success' then  1
else 0
end )*100/count(*)as decimal(10,2)) as successful_transaction
from banking_transactions t
INNER JOIN bank_details b
    ON t.sender_bank = b.bank_name
GROUP BY b.bank_name
order by successful_transaction;


    select b.bank_name,
    count(t.transaction_id)as transaction_no,
    sum(
        case when t.status<>'success' then 1
        else 0
        end )as unsuccesful_transaction,
    cast (
            sum (
            case when t.status<>'success' then 1
            else 0 
            end )*100/ NULLIF(COUNT(t.transaction_id), 0)
            AS DECIMAL(10,2))as unsecufull_perc
    from banking_transactions t
    inner join bank_details b
    on t.sender_bank= b.bank_name 
    group by bank_name
    order by unsuccesful_transaction;

SELECT
    568 * 100.0 / 5163 AS test_failure_rate;


    SELECT
    b.bank_name,
    COUNT(t.transaction_id) AS total_transactions,
    SUM(CASE
            WHEN t.status <> 'SUCCESS' THEN 1
            ELSE 0
        END) AS unsuccessful_transactions,
    SUM(CASE
            WHEN t.status <> 'SUCCESS' THEN 1
            ELSE 0
        END) * 100.0 / COUNT(t.transaction_id) AS calculated_rate
FROM banking_transactions t
INNER JOIN bank_details b
    ON t.sender_bank = b.bank_name
GROUP BY b.bank_name;


