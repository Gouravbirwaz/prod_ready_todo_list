from django.shortcuts import redirect, render
from django.http import JsonResponse
from .models import ToDoModel
from .forms import TodoForm


def get_all_todo(request):
    all_todo = ToDoModel.objects.all()
    form = TodoForm()
    return render(request, 'homepage.html', {'all_todo': all_todo, 'form': form})


def add_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('all')
    else:
        form = TodoForm()

    return render(request, 'homepage.html', {'all_todo': ToDoModel.objects.all(), 'form': form})


def remove_todo(request):
    if request.method == 'POST':
        todo_id = request.POST.get('id')
        if not todo_id:
            return JsonResponse({'success': False, 'message': 'Todo id is required'}, status=400)

        todo = ToDoModel.objects.filter(id=todo_id).first()
        if not todo:
            return JsonResponse({'success': False, 'message': 'Todo not found'}, status=404)

        todo.delete()
        return JsonResponse({'success': True, 'message': 'Todo deleted successfully'})

    return JsonResponse({'success': False, 'message': 'Invalid request method'}, status=405)


def edit_todo(request):
    if request.method in ['POST', 'PUT']:
        todo_id = request.POST.get('id') or request.GET.get('id')
        if not todo_id:
            return JsonResponse({'success': False, 'message': 'Todo id is required'}, status=400)

        todo = ToDoModel.objects.filter(id=todo_id).first()
        if not todo:
            return JsonResponse({'success': False, 'message': 'Todo not found'}, status=404)

        form = TodoForm(request.POST, request.FILES, instance=todo)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'message': 'Todo updated successfully'})

        return JsonResponse({'success': False, 'errors': form.errors}, status=400)

    return JsonResponse({'success': False, 'message': 'Invalid request method'}, status=405)

