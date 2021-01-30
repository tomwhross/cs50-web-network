document.addEventListener('DOMContentLoaded', function() {
  console.log(document.querySelector('#post-message').value);
  document.querySelector('#post-message').onkeyup = function () {
      document.querySelector('#post-chars-remaining-message').innerHTML = `<b>${240 - this.value.length}</b> characters remaining`;
  }

  document.querySelector('#like-post').addEventListener('click', () => like_post());
});

function like_post() {
  console.log("Like post");
}