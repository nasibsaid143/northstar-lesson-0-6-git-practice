You are a patient senior data analyst with experience in retail analytics,
who is teaching a beginner.

Explain customer segmentation by spending tier: what it is, why a business
would do it, and how tiers are typically defined and assigned in SQL.

I'm a junior analyst on my first assignment. I know basic SQL (SELECT, WHERE,
GROUP BY, JOINs, aggregate functions) but have no formal statistics training.
The client is a small online store. The database is PostgreSQL. The relevant
table is `orders` (with columns `order_id`, `customer_id`, `order_date`,
`order_total`). I'll need to split customers into low, mid, and high spenders
based on their total spend over the last 12 months.

Avoid statistical jargon; if a term like "percentile" or "median" is
unavoidable, define it inline in one sentence. Use one small-business example
with made-up numbers. Connect ideas to SQL I already know. Mention one or two
common pitfalls, such as a few very large spenders distorting the tiers. Use a
CTE and CASE WHEN rather than anything more advanced; don't use window
functions yet.

Output: a 250-350 word plain-prose explanation, then one SQL snippet (under 15
lines, with a comment above each CTE) that assigns tiers using the `orders`
table, then a one-sentence takeaway. End with one question I should ask the
client before building the tiers.