from django.urls import path
from .views import solve_sudoku_view, solve_sudoku_api

urlpatterns = [
    path('solve_sudoku/', solve_sudoku_view, name='solve_sudoku_view'),
    path('solve_sudoku_api/', solve_sudoku_api, name='solve_sudoku_api'),
]
