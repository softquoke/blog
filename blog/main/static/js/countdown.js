let elements = document.getElementsByClassName("numberOfPost");

function main() {
    for (let i = 0; i < elements.length; i++) {
        elements[i].textContent = ((elements[i].id) >>> 0).toString(2);
    }
}

window.onload = main;