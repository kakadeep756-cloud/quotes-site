<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Community Feed</title>

<style>
body {
    font-family: Arial;
    background: #111;
    color: white;
    text-align: center;
    padding: 20px;
}

.container {
    max-width: 500px;
    margin: auto;
}

input, textarea {
    width: 90%;
    padding: 10px;
    border-radius: 10px;
    border: none;
    margin: 5px 0;
}

textarea {
    height: 80px;
}

button {
    padding: 8px 12px;
    border-radius: 10px;
    border: none;
    cursor: pointer;
    margin: 5px;
}

.post {
    background: #222;
    padding: 15px;
    margin: 10px 0;
    border-radius: 15px;
    text-align: left;
}

.username {
    font-weight: bold;
}

.time {
    font-size: 12px;
    color: gray;
}

.actions {
    margin-top: 10px;
}
</style>
</head>

<body>

<div class="container">
<h2>🌍 Community Feed</h2>

<input id="username" placeholder="Enter your name">
<textarea id="userInput" placeholder="Write your story or quote..."></textarea>
<br>
<button onclick="addPost()">Post</button>

<h3>📢 Feed</h3>
<div id="posts"></div>

</div>

<script>

function addPost(){
    const username = document.getElementById("username").value || "Anonymous";
    const text = document.getElementById("userInput").value.trim();

    if(text === ""){
        alert("Write something!");
        return;
    }

    const time = new Date().toLocaleString();

    const postDiv = document.createElement("div");
    postDiv.className = "post";

    let likes = 0;

    postDiv.innerHTML = `
        <div class="username">${username}</div>
        <div>${text}</div>
        <div class="time">${time}</div>
        <div class="actions">
            <button onclick="likePost(this)">❤️ 0</button>
            <button onclick="deletePost(this)">🗑️</button>
        </div>
    `;

    document.getElementById("posts").prepend(postDiv);

    document.getElementById("userInput").value = "";
}

function likePost(btn){
    let count = parseInt(btn.innerText.split(" ")[1]);
    count++;
    btn.innerText = "❤️ " + count;
}

function deletePost(btn){
    btn.parentElement.parentElement.remove();
}

</script>

</body>
</html>
