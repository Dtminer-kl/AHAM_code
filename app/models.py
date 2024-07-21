from . import db

class InvestmentFund:
    def __init__(self, fund_id, fund_name, fund_manager_name, fund_description, fund_nav, fund_creation_date, fund_performance):
        self.fund_id = fund_id
        self.fund_name = fund_name
        self.fund_manager_name = fund_manager_name
        self.fund_description = fund_description
        self.fund_nav = fund_nav
        self.fund_creation_date = fund_creation_date
        self.fund_performance = fund_performance
        
def to_dict(self):
        return {
            'fund_id': self.id,
            'fund_name': self.fund_name,
            'fund_manager_name': self.fund_manager_name,
            'fund_description': self.fund_description,
            'fund_nav': self.fund_nav,
            'fund_creation_date': self.fund_creation_date.strftime('%Y-%m-%d'),
            'fund_performance': self.fund_performance
        }
  
