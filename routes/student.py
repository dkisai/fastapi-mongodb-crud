#import statements
from fastapi import APIRouter
from models.student import Student
from config.database import connection

student_router = APIRouter()

@student_router.get('/hello')
async def hello_world():
    return 'Hello'

@student_router.get('/students')
def find_all_students():
    return connection.local.student.find()