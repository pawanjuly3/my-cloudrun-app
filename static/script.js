async function sendData() {
    const text = document.getElementById("textInput").value;
    const res = await fetch("/process", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text })
    });
    const data = await res.json();
    document.getElementById("result").innerText = data.result;
}
