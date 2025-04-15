SELECT t.`ITEM_ID`, i.`ITEM_NAME`, i.`RARITY`
from `ITEM_TREE` t
join `ITEM_INFO` i on i.`ITEM_ID` = t.`ITEM_ID`
join `ITEM_INFO` f on t.`PARENT_ITEM_ID` = f.`ITEM_ID`
where f.`RARITY` = 'RARE'
ORDER BY t.`ITEM_ID` DESC