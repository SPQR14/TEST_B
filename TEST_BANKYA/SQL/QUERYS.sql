use credits;

INSERT INTO PAGOS VALUES(1, 1, '2020-10-13', 10318.11, 10318.11, '2020-10-13');

SELECT @@sql_mode;

SELECT c.NOMBRE, c.APELLIDOS, p.CONTRACTID, p.PAYMENTID, p.MONTO_PAGO, p.FECHA_PAGO
from CLIENTES c join PRESTAMOS o on c.CUSTOMERID = o.CUSTOMERID
join PAGOS p on p.CONTRACTID = o.CONTRACTID;

select * from PRESTAMOS;
select * from PAGOS;

-- Select all customers that have multiple active loans
SELECT c.NOMBRE, c.CUSTOMERID ,c.APELLIDOS, COUNT(*) as ACTIVE_LOANS
from CLIENTES c join PRESTAMOS p on p.CUSTOMERID =  c.CUSTOMERID
GROUP BY c.CUSTOMERID
HAVING COUNT(*) > 1;

-- Select the total amount paid grouped by zip code and age buckets
SELECT SUM(p.MONTO_PAGO) AS TOTAL_PAGADO, c.CP, c.EDAD
from CLIENTES c join PRESTAMOS o on c.CUSTOMERID = o.CUSTOMERID
join PAGOS p on p.CONTRACTID = o.CONTRACTID
group by c.CP, c.EDAD order by c.CP ASC;


-- Select the total amount paid and the average number of payments made by customers that have only one active loan
CREATE VIEW TABLOTA AS SELECT c.NOMBRE, c.APELLIDOS, c.EDAD, o.CONTRACTID, o.CUSTOMERID, p.PAYMENTID, p.MONTO_PAGO
 FROM CLIENTES c JOIN PRESTAMOS o ON c.CUSTOMERID = o.CUSTOMERID JOIN PAGOS p ON o.CONTRACTID = p.CONTRACTID;

SELECT c.CUSTOMERID, c.NOMBRE ,c.APELLIDOS, COUNT(*) as ACTIVE_LOANS, SUM(o.MONTO_PAGO)
from CLIENTES c join PRESTAMOS p on p.CUSTOMERID =  c.CUSTOMERID JOIN PAGOS o ON p.CONTRACTID = o.CONTRACTID
GROUP BY c.CUSTOMERID
HAVING COUNT(*) = 1;