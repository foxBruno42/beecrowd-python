SELECT m.id,m.name
FROM movies as m
JOIN genres as g on g.id=m.id_genres
WHERE g.description = 'Action'