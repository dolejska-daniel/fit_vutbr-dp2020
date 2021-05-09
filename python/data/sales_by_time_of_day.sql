SELECT (CASE WHEN tmp.hours = 24 THEN 0 ELSE tmp.hours END) AS hours,
       tmp.sales
FROM (
   SELECT
     WIDTH_BUCKET(EXTRACT(HOURS FROM created_at), 0, 24, 24) AS hours,
     --WIDTH_BUCKET(EXTRACT(MINUTES FROM created_at), 0, 60, 60) AS minutes,
     SUM(sales_delta) AS "sales"
   FROM product__stats ps
   WHERE ps.created_at > '2021-03-30 00:00'
       AND ps.created_at <= '2021-04-12 23:59'
       AND ps.sales_delta <= 3
   GROUP BY hours  --, minutes
) tmp
ORDER BY hours