import uvicorn
from api import FastAPI, create_app


api_auth: FastAPI = create_app(
    title = 'api-auth-softfinance',
    description = 'Auth api to manage users and login.'
)


if __name__ == '__main__':
    uvicorn.run('main:api_auth', port=9000, reload=True)