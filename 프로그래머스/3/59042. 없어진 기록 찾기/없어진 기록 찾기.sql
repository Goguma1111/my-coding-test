SELECT o.`ANIMAL_ID`, o.`NAME`
FROM `ANIMAL_OUTS` o
left OUTER join `ANIMAL_INS` i on o.`ANIMAL_ID` = i.`ANIMAL_ID`
where i.`ANIMAL_ID` is null
