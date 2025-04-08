select WAREHOUSE_ID, WAREHOUSE_NAME, ADDRESS, IFNULL(FREEZER_YN,  'N') as FREEZER_YN
from FOOD_WAREHOUSE
where ADDRESS LIKE '%경기도%'
order by WAREHOUSE_ID asc;