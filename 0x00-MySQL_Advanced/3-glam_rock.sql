-- This script lists bands with Glam rock as their main style, ranked by lifespan 

SELECT band_name, 
       IFNULL((IFNULL(split, 2022) - formed), 0) as lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
