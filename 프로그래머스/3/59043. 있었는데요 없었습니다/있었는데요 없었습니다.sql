SELECT i.`ANIMAL_ID`, i.`NAME`
from `ANIMAL_INS` i
left join `ANIMAL_OUTS` o on i.`ANIMAL_ID` = o.`ANIMAL_ID`
where i.`DATETIME` > o.`DATETIME`
ORDER BY i.`DATETIME` asc