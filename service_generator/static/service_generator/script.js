document.addEventListener("DOMContentLoaded", function(event) {
    const labels = document.getElementsByTagName("label");
    for (let i = 0; i < labels.length; i++) {
        if (labels[i].htmlFor !== "") {
            const input = document.getElementById(labels[i].htmlFor);
            if (input.required) {
                labels[i].style.fontWeight = "bold";
            }
        }
    }
});