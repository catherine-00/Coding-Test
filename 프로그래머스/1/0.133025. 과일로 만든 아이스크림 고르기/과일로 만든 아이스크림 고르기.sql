-- 코드를 입력하세요
SELECT
    H.FLAVOR
FROM FIRST_HALF AS H
JOIN ICECREAM_INFO AS I
    ON H.FLAVOR = I.FLAVOR
WHERE TOTAL_ORDER > 3000
    AND INGREDIENT_TYPE = 'fruit_based'
ORDER BY TOTAL_ORDER DESC;
