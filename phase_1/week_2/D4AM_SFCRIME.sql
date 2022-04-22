SELECT location,
	TRIM(LEADING '(' FROM location)
FROM sf_crime_incidents_2014_01;

SELECT category,
	POSITION('A' IN category) AS pos,
    LOWER(category) AS lowered,
    UPPER(address) AS upper
FROM sf_crime_incidents_2014_01;

SELECT day_of_week,
	DATE,
    CONCAT(day_of_week, ', ', DATE) AS day_and_date
FROM sf_crime_incidents_2014_01;

SELECT resolution,
	COALESCE(resolution, "NO RESOLUTION")
FROM sf_crime_incidents_2014_01;