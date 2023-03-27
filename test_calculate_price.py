from calculate_price import calculate_price_tea

def test_result_tea_price_30():
    score = 30
    excepted_result = "bubble"
    actual_result = calculate_price_tea(score)
    assert excepted_result == actual_result

def test_result_tea_price_35():
    score = 35
    excepted_result = "grass jelly"
    actual_result = calculate_price_tea(score)
    assert excepted_result == actual_result

def test_result_tea_price_40():
    score = 40
    excepted_result = "red bean,whipped cream,bubble and grass jelly"
    actual_result = calculate_price_tea(score)
    assert excepted_result == actual_result

def test_result_tea_price_45():
    score = 45
    excepted_result = "bubble and red bean,bubble and whipped cream"
    actual_result = calculate_price_tea(score)
    assert excepted_result == actual_result

def test_result_tea_price_50():
    score = 50
    excepted_result = "grass jelly and red bean,grass jelly and whipped cream"
    actual_result = calculate_price_tea(score)
    assert excepted_result == actual_result


def test_result_tea_price_60():
    score = 60
    excepted_result = "red bean and whipped cream"
    actual_result = calculate_price_tea(score)
    assert excepted_result == actual_result

def test_result_only_tea_price_25():
    score = 25
    excepted_result = "Only tea,not have topping"
    actual_result = calculate_price_tea(score)
    assert excepted_result == actual_result