SELECT prod.name AS product_name, prov.name AS provider_name
FROM products AS prod
JOIN providers AS prov ON prov.id = prod.id_providers
WHERE prod.id_categories = 6;