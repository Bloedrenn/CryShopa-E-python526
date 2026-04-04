# from fastapi import FastAPI

# app = FastAPI()

# 1
# notes_db = {
#   1: "Study FastAPI",
#   2: "I like FastAPI"
# }


# @app.get('/notes')
# async def get_notes() -> dict:
#   return notes_db


# 2
# from fastapi import HTTPException, status

# tasks_db = {
#   1: "Study FastAPI",
#   2: "I like FastAPI"
# }


# @app.get("/tasks/{task_id}")
# async def get_task(task_id: int) -> str:
#   try:
#     return tasks_db[task_id]
#   except:
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")



# 3
# from typing import Annotated

# from fastapi import Body, status

# reminders_db = {}


# @app.post('/reminders', status_code=status.HTTP_201_CREATED)
# async def create_reminder(reminder: Annotated[str, Body()]) -> str:
#   new_index = max(reminders_db) + 1 if reminders_db else 0
#   reminders_db[new_index] = reminder
#   return "Reminder created!"



# 4
# from typing import Annotated

# from fastapi import Body, HTTPException, status

# quotes_db = {
#   1: "FastAPI lets you build APIs fast with type hints",
#   2: "Auto docs at /docs and /redoc with OpenAPI",
#   3: "Pydantic validates your data",
#   4: "Depends gives clean Dependency Injection",
#   5: "Use async def and await for concurrency"
# }


# @app.put('/quotes/{quote_id}')
# async def update_quote(quote_id: int, quote: Annotated[str, Body()]) -> str:
#   if quote_id in quotes_db:
#     quotes_db[quote_id] = quote
#     return "Quote updated!"

#   raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Quote not found")



# 5
# from fastapi import HTTPException, status

# goals_db = {
#   1: "Learn FastAPI basics",
#   2: "Build CRUD app",
#   3: "Write tests with TestClient",
#   4: "Add authentication",
#   5: "Deploy to production"
# }


# @app.delete("/goals/{goal_id}")
# async def delete_goal(goal_id: int) -> str:
#   try:
#     goals_db.pop(goal_id)
#     return "Goal deleted!"
#   except:
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Goal not found")



# 6
# from typing import Annotated

# from fastapi import Body, HTTPException, status

# comments_db = {
#   1: "First comment in FastAPI"
# }


# @app.get("/comments")
# async def read_comments() -> dict:
#   return comments_db


# @app.get("/comments/{comment_id}")
# async def read_comment(comment_id: int) -> str:
#   if comment_id in comments_db:
#     return comments_db[comment_id]
#   raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Comment not found")


# @app.post("/comments", status_code=status.HTTP_201_CREATED)
# async def create_comment(comment: Annotated[str, Body()]) -> str:
#   new_index = max(comments_db) + 1 if comments_db else 0
#   comments_db[new_index] = comment
#   return "Comment created!"


# @app.put("/comments/{comment_id}")
# async def update_comment(comment_id: int, comment: Annotated[str, Body()]) -> str:
#   if comment_id not in comments_db:
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Comment not found")

#   comments_db[comment_id] = comment
#   return "Comment updated!"


# @app.delete("/comments/{comment_id}")
# async def delete_comment(comment_id: int) -> str:
#   try:
#     comments_db.pop(comment_id)
#     return "Comment deleted!"
#   except:
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Comment not found")



# # Можно использовать:
# # def is_comment_in_db(comment_id: int) -> bool:
# #   if comment_id not in comments_db:
# #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Comment not found")

# #   return True
