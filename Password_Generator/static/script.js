let container = document.getElementById('container')
let value = document.querySelector('.lengthvalue')
let input = document.querySelector('.Length')
value.textContent = input.value
input.addEventListener('input',(event) => {
    value.textContent = event.target.value;
})



setTimeout(() => {
    container.classList.add('sign-in')
}, 200)