document.addEventListener('DOMContentLoaded', function () {
  const input = document.getElementById('todo-input');
  const addBtn = document.getElementById('add-btn');
  const list = document.getElementById('todo-list');

  function createTodoItem(text) {
    const li = document.createElement('li');
    li.className = 'todo-item';
    const content = document.createElement('div');
    content.className = 'content';

    const checkbox = document.createElement('input');
    checkbox.type = 'checkbox';
    checkbox.className = 'complete-checkbox';
    checkbox.addEventListener('change', function () {
      li.classList.toggle('completed', checkbox.checked);
    });

    const span = document.createElement('span');
    span.textContent = text;
    span.addEventListener('click', function () {
      checkbox.checked = !checkbox.checked;
      checkbox.dispatchEvent(new Event('change'));
    });

    const del = document.createElement('button');
    del.className = 'delete-btn';
    del.textContent = 'Delete';
    del.addEventListener('click', function () {
      li.remove();
    });

    content.appendChild(checkbox);
    content.appendChild(span);
    li.appendChild(content);
    li.appendChild(del);
    return li;
  }

  addBtn.addEventListener('click', function () {
    const val = input.value.trim();
    if (!val) return;
    list.appendChild(createTodoItem(val));
    input.value = '';
    input.focus();
  });

  input.addEventListener('keydown', function (e) {
    if (e.key === 'Enter') addBtn.click();
  });
});
