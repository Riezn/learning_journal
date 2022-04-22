SELECT founded_at,
		CONVERT(founded_at, DATE) AS converted_1,
		founded_at_clean,
        CONVERT(founded_at_clean, DATE) as converted_2,
        STR_TO_DATE(founded_at, '%m/%d/%y') AS changed_format
FROM crunchbase_companies_clean_data 

Alter TABLE crunchbase_companies_clean_data
add column founded_clean date;

update crunchbase_companies_clean_data 
set founded_clean= STR_TO_DATE(founded_at, '%m/%d/%y');

SELECT founded_at,
	founded_at_clean,
    founded_clean,
FROM crunchbase_companies_clean_data;

ALTER TABLE crunchbase_companies_clean_data
DROP column founded_at;

select *
from crunchbase_companies_clean_data
