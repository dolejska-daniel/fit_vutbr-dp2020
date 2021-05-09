SELECT pc2.name AS category,
       SUM(sales_delta) AS sales
FROM product__stats ps
INNER JOIN product__items pi ON pi.id = ps.product_id
INNER JOIN product__categories pc1 ON pc1.id = pi.category_id
INNER JOIN product__categories pc2 ON pc2.id = pc1.parent_id
WHERE ps.created_at > '2021-03-01 12:00'
GROUP BY pc2.id
ORDER BY SUM(sales_delta) DESC;
