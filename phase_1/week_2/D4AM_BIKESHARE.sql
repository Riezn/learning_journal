SELECT start_time,
	duration_seconds,
	SUM(duration_seconds) OVER(ORDER BY start_time) AS running_total
FROM dc_bikeshare_q1_2012;

SELECT start_time,
	duration_seconds,
	SUM(duration_seconds) OVER(PARTITION BY start_time ORDER BY start_time) AS running_total
FROM dc_bikeshare_q1_2012;

SELECT start_time,
	start_terminal,
	duration_seconds,
	SUM(duration_seconds) OVER(PARTITION BY start_terminal ORDER BY start_time) AS running_total
FROM dc_bikeshare_q1_2012;

SELECT start_terminal,
       start_time,
       duration_seconds,
       ROW_NUMBER() OVER (PARTITION BY start_terminal ORDER BY start_time) AS row_number #error dari sqlite
FROM dc_bikeshare_q1_2012;

SELECT start_terminal,
       start_time,
       duration_seconds,
       NTILE(4) OVER (PARTITION BY start_terminal ORDER BY duration_seconds) AS quartile,
       NTILE(5) OVER (PARTITION BY start_terminal ORDER BY duration_seconds) AS quintile
FROM dc_bikeshare_q1_2012;

SELECT start_terminal,
       duration_seconds,
      LAG(duration_seconds, 1) OVER
         (PARTITION BY start_terminal ORDER BY duration_seconds) AS lag,
       LEAD(duration_seconds, 1) OVER
         (PARTITION BY start_terminal ORDER BY duration_seconds) AS lead,
        duration_seconds - LAG(duration_seconds, 1) OVER
        (PARTITION BY start_terminal ORDER BY duration_seconds) AS DIFFERENT
FROM dc_bikeshare_q1_2012
ORDER BY start_terminal, duration_seconds;
