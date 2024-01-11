
# def get_task(request):
#     task_id = request.form.get('taskid')
#     task = TodoItem.query.filter_by(id=task_id).first()
#     return task


# def index():
#     users = User.query.all()
#     lists = TodoList.query.order_by('id').all()
#     tasks = TodoItem.query.all()
#     print(f"debug tasks: {tasks}")
#     return render_template('index.html', users=users,lists=lists, tasks=tasks)

# def add_list():
#     name = request.get_json()['name']
#     list = TodoList(name=name)
#     db.session.add(list)
#     db.session.commit()
    
#     return jsonify({
#         'id': list.id,
#         'name': list.name
#     })


# def delete_list():
#     listid = request.get_json()['listid']
#     todo_list = TodoList.query.get(listid)

#     if todo_list:
#         todo_list.delete()
#     else:
#         print("No TodoList with that Id exists")

#     return jsonify({
#         'id': todo_list.id,
#         'name': todo_list.name
#     })    

# def add_task():
#     list_id = request.form.get('listid')
#     description = request.form.get('description')
#     task = TodoItem(description=description, list_id=list_id)
#     db.session.add(task)
#     db.session.commit()
#     return redirect(url_for('index'))

# @app.route('/task-completion', methods=['POST'])
# def task_completion():
#     task_id = request.get_json()['taskid']
#     print(f"debug task id: {task_id}")
#     if task_id:
#         task = TodoItem.query.get(task_id)
#         task.completed = not task.completed
#         db.session.commit()
#     return jsonify({
#         'id': task.id,
#         'completed': task.completed
#     })


# def delete_task():
#     task_id = request.get_json()['taskid']
#     print(f"debug task id: {task_id}")
#     if task_id:
#         task = TodoItem.query.get(task_id)
#         task.delete()
       
#     return jsonify({
#         'id': task.id,
#         'description': task.description
#     })


# def users():
#     users = User.query.all()
#     return render_template('users.html', users=users)


# def add_user():
#     name = request.form.get('name')
#     user = User(name=name, email=f"{name.lower()}@mail.com")
#     db.session.add(user)
#     db.session.commit()
#     return redirect(url_for('users'))