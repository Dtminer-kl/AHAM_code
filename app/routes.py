from flask import request, jsonify
from . import db
from .models import InvestmentFund
from . import create_app

app = create_app()

@app.route('/funds', methods=['GET'])
def get_funds():
  ##Get listt of all funds
    funds = InvestmentFund.query.all()
    return jsonify([fund.to_dict() for fund in funds])

@app.route('/funds', methods=['POST'])
def create_fund():
  ##Create new funds
    data = request.get_json()
    new_fund = InvestmentFund(
        fund_name=data['fund_name'],
        fund_manager_name=data['fund_manager_name'],
        fund_description=data['fund_description'],
        fund_nav=data['fund_nav'],
        fund_creation_date=data['fund_creation_date'],
        fund_performance=data['fund_performance']
    )
    db.session.add(new_fund)
    db.session.commit()
    return jsonify(new_fund.to_dict()), 201

@app.route('/funds/<int:fund_id>', methods=['GET'])
def get_fund(fund_id):
  ##Get detials of fund using ID
    fund = InvestmentFund.query.get_or_404(fund_id)
    return jsonify(fund.to_dict())

@app.route('/funds/<int:fund_id>', methods=['PUT'])
def update_fund_performance(fund_id):
  ##Update fund via id
    data = request.get_json()
    fund = InvestmentFund.query.get_or_404(fund_id)
    fund.fund_performance = data.get('fund_performance', fund.fund_performance)
    db.session.commit()
    return jsonify(fund.to_dict())

@app.route('/funds/<int:fund_id>', methods=['DELETE'])
def delete_fund(fund_id):
  ##Delete fund via id
    fund = InvestmentFund.query.get_or_404(fund_id)
    db.session.delete(fund)
    db.session.commit()
    return jsonify({'message': 'Fund deleted'})
