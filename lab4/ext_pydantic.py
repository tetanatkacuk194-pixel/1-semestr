from pydantic import BaseModel

class Course(BaseModel):
    title: str
    code: int

def demo_pydantic():
    course = Course(title="Python Dev", code=101)
    print(f"[Pydantic] Дані валідовано: {course.title}")