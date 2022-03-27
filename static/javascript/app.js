const AllImages = document.querySelectorAll('.picture')

AllImages.forEach((image) => {
    image.addEventListener('click', () => {
        console.log(image.src)
    })
});

