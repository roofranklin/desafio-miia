from .student import router as student_router
from .activity import router as activity_router
from .question import router as question_router

__all__ = ["student_router", "activity_router", "question_router"]
