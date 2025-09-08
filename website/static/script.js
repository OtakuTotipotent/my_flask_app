document.addEventListener('DOMContentLoaded', () => {
    const addButton = document.getElementById('add-item');
    const modalContainer = document.getElementById('modal-container');
    const closeModalButton = document.getElementById("close-modal");

    addButton.addEventListener('click', () => {
        modalContainer.classList.remove('hidden');
        console.log("hello")
    });

    closeModalButton.addEventListener('click', () => {
        console.log("hello")
        modalContainer.classList.add("hidden");
    });
});

console.log("hello")