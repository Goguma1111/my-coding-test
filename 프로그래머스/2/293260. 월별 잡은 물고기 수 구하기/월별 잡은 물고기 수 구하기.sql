SELECT count(FISH_TYPE) as FISH_COUNT, MONTH(TIME) as MONTH 
from `FISH_INFO`
GROUP BY MONTH
ORDER BY MONTH asc;