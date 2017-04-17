\i lab3.queries
select ord_id, co_name, ord_product, pr_desc, ord_placed, ord_delivered
from orders, companies, products
where co_id = ord_company and ord_product = pr_id;
\t products
\t
\d products
select ord_id, co_name, ord_product, pr_desc, ord_placed, ord_delivered
from orders, companies, products
where co_id = ord_company and ord_product = pr_code;
select ord_id, co_name, ord_product, pr_desc, ord_placed, ord_delivered
from orders, companies, products
where co_id = ord_company and ord_product = pr_code and ;
select ord_id, co_name, ord_product, pr_desc, ord_placed, ord_delivered
from orders, companies, products
where co_id = ord_company and ord_product = pr_code and 
time_part('year',ord_placed)=2000;
select ord_id, co_name, ord_product, pr_desc, ord_placed, ord_delivered
from orders, companies, products
where co_id = ord_company and ord_product = pr_code and 
date_part('year',ord_placed)=2000;
select ord_id, co_name, ord_product, pr_desc, ord_placed, ord_delivered
;
select ord_id, co_name, pr_desc, ord_placed, ord_delivered
from orders, companies, products
where co_id = ord_company and ord_product = pr_code and 
date_part('year',ord_placed)=2000;
select ord_id, co_name, pr_desc, ord_placed, ord_delivered
from orders, companies, products
where co_id = ord_company and ord_product = pr_code and 
date_part('year',ord_placed)=2000 order by co_name;
\s lab3.q
