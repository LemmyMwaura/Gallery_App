const allImages = document.querySelectorAll('.picture')
const overlay = document.getElementById('overlay')

allImages.forEach((image) => {
    image.addEventListener('click', () => {
        let modal = image.parentElement.nextElementSibling
        openModal(modal)
    })
})

overlay.addEventListener('click', () => {
    const modals = document.querySelectorAll('.modal.active')
    modals.forEach((modal) => {
        closeModal(modal)
    })
})

function openModal(modal){
    if (modal == null) return
    modal.classList.add('active')
    overlay.classList.add('active')
}

function closeModal(modal){
    if (modal == null) return
    modal.classList.remove('active')
    overlay.classList.remove('active')
}
