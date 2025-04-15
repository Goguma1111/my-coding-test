SELECT i.`NAME`, i.`DATETIME`
from `ANIMAL_INS` i
left OUTER join `ANIMAL_OUTS` o on i.`ANIMAL_ID` = o.`ANIMAL_ID`
where o.`ANIMAL_ID` is null
ORDER BY i.`DATETIME` asc
LIMIT 3
