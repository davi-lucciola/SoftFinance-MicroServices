from api import create_app
import uvicorn


api_auth = create_app (
    title = 'api-auth-softfinance',
    description = 'Auth api to manage users and login.'
)


if __name__ == '__main__':
    uvicorn.run('main:api_auth', host='0.0.0.0', port=9000, reload=True)