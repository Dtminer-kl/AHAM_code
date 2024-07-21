import pytest
from app import create_app, db
from app.models import InvestmentFund

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        db.drop_all()

def test_create_fund(client):
    response = client.post('/funds', json={
        'fund_name': 'Test Fund',
        'fund_manager_name': 'Test Manager',
        'fund_description': 'A test fund',
        'fund_nav': 100.0,
        'fund_creation_date': '2024-07-21',
        'fund_performance': 10.0
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data['fund_name'] == 'Test Fund'

def test_get_fund(client):
    fund = InvestmentFund(
        fund_name='Test Fund',
        fund_manager_name='Test Manager',
        fund_description='A test fund',
        fund_nav=100.0,
        fund_creation_date='2024-07-21',
        fund_performance=10.0
    )
    db.session.add(fund)
    db.session.commit()
    response = client.get(f'/funds/{fund.id}')
    assert response.status_code == 200
    data = response.get_json()
    assert data['fund_name'] == 'Test Fund'
