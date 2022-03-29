const allImages = document.querySelectorAll('.picture')
const overlay = document.getElementById('overlay')
const copyButtons = document.querySelectorAll('.copy-btn')

// Copy link
copyButtons.forEach((btn) => {
    console.log(btn)
    btn.addEventListener('click', () => {
        let link = btn.closest('.modal').previousElementSibling.firstElementChild
        navigator.clipboard.writeText(link.src)
        btn.classList.add('active')
    }) 
})

// modal
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

    const activeBtns = document.querySelectorAll('.copy-btn.active')
    activeBtns.forEach( (btn) => {
        btn.classList.remove('active')
    }) 
}

