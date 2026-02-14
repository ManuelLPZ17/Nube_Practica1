const form = document.getElementById("productForm");
const responseText = document.getElementById("response");

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const formData = new FormData(form);

    const API_URL = `${window.location.protocol}//${window.location.hostname}:${window.location.port}`;

    const response = await fetch(`${API_URL}/upload`, {
        method: "POST",
        body: formData
    });

    const data = await response.json();
    responseText.innerText = data.message;
});
