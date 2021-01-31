document.addEventListener('DOMContentLoaded', function() {
  follow_button = document.querySelector('#follow-user');
  follow_button.addEventListener('click', function() {
    console.log(`clicked follow on ${this.dataset.userid}`);

    fetch(`/follow_user/${this.dataset.userid}`, {
      credentials: 'include',
      method: 'POST',
      mode: 'same-origin',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'X-CSRFToken': getCookie('csrftoken') 
      },
    })
    .then(response => response.json())
    .then(result => {
      if (result.followed === true) {
        console.log(`followed: ${result.followed}`);
        follow_button.innerHTML = 'Unfollow user';
        console.log(follow_button);
      }
      else {
        console.log(`followed: ${result.followed}`);
        follow_button.innerHTML = 'Follow user';
        console.log(follow_button);
      }
    });
  });
});
    
function like_post() {
  console.log("Like post");
  console.log(dataset.id);
}

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