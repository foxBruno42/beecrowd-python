SELECT prod.id,prod.name
FROM products AS prod
JOIN categories AS cat ON cat.id = prod.id_categories
WHERE cat.name LIKE 'super%'