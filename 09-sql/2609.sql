SELECT c.name, sum(p.amount) AS sum
FROM products AS p
JOIN categories AS c on c.id = p.id_categories
GROUP BY c.name