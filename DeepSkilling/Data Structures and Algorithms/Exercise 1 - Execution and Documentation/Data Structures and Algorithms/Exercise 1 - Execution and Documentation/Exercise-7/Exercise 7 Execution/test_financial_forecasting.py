from financial_forecasting import forecast_recursive


def test_forecast_recursive_base_case():
    assert forecast_recursive([100, 110, 120], 0) == []


def test_forecast_recursive_linear_pattern():
    assert forecast_recursive([100, 110, 120], 3) == [130.0, 140.0, 150.0]


def test_forecast_recursive_negative_trend():
    assert forecast_recursive([100, 90, 80], 2) == [70.0, 60.0]
