from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal

router = APIRouter()

users = []

@router.post('/register')
def register():
    return {}

@router.post('/login')
def login():
    return {}

@router.get('/unprotected')
def unprotected():
    return {'hello' : 'world'}

@router.get('/protected')
def protected():
    return {}