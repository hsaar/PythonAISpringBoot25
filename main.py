from fastapi import FastAPI
from pydantic import BaseModel
# 데이터 유효성 검사와 설정 관리에 사용되는 라이브러리(모델링이 쉽고 강력함)

from starlette.middleware.base import BaseHTTPMiddleware
# 요청과 응답사이에 특정 작업 수행
# 미들웨어는 모든 요청에 대해 실행되며, 요청을 처리하기 전에 응답을 반환하기 전에 특정 작업을 수행할 수 있음
# 예를 들어 로깅, 인증, cors처리, 압축등...

import logging # 로깅 처리용 메서드

app = FastAPI( # 앱의 시그니처와 환경설정을 담당
    title="MBC AI Study",
    description="MBC AI study",
    version="0.0.1",
    docs_url=None,
    redoc_url=None,
)

class LoggingMiddleware(BaseHTTPMiddleware): # 로그를 콘솔에 출력하는 용도
    logging.basicConfig(level=logging.INFO) # 로그 출력 추가
    async def dispatch(self, request, call_next):
        logging.info(f"Req: {request.method}{request.url}")
        response = await call_next(request)
        logging.info(f"Status Code: {response.status_code}")
        return response
app.add_middleware(LoggingMiddleware) # 모든 요청에 대해 로그를 남기는 미들웨어 클래스 사용

class Item(BaseModel): # 아이템 객체 검증용
    name: str
    description: str = None
    price: float
    tax: float = None
    
@app.post("/items") # Post 매서드용 요청 (create)
async def create_item(item: Item):
    # BaseModel은 데이터 모델링을 쉽게 도와주고 유효성검사도 수행
    # 잘못된 데이터가 들어오면 422 반환
    return item

@app.get("/") # 웹 브라우저 http://localhost:8001/ -> Get 요청 시 처리
async def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}") # http://localhost:8001/items/1~ -> Get 요청 시 처리
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
    # item_id : 상품의 번호 -> 경로 매개변수
    # q : 쿼리 매개변수

# postman은 프론트가 없는 백앤드 테스트용 프로그램으로 활용

# 서버 실행은 uvicorn main:app --reload --port 8001
# 파이썬 백앤드 가동 서버로 main.py에 app이라는 매서드 사용