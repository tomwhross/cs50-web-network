document.addEventListener('DOMContentLoaded', function() {
    edit_buttons = document.querySelectorAll('.edit_post');
    cancel_buttons = document.querySelectorAll('.cancel-button');
    save_buttons = document.querySelectorAll('.save-button');

    edit_buttons.forEach(function(edit_button) {
        edit_button.addEventListener('click', function() {
            post_id = this.dataset.editid;
            post_container = document.querySelector(`div[data-post_container_id="${post_id}"]`);
            edit_container = document.querySelector(`div[data-edit_container_id="${post_id}"]`);
             
            post_container.style.display = 'none';
            edit_container.style.display = 'block';
        });
    });

    cancel_buttons.forEach(function(cancel_button) {
        cancel_button.addEventListener('click', function() {
            post_id = this.dataset.cancelid;

            post_container = document.querySelector(`div[data-post_container_id="${post_id}"]`);
            edit_container = document.querySelector(`div[data-edit_container_id="${post_id}"]`);

            post_container.style.display = 'block';
            edit_container.style.display = 'none';
        });
    });

    save_buttons.forEach(function(save_button) {
        save_button.addEventListener('click', function() {
            post_id = this.dataset.saveid;

            text = document.querySelector(`#text_${post_id}`).value; 

            post_container = document.querySelector(`div[data-post_container_id="${post_id}"]`);
            edit_container = document.querySelector(`div[data-edit_container_id="${post_id}"]`);

            post = document.querySelector(`div[data-message="${post_id}"]`);
           
            // message = {'message': text};

            fetch(`/post/${post_id}`, {
                credentials: 'include',
                method: 'POST',
                mode: 'same-origin',
                headers: {
                  'Accept': 'application/json',
                  'Content-Type': 'application/json',
                  'X-CSRFToken': getCookie('csrftoken') 
                },
                body: JSON.stringify({message: text}),
            })
            .then(response => response.json())
            .then(result => {
                console.log(result);
            });

            post.innerHTML = text;
            post_container.style.display = 'block';
            edit_container.style.display = 'none';
        });
    });
});

function getCookie(name) {
    if (!document.cookie) {
      return null;
    }
    
    const token = document.cookie.split(';')
    .map(c => c.trim())
    .filter(c => c.startsWith(name + '='));
  
    if (token.length === 0) {
      return null;
    }
    
    return decodeURIComponent(token[0].split('=')[1]);
 }
