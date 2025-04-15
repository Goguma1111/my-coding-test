SELECT sum(g.`SCORE`) as SCORE, e.`EMP_NO`, e.`EMP_NAME`, e.`POSITION`, e.`EMAIL`  
from `HR_DEPARTMENT` d
join `HR_EMPLOYEES` e on d.`DEPT_ID` = e.`DEPT_ID`
join `HR_GRADE` g on e.`EMP_NO` = g.`EMP_NO`
GROUP BY e.`EMP_NO`
ORDER BY SCORE desc
LIMIT 1
