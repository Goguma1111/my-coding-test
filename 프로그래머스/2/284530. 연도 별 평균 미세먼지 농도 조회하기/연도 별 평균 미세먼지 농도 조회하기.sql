select year(YM) as YEAR, ROUND(avg(PM_VAL1),2) as PM10, ROUND(avg(PM_VAL2), 2) as 'PM2.5'
from AIR_POLLUTION
where LOCATION1 = '경기도' and LOCATION2 = '수원'
group by YEAR
order by YEAR asc;