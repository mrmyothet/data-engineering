WITH quarterly_revenue AS (
    SELECT
        pickup_year,
        pickup_quarter,
        pickup_year || '/Q' || pickup_quarter AS pickup_year_quarter,
        vendor_id,
        SUM(total_amount) AS quarterly_revenue
    FROM
        {{ ref('fct_taxi_trips') }}
    GROUP BY
        1, 2, 3, 4
),

lagged_quarterly_revenue AS (
    SELECT
        *,
        LAG(quarterly_revenue, 4, 0) OVER (PARTITION BY vendor_id ORDER BY pickup_year, pickup_quarter) AS previous_year_quarterly_revenue
    FROM
        quarterly_revenue
),

yoy_growth AS (
    SELECT
        *,
        (quarterly_revenue - previous_year_quarterly_revenue) / previous_year_quarterly_revenue AS yoy_growth
    FROM
        lagged_quarterly_revenue
),

ranked_growth AS (
    SELECT
        *,
        RANK() OVER (PARTITION BY vendor_id, pickup_year ORDER BY yoy_growth ASC) AS rank_asc,
        RANK() OVER (PARTITION BY vendor_id, pickup_year ORDER BY yoy_growth DESC) AS rank_desc
    FROM
        yoy_growth
    WHERE pickup_year = 2020 -- Considering 2020 as the target year
),

best_worst_quarters AS (
    SELECT
        vendor_id,
        'best' AS metric,
        pickup_year_quarter AS quarter,
        yoy_growth
    FROM ranked_growth
    WHERE rank_desc = 1
    UNION ALL
    SELECT
        vendor_id,
        'worst' AS metric,
        pickup_year_quarter AS quarter,
        yoy_growth
    FROM ranked_growth
    WHERE rank_asc = 1
)

SELECT * FROM best_worst_quarters
ORDER BY vendor_id, metric;