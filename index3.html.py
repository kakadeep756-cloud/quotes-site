<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Soul Quotes</title>

<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;500&display=swap" rel="stylesheet">

<style>
body {
    font-family: 'Poppins', sans-serif;
    margin: 0;
    background: #111;
    color: white;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}

.container {
    max-width: 400px;
    text-align: center;
    padding: 20px;
}

.quote {
    font-size: 20px;
    margin: 20px 0;
    line-height: 1.5;
}

button {
    padding: 10px 15px;
    border: none;
    border-radius: 10px;
    margin: 5px;
    cursor: pointer;
}

.btn-main { background: #00c9a7; color: white; }
.btn-copy { background: #444; color: white; }

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
    <h2>✨ Soul Quotes</h2>

    <!-- Ad placeholder -->
    <div class="ad">
        🔥 Your Ad Here (AdSense later)
    </div>

    <div class="quote" id="quote">
        Click below to feel something real...
    </div>

    <button class="btn-main" onclick="newQuote()">New Quote</button>
    <button class="btn-copy" onclick="copyQuote()">Copy</button>
</div>

<script>

const quotes = [
"Sometimes you don’t need motivation. You need discipline.",
"You are not behind in life. You are on your own path.",
"Growth feels uncomfortable because you’ve never been here before.",
"Your future is created by what you do today, not tomorrow.",
"Silence is sometimes the loudest answer.",
"Not everything you lose is a loss.",
"Healing takes time. Don’t rush yourself.",
"You don’t have to be perfect to be amazing.",
"Small progress is still progress.",
"Be proud of how far you’ve come.",
"Your only competition is who you were yesterday.",
"Don’t let temporary emotions make permanent decisions.",
"The struggle you’re in today builds the strength you need tomorrow.",
"Peace begins when expectations end.",
"Hard times create strong people."
];

function newQuote(){
    const q = document.getElementById("quote");
    const random = Math.floor(Math.random()*quotes.length);
    q.textContent = quotes[random];
}

function copyQuote(){
    const text = document.getElementById("quote").textContent;
    navigator.clipboard.writeText(text);
    alert("Copied!");
}

</script>

</body>
</html>