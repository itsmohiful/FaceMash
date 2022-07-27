const message = document.querySelector('.message');


if (message) {
   setTimeout(() => {
     message.classList.add("message-hide");
   }, 3000);
}



// setInterval(() => {
//     const now = new Date();
   
//     console.log(now.toLocaleTimeString())
// }, 1000);



// Delete post

const deleteButtons = Array.from(document.querySelectorAll(".delete-btn"));
const modal = document.querySelector(".modal");
const cancelButton = document.querySelector(".cancel-btn");
const confirmButton = document.querySelector(".confirm-btn");

function modalOpen() {
   modal.classList.add("modal-open");
}

function modalClose() {
   modal.classList.remove("modal-open");
}

//delete post
async function deletePost() {
  try {
      await fetch(`/post/${this.dataset.id}/delete`);
      modalClose();
      window.location = "/";
  } catch (err) {
    console.log(err);
  }
}



confirmButton.addEventListener("click", deletePost);
deleteButtons.forEach((button) => button.addEventListener("click", modalOpen));
cancelButton.addEventListener('click', modalClose);



// async function getPosts() {
//   const res = await fetch("https://jsonplaceholder.typicode.com/posts");
//   const data = await res.json()
//   console.log(data);
// }

// getPosts();


// Accordion
function myFunction(id) {
    var x = document.getElementById(id);
    if (x.className.indexOf("w3-show") == -1) {
        x.className += " w3-show";
        x.previousElementSibling.className += " w3-theme-d1";
    } else {
        x.className = x.className.replace("w3-show", "");
        x.previousElementSibling.className =
        x.previousElementSibling.className.replace(" w3-theme-d1", "");
    }
}

// Used to toggle the menu on smaller screens when clicking on the menu button
function openNav() {
    var x = document.getElementById("navDemo");
    if (x.className.indexOf("w3-show") == -1) {
        x.className += " w3-show";
    } else {
        x.className = x.className.replace(" w3-show", "");
    }
}