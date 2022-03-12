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