from app import create_app
import uvicorn


api_customer = create_app (
    title = 'api-customer-softfinance',
    description = 'Api to manage customer resources'
)


if __name__ == '__main__':
    uvicorn.run('main:api_customer', host='0.0.0.0', port=9000, reload=True)