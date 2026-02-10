-- 3-glam_rock.sql
-- Lists all bands with Glam rock as their main style, ranked by longevity
-- Column names: band_name and lifespan (in years up to 2024)

SELECT 
    band_name,
    (IFNULL(split, 2024) - formed) AS lifespan
FROM 
    metal_bands
WHERE 
    style LIKE '%Glam rock%'
ORDER BY 
    lifespan DESC;
