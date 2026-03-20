<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Soul Quotes</title>

<style>
body {
    background: #111;
    color: white;
    font-family: Arial;
    text-align: center;
    padding: 20px;
}

.container {
    max-width: 500px;
    margin: auto;
}

.quote {
    font-size: 20px;
    margin: 20px 0;
    padding: 15px;
    background: #222;
    border-radius: 10px;
}

button {
    padding: 10px 15px;
    margin: 5px;
    border: none;
    border-radius: 10px;
    cursor: pointer;
    transition: 0.3s;
}

button:hover {
    transform: scale(1.1);
}

.btn-main {
    background: #00c9a7;
    color: white;
}

.btn-copy {
    background: #444;
    color: white;
}

.light-mode {
    background: white;
    color: black;
}

.ad {
    margin: 15px 0;
    padding: 10px;
    background: #222;
    border-radius: 10px;
}
</style>
</head>

<body>

<div class="container">
<h2>✨ Soul Quotes ✨</h2>

<div class="ad">
🔥 Your Ad Here (AdSense later)
</div>

<div class="quote" id="quote">
Click below to feel something real...
</div>

<button class="btn-main" onclick="newQuote()">New Quote</button>
<button class="btn-copy" onclick="copyQuote()">Copy</button>
<button onclick="shareWhatsApp()" style="background:#25D366;color:white;">WhatsApp</button>
<button onclick="likeQuote()">❤️ Like</button>
<button onclick="toggleMode()">🌙 Mode</button>

<p id="likes">Likes: 0</p>

</div>

<script>
const quotes = [
"Sometimes you don’t need motivation. You need discipline.",
"You are not behind in life. You are on your own path.",
"Growth feels uncomfortable because you've never been here before.",
"Your future is created by what you do today, not tomorrow.",
"Silence is sometimes the loudest answer.",
"Not everything you lose is a loss.",
"Healing takes time. Don’t rush yourself.",
"You don’t have to be perfect to be amazing.",
"Small progress is still progress.",
"Be proud of how far you’ve come.",
"Your only competition is who you were yesterday.",
"Don’t let temporary emotions make permanent decisions.",
"The struggle you're in today builds the strength you need tomorrow.",
"Peace begins when expectations end.",
"Hard times create strong people."
];

let likes = 0;

function newQuote(){
    const q = document.getElementById("quote");
    const random = Math.floor(Math.random() * quotes.length);
    q.textContent = quotes[random];
}

function copyQuote(){
    const text = document.getElementById("quote").textContent;
    navigator.clipboard.writeText(text);
    alert("Copied!");
}

function shareWhatsApp(){
    const text = document.getElementById("quote").textContent;
    const url = window.location.href;
    const link = "https://wa.me/?text=" + encodeURIComponent(text + " - " + url);
    window.open(link, "_blank");
}

function likeQuote(){
    likes++;
    document.getElementById("likes").textContent = "Likes: " + likes;
}

function toggleMode(){
    document.body.classList.toggle("light-mode");
}

window.onload = function(){
    newQuote();
}
</script>

</body>
</html>
