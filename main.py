from datetime import datetime 
import pull_stock  as pt

if __name__ == '__main__':
    company_name = "GOOGL" 
    start_date =  datetime(2004,8,19).date()
    end_date = datetime.now().date()
    current_stock_history = pt.pull_stock_data(company_name,start_date,end_date)
    pt.PreProcessing(current_stock_history)