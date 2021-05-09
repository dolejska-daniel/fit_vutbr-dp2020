SELECT TIME_BUCKET('1d', s.created_at) AS "time",
       SUM(s.sales_delta) AS "Sales"
FROM product__stats s
WHERE created_at BETWEEN '2021-03-01 12:00' AND NOW()
GROUP BY 1
ORDER BY 1;