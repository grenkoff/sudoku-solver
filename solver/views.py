import json
from django.shortcuts import render
from django.http import JsonResponse
from .services.sudoku_solver import solve_sudoku

def solve_sudoku_view(request):
    return render(request, 'solver/solve_sudoku.html')

def solve_sudoku_api(request):
    if request.method == 'POST':
        data = request.POST.get('board')
        if data:
            try:
                board = json.loads(data)
                if len(board) != 9 or any(len(row) != 9 for row in board):
                    return JsonResponse({'error': 'Invalid board'}, status=400)

                # Call the sudoku solver service
                if solve_sudoku(board):
                    return JsonResponse({'solution': board})
                else:
                    return JsonResponse({'error': 'No solution'}, status=400)
            except json.JSONDecodeError:
                return JsonResponse({'error': 'Invalid JSON data'}, status=400)
        else:
            return JsonResponse({'error': 'Board data not provided'}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
