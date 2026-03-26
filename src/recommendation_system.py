def recommend_action(risk, bias):

    if bias == "High-risk market pattern detected":
        return "Reduce high-volatility exposure and increase diversification"

    if risk > 0.05:
        return "Market volatility is high. Rebalance to lower-risk assets"

    return "Price trends are stable. Continue current allocation and monitoring"