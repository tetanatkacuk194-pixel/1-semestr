from pydantic import BaseModel

class Course(BaseModel): # Створює нове правило для перевірки інформації про навчальний курс
    title: str
    code: int

def demo_pydantic():#Оголошує функцію для перевірки валідації
    course = Course(title="Python Dev", code=101)
    print(f"[Pydantic] Дані валідовано: {course.title}")
