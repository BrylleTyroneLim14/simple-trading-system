# simple-trading-system

# Clone the repository
git clone https://github.com/BrylleTyroneLim14/simple-trading-system.git

# Create a virtual environment to isolate our package dependencies locally
python3 -m venv trading_system_env
source trading_system_env/bin/activate  # On Windows use `.\trading_system_env\Scripts\activate`

# Install Django and Django REST framework into the virtual environment
pip install django
pip install djangorestframework

# Another way to install the package use in the project
cd simple-trading-system
pip install -r requirements.txt

# Sample CURL to test the REST API
curl -d '{"user_id":1, "trade_type":"sell","stock_id":1,"quantity":10}' -H "Content-Type: application/json" --header "Authorization: Token eb6e610f3c0542e84da06309e94a7766ecc8b109" -X POST http://localhost:8000/api/place-trade/

curl -d '{"user_id":1, "trade_type":"buy","stock_id":2}' -H "Content-Type: application/json" --header "Authorization: Token eb6e610f3c0542e84da06309e94a7766ecc8b109" -X POST http://localhost:8000/api/total-value/