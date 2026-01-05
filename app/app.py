from fastapi import FastAPI,HTTPException
from app.schemas import PostCreate,PostResponse
from app.db import Post,create_db_and_tables,get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app:FastAPI):
    await create_db_and_tables()
    yield


app=FastAPI(lifespan=lifespan)

text_posts = {
    1: {"title": "New Post", "content": "Cool test post"},
    2: {"title": "Update", "content": "This is an update post"},
    3: {"title": "Announcement", "content": "Big news coming soon"},
    4: {"title": "Daily Thoughts", "content": "Just sharing some thoughts"},
    5: {"title": "Tech Talk", "content": "Let’s discuss new technology"},
    6: {"title": "Reminder", "content": "Don’t forget to check this out"},
    7: {"title": "Question", "content": "What do you think about this?"},
    8: {"title": "Tips", "content": "Here are some useful tips"},
    9: {"title": "Feedback", "content": "We value your feedback"},
    10: {"title": "Final Note", "content": "Thanks for reading"}
}


@app.get("/posts")
def get_all_posts(limit:int):
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts

@app.get("/posts/{id}")
def get_post(id:int):
    if id not in text_posts:
        raise HTTPException(status_code=404,detail="Post not found")
    return text_posts.get(id)

@app.post("/posts")
def create_post(post:PostCreate)->PostResponse:
    new_post={"title":post.title,"content":post.content}
    text_posts[max(text_posts.keys())+1]=new_post
    return new_post


