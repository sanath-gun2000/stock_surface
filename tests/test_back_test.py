"""
Author Jason Bamford
Date Aug 2 2018

"""
import get_tickers as get_tickers
import back_test as back_test
import pandas as pd
import sample_slopes as sample_slopes


def test_batcher():
    data = {'col1CLS': [3, 3, 4, 5, 7, 8, 7, 6, 5, 4],
            'col2CLS': [6, 5, 5, 6, 7, 6, 4, 3, 3, 8],
            'col3CLS': [7, 6, 4, 6, 4, 2, 4, 5, 6, 5],
            'col4CLS': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            'col5CLS': [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
            'col1CHG': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            'col2CHG': [4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
            'col3CHG': [4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
            'col4CHG': [4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
            'col5CHG': [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
            'col2slope_sum': [13, 8, -3, 3, 3, 3, 3, 3, 3, 3],
            'col3slope_sum': [1, -3, 3, 5, 3, 3, 3, 3, 3, 3],
            'col4slope_sum': [9, 3, 9, 3, -3, 3, 3, 3, 3, 3],
            }
    stock_data = pd.DataFrame(data=data)
    back_Test = back_test.BackTest(
        stock_data, '/Users/jasonbamford/workspace/stock_surface/model_3_batch.pkl')
    assert len(back_Test.create_batch_of_slopes(
        stock_data, 'col4slope_sum', 2, 3)) == 3
    assert back_Test.create_batch_of_slopes(stock_data, 'col4slope_sum', 2, 3) == [
        [9, 3], [3, 9], [9, 3]]


def test_generate_buy_sells():
    data = {'col1CLS': [3, 3, 4, 5, 7, 8, 7, 6, 5, 4],
            'col2CLS': [6, 5, 5, 6, 7, 6, 4, 3, 3, 8],
            'col3CLS': [7, 6, 4, 6, 4, 2, 4, 5, 6, 5],
            'col4CLS': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            'col5CLS': [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
            'col1CHG': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            'col2CHG': [4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
            'col3CHG': [4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
            'col4CHG': [4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
            'col5CHG': [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
            'col2slope_sum': [13, 8, -3, 3, 3, 3, 3, 3, 3, 3],
            'col3slope_sum': [1, -3, 3, 5, 3, 3, 3, 3, 3, 3],
            'col4slope_sum': [9, 3, 9, 3, -3, 3, 3, 3, 3, 3],
            }
    stock_data = pd.DataFrame(data=data)

    back_Test = back_test.BackTest(
        stock_data, '/Users/jasonbamford/workspace/stock_surface/model_18_batch.pkl')
    assert back_Test.generate_buy_sells(
        [9, 3, 9, 3, 9, 3, -3, 3, 3, 3, 3, 3, 4, 5, 6, 1, 3, 4]) == 0


def test_append_list_of_buy_sells():
    """
    used to make sure that the bid stream can be added to the main data frame
    """
    data = {'col1CLS': [3, 3, 4, 5, 7, 8, 7, 6, 5, 4],
            'col2CLS': [6, 5, 5, 6, 7, 6, 4, 3, 3, 8],
            'col3CLS': [7, 6, 4, 6, 4, 2, 4, 5, 6, 5],
            'col4CLS': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            'col5CLS': [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
            'col1CHG': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            'col2CHG': [4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
            'col3CHG': [4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
            'col4CHG': [4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
            'col5CHG': [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
            'col2slope_sum': [13, 8, -3, 3, 3, 3, 3, 3, 3, 3],
            'col3slope_sum': [1, -3, 3, 5, 3, 3, 3, 3, 3, 3],
            'col4slope_sum': [9, 3, 9, 3, -3, 3, 3, 3, 3, 3]
            }
    stock_data = pd.DataFrame(data=data)

    # stock_data = pd.read_pickle('df_without_zeros.pkl')

    back_Test = back_test.BackTest(
        stock_data, '/Users/jasonbamford/workspace/stock_surface/model_3_batch.pkl')

    array_of_batches = back_Test.create_batch_of_slopes(
        stock_data, 'col4slope_sum', 3, 9)

    print array_of_batches
    print back_Test.append_list_of_buy_sells(array_of_batches, "col4slope_sum")

    assert len(back_Test.main_df['col4bid_stream']) == 10


def test_log_return():
    """
    make sure does log return right
    """
    data = {'col1CLS': [3, 3, 4, 5, 7, 8, 7, 6, 5, 4],
            'col2CLS': [6, 5, 5, 6, 7, 6, 4, 3, 3, 8],
            'col3CLS': [7, 6, 4, 6, 4, 2, 4, 5, 6, 5],
            'col4CLS': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            'col5CLS': [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
            'col1CHG': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            'col2CHG': [4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
            'col3CHG': [4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
            'col4CHG': [4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
            'col5CHG': [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
            'col2slope_sum': [13, 8, -3, 3, 3, 3, 3, 3, 3, 3],
            'col3slope_sum': [1, -3, 3, 5, 3, 3, 3, 3, 3, 3],
            'col4slope_sum': [9, 3, 9, 3, -3, 3, 3, 3, 3, 3]
            }
    stock_data = pd.DataFrame(data=data)
    back_Test = back_test.BackTest(
        stock_data, '/Users/jasonbamford/workspace/stock_surface/model_3_batch.pkl')

    assert back_Test.log_return(10, 5) == 0.6931471805599453
    assert back_Test.log_return(1.1, 1.0) == 0.09531017980432493


def test_take_bid_stream_calculate_return():
    """
    makes sure that when it takes a bid stream it popary records the corect log returns over time

    """
    data = {'col1CLS': [3, 3, 4, 5, 7, 8, 7, 6, 5, 4],
            'col2CLS': [6, 5, 5, 6, 7, 6, 4, 3, 3, 8],
            'col3CLS': [7, 6, 4, 6, 4, 2, 4, 5, 6, 5],
            'col4CLS': [1, 1, 1, 1, 55555, 1, 1, 1, 1, 1],
            'col5CLS': [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
            'col1CHG': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            'col2CHG': [4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
            'col3CHG': [4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
            'col4CHG': [4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
            'col5CHG': [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
            'col2slope_sum': [13, 8, -3, 3, 3, 3, 3, 3, 3, 3],
            'col3slope_sum': [1, -3, 3, 5, 3, 3, 3, 3, 3, 3],
            'col4slope_sum': [9, 3, 9, 3, -3, 3, 3, 3, 3, 3],
            'col4slope_sum': [1, 1.2, 1.3, 1.7, 1.5, 1.2, 1.5, 1.6, 1.7, 1.8],
            }
    stock_data = pd.DataFrame(data=data)

    # stock_data = pd.read_pickle('df_without_zeros.pkl')

    Back_Test = back_test.BackTest(
        stock_data, '/Users/jasonbamford/workspace/stock_surface/model_3_batch.pkl')

    array_of_batches = Back_Test.create_batch_of_slopes(
        stock_data, 'col4slope_sum', 3, 9)

    print array_of_batches
    print Back_Test.append_list_of_buy_sells(array_of_batches, "col4slope_sum"), 'yoo'

    print Back_Test.take_bid_stream_calculate_return("col4bid_stream", 3, 2), 'tada'


def test_take_bid_stream_calculate_return1():
    """
    makes sure that when it takes a bid stream it popary records the corect log returns over time

    """
    data = {
        'col4CLS': [1, 1.2, 1.3, 1.7, 1.5, 1.2, 1.5, 1.6, 1.7, 1.8, 1.9, 2, 2.1, 2.4, 2.1, 2.6, 2.7, 2.1, 2.0, 1.6, 1.9, 1.2, 1.6, 2, 2.1],
        'col4slope_sum': [1, 1.2, 1.3, 1.7, 1.5, 1.2, 1.5, 1.6, 1.7, 1.8, 1.9, 2, 2.1, 2.4, 2.2, 2.6, 2.7, 2.1, 2.0, 1.6, 1.9, 1.2, 1.6, 2, 2.1],
        'col4bid_stream': [1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1]
    }
    stock_data = pd.DataFrame(data=data)

    # stock_data = pd.read_pickle('df_without_zeros.pkl')

    Back_Test = back_test.BackTest(
        stock_data, '/Users/jasonbamford/workspace/stock_surface/model_3_batch.pkl')

    array_of_batches = Back_Test.create_batch_of_slopes(
        stock_data, 'col4slope_sum', 3, 9)

    print Back_Test.take_bid_stream_calculate_return("col4bid_stream", 3, 2), 'tada'


def test_calculate_holding_percent_change_return():
    """
    make sure it does percetn chagnge correct
    """
    data = {
        'col4CLS': [1, 1.2, 1.3, 1.7, 1.5, 1.2, 1.5, 1.6, 1.7, 1.8, 1.9, 2, 2.1, 2.4, 2.1, 2.6, 2.7, 2.1, 2.0, 1.6, 1.9, 1.2, 1.6, 2, 2.1],
        'col4slope_sum': [1, 1.2, 1.3, 1.7, 1.5, 1.2, 1.5, 1.6, 1.7, 1.8, 1.9, 2, 2.1, 2.4, 2.2, 2.6, 2.7, 2.1, 2.0, 1.6, 1.9, 1.2, 1.6, 2, 2.1],
        'col4bid_stream': [1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1]
    }
    stock_data = pd.DataFrame(data=data)

    # stock_data = pd.read_pickle('df_without_zeros.pkl')

    Back_Test = back_test.BackTest(
        stock_data, '/Users/jasonbamford/workspace/stock_surface/model_3_batch.pkl')
    assert Back_Test.calculate_holding_percent_change_return("col4CLS") == 1.1


def test_on_market_data_single_stock():
    """
    This test is used to try out the returns calculator on the stock market data

    """

    main_df = pd.read_pickle('df_without_zeros.pkl')
    main_df = sample_slopes.create_slope_sum(main_df)

    Back_Test = back_test.BackTest(
        main_df, '/Users/jasonbamford/workspace/stock_surface/model_18_batch.pkl')

    y_values = sample_slopes.generate_target_values(
        main_df, 18, 'FBCLS', 2)

    x_values = sample_slopes.create_batch_of_slopes(
        main_df, 'FBCLS', 18,   y_values[1])

    array_of_batches = Back_Test.create_batch_of_slopes(
        main_df, 'FBslope_sum', 18, y_values[1])

    print array_of_batches, ' here is lensss'

    print Back_Test.append_list_of_buy_sells(array_of_batches,
                                             "FBslope_sum")

    print "algorithm ", sum(Back_Test.take_bid_stream_calculate_return("FBbid_stream", 18, 2)) * 100, '%'
    print "log return ", sum(Back_Test.test_calculate_holding_log_return('FBCLS')) * 100, '%'
    print "percent change", Back_Test.calculate_holding_percent_change_return("FBCLS") * 100, '%'


def test_calculate_holding_return():
    """
    Makes sure that we can caculate the return if we just had held the stock
    """
    data = {
        'col4CLS': [1, 1.2, 1.3, 1.7, 1.5, 1.2, 1.5, 1.6, 1.7, 1.8, 1.9, 2, 2.1, 2.4, 2.1, 2.6, 2.7, 2.1, 2.0, 1.6, 1.9, 1.2, 1.6, 2, 2.1],
        'col4slope_sum': [1, 1.2, 1.3, 1.7, 1.5, 1.2, 1.5, 1.6, 1.7, 1.8, 1.9, 2, 2.1, 2.4, 2.2, 2.6, 2.7, 2.1, 2.0, 1.6, 1.9, 1.2, 1.6, 2, 2.1],
        'col4bid_stream': [1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1]
    }
    stock_data = pd.DataFrame(data=data)

    # stock_data = pd.read_pickle('df_without_zeros.pkl')

    Back_Test = back_test.BackTest(
        stock_data, '/Users/jasonbamford/workspace/stock_surface/model_3_batch.pkl')

    print sum(Back_Test.test_calculate_holding_log_return('col4CLS'))


def test_on_array_of_market():
    """
    This test is used to try out the returns calculator on the stock market data

    """
    tickers = ["GOOG", "FB", "INTC", 'TSM',
               "CSCO", "ORCL", "NVDA", "SAP", "IBM", "ADBE",
               "TXN", "AVGO", "CRM", "QCOM", "MU", "BIDU",
               "ADP", "VMW", "ATVI", "AMAT", "INTU",
               "CTSH", "EA", "EA", "NXPI", "INFY"]

    # tickers = ["GOOG", "FB", "INTC", 'TSM', "CSCO"]

    main_df = pd.read_pickle('df_without_zeros.pkl')
    main_df = sample_slopes.create_slope_sum(main_df)

    Back_Test = back_test.BackTest(
        main_df, '/Users/jasonbamford/workspace/stock_surface/model_18_batch.pkl')

    with open('return_output.csv', 'w') as f:
        for ticker in tickers:

            y_values = sample_slopes.generate_target_values(
                main_df, 18, ticker + "CLS", 2)

            x_values = sample_slopes.create_batch_of_slopes(
                main_df, ticker + 'CLS', 18,   y_values[1])

            array_of_batches = Back_Test.create_batch_of_slopes(
                main_df, ticker + 'slope_sum', 18, y_values[1])

            Back_Test.append_list_of_buy_sells(array_of_batches,
                                               ticker + "slope_sum")

            algorithm_return = sum(Back_Test.take_bid_stream_calculate_return(
                ticker + "bid_stream", 18, 2)) * 100
            log_return = sum(
                Back_Test.test_calculate_holding_log_return(ticker + 'CLS')) * 100
            percent_change = Back_Test.calculate_holding_percent_change_return(
                ticker + "CLS") * 100

            print "algorithm ", algorithm_return, '%'
            print "log return ", log_return, ' %'
            print "percent change", percent_change, '%'

            f.write(ticker + ',' + str(algorithm_return) + ',' + str(log_return) +
                    ',' + str(percent_change) + '\n')


def test_on_market_data_single_stock_profit():
    """
    This test is used to try out the returns calculator on the stock market data

    """

    main_df = pd.read_pickle('df_without_zeros.pkl')
    main_df = sample_slopes.create_slope_sum(main_df)

    Back_Test = back_test.BackTest(
        main_df, '/Users/jasonbamford/workspace/stock_surface/model_18_batch.pkl')

    y_values = sample_slopes.generate_target_values(
        main_df, 18, 'FBCLS', 2)

    x_values = sample_slopes.create_batch_of_slopes(
        main_df, 'FBCLS', 18,   y_values[1])

    array_of_batches = Back_Test.create_batch_of_slopes(
        main_df, 'FBslope_sum', 18, y_values[1])

    print array_of_batches, ' here is lensss'

    print Back_Test.append_list_of_buy_sells(array_of_batches,
                                             "FBslope_sum")

    print "algorithm ", sum(Back_Test.take_bid_stream_calculate_profit("FBbid_stream", 18, 2)),
    print "percent change", Back_Test.calculate_holding_profit("FBCLS"),


def test_on_array_of_tickers_profit():
    """
    This test is used to try out the returns calculator on the stock market data

    """
    tickers = ["GOOG", "FB", "INTC", 'TSM',
               "CSCO", "ORCL", "NVDA", "SAP", "IBM", "ADBE",
               "TXN", "AVGO", "CRM", "QCOM", "MU", "BIDU",
               "ADP", "VMW", "ATVI", "AMAT", "INTU",
               "CTSH", "EA", "EA", "NXPI", "INFY"]

    # tickers = ["GOOG", "FB", "INTC", 'TSM', "CSCO"]

    main_df = pd.read_pickle('df_without_zeros.pkl')
    main_df = sample_slopes.create_slope_sum(main_df)

    Back_Test = back_test.BackTest(
        main_df, '/Users/jasonbamford/workspace/stock_surface/model_18_batch.pkl')

    with open('return_output.csv', 'w') as f:
        for ticker in tickers:

            y_values = sample_slopes.generate_target_values(
                main_df, 18, ticker + "CLS", 2)

            x_values = sample_slopes.create_batch_of_slopes(
                main_df, ticker + 'CLS', 18,   y_values[1])

            array_of_batches = Back_Test.create_batch_of_slopes(
                main_df, ticker + 'slope_sum', 18, y_values[1])

            Back_Test.append_list_of_buy_sells(array_of_batches,
                                               ticker + "slope_sum")

            algorithm_return = sum(Back_Test.take_bid_stream_calculate_profit(
                ticker + "bid_stream", 18, 2))
            log_return = sum(
                Back_Test.test_calculate_holding_log_return(ticker + 'CLS'))
            percent_change = Back_Test.calculate_holding_profit(
                ticker + "CLS")

            print "algorithm ", algorithm_return, '%'
            print "log return ", log_return, ' %'
            print "percent change", percent_change, '%'

            f.write(ticker + ',' + str(algorithm_return) + ',' + str(log_return) +
                    ',' + str(percent_change) + '\n')