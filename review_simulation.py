
def fraud_loss_prevented(scores, amounts, threshold):
    flagged = scores >= threshold
    return amounts[flagged].sum()
