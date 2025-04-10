SELECT COUNT(*) as USERS
from `USER_INFO`
where year(joined) = 2021 and age BETWEEN 20 and 29