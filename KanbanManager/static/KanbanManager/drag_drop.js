const list_items = document.querySelectorAll('.list-item');
const lists = document.querySelectorAll('.list');

let draggedItem = null;

for (let i = 0; i < list_items.length; i++) {
	const item = list_items[i];
	const bgcolor = item.style.backgroundColor;


	item.addEventListener('dragstart', function () {
		draggedItem = item;
		setTimeout(function () {
			item.style.display = 'none';
		}, 0)
	});

	item.addEventListener('dragend', function () {
		setTimeout(function () {
			draggedItem.style.display = 'block';
			draggedItem = null;
		}, 0);
	})

	for (let j = 0; j < lists.length; j ++) {
		const list = lists[j];
		const bgcolor = list.style.backgroundColor;

		list.addEventListener('dragover', function (e) {
			e.preventDefault();
			this.style.backgroundColor = 'rgba(0, 0, 0, 0.2)';
		});
		
		list.addEventListener('dragenter', function (e) {
			e.preventDefault();
		});

		list.addEventListener('dragleave', function (e) {
			this.style.backgroundColor = bgcolor;
		});

		list.addEventListener('drop', function (e) {
			this.querySelector(".card-body").append(draggedItem);
			cardId = draggedItem.id;
			newColumn = j;
			//this.style.backgroundColor = 'rgba(0, 0, 0, 0.1)';

			// create a post request to the server to update the database
			var xhr = new XMLHttpRequest();
			xhr.onreadystatechange = function() {};
			xhr.open('POST', `/update_card/${cardId}/${newColumn}`);
			xhr.send();
		});
	}
}